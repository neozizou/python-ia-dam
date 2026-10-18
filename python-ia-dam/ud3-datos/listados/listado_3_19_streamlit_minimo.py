"""Streamlit en veinte líneas: de un script a una página web.

Streamlit convierte un script de Python en una aplicación web sin escribir
HTML. La idea clave es que **el script entero se vuelve a ejecutar de arriba
abajo cada vez que alguien toca un control**. No hay eventos ni callbacks: se
reejecuta todo y se vuelve a pintar.

    streamlit run listado_3_19_streamlit_minimo.py
"""

import streamlit as st

from comun import cargar_limpio

st.title("Explorador de jugadores")

jugadores = cargar_limpio(edicion=2020)

# Un control devuelve directamente su valor. No hay que registrar nada.
minimo = st.slider("Valoración mínima", 40, 95, 80)

# Y a partir de aquí, Python normal.
seleccion = jugadores[jugadores["overall"] >= minimo]

st.write(f"Hay **{len(seleccion):,}** jugadores con valoración {minimo} o más.")
st.dataframe(seleccion[["short_name", "club", "age", "overall", "value_eur"]]
             .sort_values("overall", ascending=False).head(20))

st.caption("Mueve el control y fíjate en que el script se ejecuta otra vez entero.")
