"""Listado 3.19. La aplicación Streamlit más pequeña posible.

Se ejecuta con:  streamlit run listado_3_19_streamlit_minimo.py
"""

import streamlit as st

from comun import cargar_ventas

st.title("Ventas 2026")

ventas = cargar_ventas()

st.metric("Facturación total", f"{ventas['importe'].sum():,.0f} €")
st.dataframe(ventas.head(20))
st.bar_chart(ventas.groupby("ciudad")["importe"].sum())
