"""Listado 6.17. El modelo, dentro de una aplicación.

Ejecuta antes listado_6_16_guardar_modelo.py para generar el fichero del modelo.

    streamlit run ud6-ml/app/app.py
"""

import json
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

MODELO = Path(__file__).parent.parent / "listados" / "modelos" / "modelo_unidades.joblib"
METRICAS = MODELO.parent / "metricas.json"

st.set_page_config(page_title="Predicción de unidades", page_icon="🔮")
st.title("🔮 ¿Cuántas unidades venderemos?")

if not MODELO.exists():
    st.error("No encuentro el modelo. Ejecuta primero el listado 6.16.")
    st.stop()


@st.cache_resource            # cache_resource, no cache_data: el modelo es un objeto vivo
def cargar_modelo(ruta: Path):
    """Carga el pipeline entrenado una sola vez."""
    return joblib.load(ruta)


modelo = cargar_modelo(MODELO)
metricas = json.loads(METRICAS.read_text(encoding="utf-8"))

col1, col2 = st.columns(2)
with col1:
    producto = st.selectbox("Producto", ["portátil", "monitor", "teclado", "ratón",
                                         "tablet", "impresora"])
    canal = st.selectbox("Canal", ["tienda", "online", "teléfono"])
    ciudad = st.selectbox("Ciudad", ["Granada", "Málaga", "Sevilla", "Córdoba",
                                     "Almería", "Jaén", "Cádiz", "Huelva"])
with col2:
    mes = st.slider("Mes", 1, 12, 6)
    descuento = st.select_slider("Descuento", options=[0.0, 0.05, 0.10, 0.20],
                                 format_func=lambda v: f"{v:.0%}")
    precio = st.number_input("Precio unitario (€)", min_value=1.0, value=180.0, step=5.0)

caso = pd.DataFrame([{
    "mes": mes, "descuento": descuento, "precio": precio,
    "ciudad": ciudad, "producto": producto, "canal": canal,
}])

prediccion = modelo.predict(caso)[0]

st.metric("Unidades estimadas", f"{prediccion:.1f}")
st.caption(
    f"Error medio del modelo en datos no vistos (MAE): ±{metricas['mae']} unidades · "
    f"R² = {metricas['r2']} · scikit-learn {metricas['version_sklearn']}"
)
st.info("Una predicción sin su margen de error no es información: es una cifra suelta.")
