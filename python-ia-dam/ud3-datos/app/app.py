"""Panel de exploración de jugadores de FIFA 20.

Es el listado 3.20 preparado para desplegarse en Streamlit Community Cloud:
la única diferencia es que aquí la carga de datos va incluida, porque en el
servidor no existe la carpeta `listados/`.

    streamlit run app/app.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

RAIZ = Path(__file__).resolve().parents[2]


def cargar_limpio(edicion: int = 2020) -> pd.DataFrame:
    """Misma limpieza que `listados/comun.py`, resumida."""
    jugadores = pd.read_csv(RAIZ / "datos-comunes" / "jugadores.csv", low_memory=False)
    jugadores = jugadores[jugadores["fifa"] == edicion].copy()
    for columna in ("value_eur", "wage_eur"):
        jugadores[columna] = jugadores[columna].replace(0, pd.NA).astype("Int64")
    jugadores["posicion"] = jugadores["player_positions"].str.split(",").str[0].str.strip()
    return jugadores


def cargar_posiciones() -> pd.DataFrame:
    return pd.read_csv(RAIZ / "datos-comunes" / "posiciones.csv")

st.set_page_config(page_title="Jugadores FIFA", layout="wide")
sns.set_theme(style="whitegrid")

ORDEN_LINEAS = ["Portería", "Defensa", "Centro del campo", "Ataque"]


@st.cache_data                     # se ejecuta una vez; después, memoria
def datos():
    return cargar_limpio(2020).merge(cargar_posiciones(), on="posicion", how="left")


jugadores = datos()

# --- Filtros, en la barra lateral ---------------------------------------
st.sidebar.header("Filtros")
lineas = st.sidebar.multiselect("Línea", ORDEN_LINEAS, default=ORDEN_LINEAS)
edad = st.sidebar.slider("Edad", 16, 45, (18, 33))
minimo = st.sidebar.slider("Valoración mínima", 40, 95, 65)

seleccion = jugadores[
    jugadores["linea"].isin(lineas)
    & jugadores["age"].between(*edad)
    & (jugadores["overall"] >= minimo)
]

# --- Indicadores ---------------------------------------------------------
st.title("Jugadores de FIFA 20")
a, b, c, d = st.columns(4)
a.metric("Jugadores", f"{len(seleccion):,}")
b.metric("Valoración media", f"{seleccion['overall'].mean():.1f}")
c.metric("Edad media", f"{seleccion['age'].mean():.1f}")
d.metric("Valor mediano", f"{seleccion['value_eur'].median():,.0f} €")

if seleccion.empty:
    st.warning("Ningún jugador cumple esos filtros. Prueba a relajarlos.")
    st.stop()

# --- Gráficos ------------------------------------------------------------
izquierda, derecha = st.columns(2)

with izquierda:
    st.subheader("Valoración por línea")
    figura, ejes = plt.subplots(figsize=(5, 3.2))
    sns.boxplot(data=seleccion, x="linea", y="overall", ax=ejes,
                color="#dbe8fb", order=[l for l in ORDEN_LINEAS if l in lineas])
    ejes.set_xlabel("")
    ejes.set_ylabel("Valoración media")
    ejes.tick_params(axis="x", rotation=20)
    st.pyplot(figura)

with derecha:
    st.subheader("Edad y valor de mercado")
    figura, ejes = plt.subplots(figsize=(5, 3.2))
    con_valor = seleccion.dropna(subset=["value_eur"])
    ejes.scatter(con_valor["age"], con_valor["value_eur"], s=6, alpha=0.2,
                 color="#2f6fd0")
    ejes.set_yscale("log")
    ejes.set_xlabel("Edad (años)")
    ejes.set_ylabel("Valor (€, escala log.)")
    st.pyplot(figura)

# --- Tabla y descarga ----------------------------------------------------
st.subheader("Los 20 más valorados de la selección")
tabla = (seleccion.sort_values("overall", ascending=False).head(20)
         [["short_name", "club", "nombre_es", "age", "overall", "potential", "value_eur"]]
         .rename(columns={"short_name": "Jugador", "club": "Club",
                          "nombre_es": "Puesto", "age": "Edad",
                          "overall": "Media", "potential": "Potencial",
                          "value_eur": "Valor (€)"}))
st.dataframe(tabla, width="stretch", hide_index=True)

st.download_button("Descargar la selección en CSV",
                   seleccion.to_csv(index=False).encode("utf-8"),
                   file_name="jugadores_filtrados.csv", mime="text/csv")
