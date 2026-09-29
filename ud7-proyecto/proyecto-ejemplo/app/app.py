"""Aplicación del proyecto integrador: panel de análisis y predictor.

    streamlit run app/app.py
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# La aplicación vive en app/ y el paquete en src/: así lo encuentra también
# Streamlit Community Cloud, donde no se ejecuta "pip install -e .".
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "src"))

from ventas_ia import cargar_limpio, cargar_modelo  # noqa: E402

st.set_page_config(page_title="Ventas IA", page_icon="📈", layout="wide")


@st.cache_data                      # datos: se copian y se cachean por valor
def datos() -> pd.DataFrame:
    return cargar_limpio(RAIZ / "datos" / "ventas_ml.csv")


@st.cache_resource                  # modelo: objeto vivo, una sola copia
def modelo_y_metricas():
    return cargar_modelo(RAIZ / "modelos" / "modelo.joblib")


ventas = datos()

try:
    modelo, ficha = modelo_y_metricas()
except FileNotFoundError:
    modelo, ficha = None, None

st.title("📈 Ventas: análisis y predicción")

panel, predictor, acerca_de = st.tabs(["Panel", "Predicción", "Sobre el modelo"])

with panel:
    ciudades = st.multiselect("Ciudades", sorted(ventas["ciudad"].unique()),
                              default=sorted(ventas["ciudad"].unique()))
    filtradas = ventas[ventas["ciudad"].isin(ciudades)]

    if filtradas.empty:
        st.warning("Ningún dato cumple los filtros.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Facturación", f"{filtradas['importe'].sum():,.0f} €")
        col2.metric("Ventas", f"{len(filtradas):,}")
        col3.metric("Unidades por venta", f"{filtradas['unidades'].mean():.1f}")

        izquierda, derecha = st.columns(2)
        izquierda.subheader("Importe por producto")
        izquierda.bar_chart(filtradas.groupby("producto")["importe"].sum())
        derecha.subheader("Unidades por mes")
        derecha.line_chart(filtradas.groupby("mes")["unidades"].mean())

with predictor:
    if modelo is None:
        st.error("No hay modelo entrenado. Ejecuta `python scripts/entrenar.py`.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            producto = st.selectbox("Producto", sorted(ventas["producto"].unique()))
            canal = st.selectbox("Canal", sorted(ventas["canal"].unique()))
            ciudad = st.selectbox("Ciudad", sorted(ventas["ciudad"].unique()))
        with col2:
            mes = st.slider("Mes", 1, 12, 6)
            descuento = st.select_slider("Descuento", [0.0, 0.05, 0.10, 0.20],
                                         format_func=lambda v: f"{v:.0%}")
            precio = st.number_input("Precio unitario (€)", min_value=1.0,
                                     value=float(ventas["precio"].median()), step=5.0)

        caso = pd.DataFrame([{"mes": mes, "descuento": descuento, "precio": precio,
                              "ciudad": ciudad, "producto": producto, "canal": canal}])
        prediccion = modelo.predict(caso)[0]
        margen = ficha["mae"]

        st.metric("Unidades estimadas", f"{prediccion:.1f}",
                  help=f"Intervalo orientativo: {max(prediccion - margen, 0):.1f} – "
                       f"{prediccion + margen:.1f}")
        st.caption(f"Error medio del modelo en datos no vistos: ±{margen} unidades")

        maximo = ventas["precio"].max()
        if precio > maximo:
            st.warning(f"El precio introducido ({precio:.2f} €) supera el máximo visto "
                       f"al entrenar ({maximo:.2f} €): la predicción es poco fiable.")

with acerca_de:
    if ficha is None:
        st.info("Entrena el modelo para ver su ficha.")
    else:
        st.subheader("Ficha del modelo")
        st.json(ficha)
        st.markdown(
            "- **Qué predice**: unidades de una venta a partir de producto, canal, "
            "ciudad, mes, descuento y precio.\n"
            "- **Dónde falla**: el error es mayor en productos baratos (ratón y "
            "teclado), donde las cantidades varían mucho más.\n"
            "- **Límites de uso**: no sirve para productos, canales o precios fuera "
            "del rango de los datos de entrenamiento, ni para explicar causas."
        )
