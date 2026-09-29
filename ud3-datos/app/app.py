"""Listado 3.20. Panel de ventas con Streamlit.

Local:     streamlit run ud3-datos/app/app.py
Publicado: https://share.streamlit.io -> elegir el repositorio y este fichero
"""

from pathlib import Path

import pandas as pd
import streamlit as st

RUTA = Path(__file__).parent / "datos" / "ventas_2026.csv"

st.set_page_config(page_title="Ventas 2026", page_icon="📊", layout="wide")


@st.cache_data                      # se calcula una vez; no en cada interacción
def cargar_ventas(ruta: Path) -> pd.DataFrame:
    """Lee y limpia el fichero de ventas."""
    ventas = pd.read_csv(ruta, sep=";", decimal=",", parse_dates=["fecha"])
    ventas = ventas.drop_duplicates()
    ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
    ventas["canal"] = ventas["canal"].fillna("desconocido")
    ventas["unidades"] = ventas["unidades"].fillna(ventas["unidades"].median())
    ventas["unidades"] = ventas["unidades"].astype("int64")
    return ventas.assign(importe=lambda df: (df["unidades"] * df["precio"]).round(2))


ventas = cargar_ventas(RUTA)

st.title("📊 Panel de ventas 2026")
st.caption("Datos de ejemplo del módulo Python aplicado a la Inteligencia Artificial")

# --- Filtros ---------------------------------------------------------------
with st.sidebar:
    st.header("Filtros")
    ciudades = st.multiselect(
        "Ciudades",
        options=sorted(ventas["ciudad"].unique()),
        default=sorted(ventas["ciudad"].unique()),
    )
    canales = st.multiselect(
        "Canales",
        options=sorted(ventas["canal"].unique()),
        default=sorted(ventas["canal"].unique()),
    )
    minimo, maximo = st.slider(
        "Importe por venta (€)",
        min_value=0,
        max_value=int(ventas["importe"].max()),
        value=(0, int(ventas["importe"].max())),
        step=100,
    )

filtradas = ventas[
    ventas["ciudad"].isin(ciudades)
    & ventas["canal"].isin(canales)
    & ventas["importe"].between(minimo, maximo)
]

if filtradas.empty:
    st.warning("Ningún dato cumple los filtros seleccionados.")
    st.stop()

# --- Indicadores -----------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Facturación", f"{filtradas['importe'].sum():,.0f} €")
col2.metric("Ventas", f"{len(filtradas):,}")
col3.metric("Ticket medio", f"{filtradas['importe'].mean():,.0f} €")

# --- Gráficos --------------------------------------------------------------
izquierda, derecha = st.columns(2)

with izquierda:
    st.subheader("Evolución mensual")
    mensual = filtradas.set_index("fecha")["importe"].resample("ME").sum()
    st.line_chart(mensual)

with derecha:
    st.subheader("Facturación por ciudad")
    st.bar_chart(filtradas.groupby("ciudad")["importe"].sum().sort_values())

# --- Tabla y descarga ------------------------------------------------------
st.subheader("Detalle")
resumen = (
    filtradas.groupby(["ciudad", "canal"])
    .agg(ventas=("id_venta", "count"), importe=("importe", "sum"))
    .round(2)
    .reset_index()
    .sort_values("importe", ascending=False)
)
st.dataframe(resumen, width="stretch", hide_index=True)

st.download_button(
    "Descargar resumen en CSV",
    data=resumen.to_csv(index=False, sep=";", decimal=",").encode("utf-8"),
    file_name="resumen_ventas.csv",
    mime="text/csv",
)
