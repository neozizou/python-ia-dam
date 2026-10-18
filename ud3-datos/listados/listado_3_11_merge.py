"""Unir tablas: traer datos de otro sitio.

Dos situaciones muy distintas con la misma orden. En la primera, una tabla
pequeña de búsqueda añade información a cada fila. En la segunda, dos tablas
grandes se cruzan y hay que decidir qué pasa con las filas que no casan.
"""

import pandas as pd

from comun import JUGADORES, cargar_limpio, cargar_posiciones

sol = cargar_limpio(edicion=2020)

# ---------------------------------------------------------------- 1. Búsqueda
posiciones = cargar_posiciones()
print("La tabla de búsqueda, 15 filas:")
print(posiciones.head(4).to_string(index=False))

# merge por la columna común: cada jugador recibe su línea del campo.
con_linea = sol.merge(posiciones, on="posicion", how="left")
print(f"\nAntes del merge: {sol.shape} · después: {con_linea.shape}")
print("  Mismas filas, tres columnas más. Eso es lo que debe pasar.")

print("\nJugadores y valor mediano por línea:")
print(con_linea.groupby("linea").agg(
    jugadores=("sofifa_id", "size"),
    media=("overall", "mean"),
    valor_mediano=("value_eur", "median"),
).round(1).to_string())

# Comprobación obligatoria: ¿se ha quedado alguien sin pareja?
print("\nSin línea asignada:", int(con_linea["linea"].isna().sum()))

# ------------------------------------------------------- 2. Entre dos tablas
RUTA = JUGADORES
columnas = ["sofifa_id", "short_name", "overall", "club"]
anterior = pd.read_csv(RUTA, usecols=["fifa"] + columnas, low_memory=False)
anterior = anterior[anterior["fifa"] == 2019][columnas]
actual = sol[columnas]

print(f"\nFIFA 19: {len(anterior):,} jugadores · FIFA 20: {len(actual):,}")

# inner: solo los que están en las dos.
cruce = anterior.merge(actual, on="sofifa_id", how="inner",
                       suffixes=("_19", "_20"))
print(f"inner -> {len(cruce):,} jugadores están en las dos ediciones")

# left: todos los de FIFA 19; los que no siguen, con huecos.
izquierda = anterior.merge(actual, on="sofifa_id", how="left",
                           suffixes=("_19", "_20"))
desaparecidos = izquierda["overall_20"].isna().sum()
print(f"left  -> {len(izquierda):,} filas, de las que {desaparecidos:,} "
      f"no aparecen en FIFA 20")

# Y ahora el análisis que solo es posible tras cruzar.
cruce["cambio"] = cruce["overall_20"] - cruce["overall_19"]
print(f"\nMejoran {int((cruce['cambio'] > 0).sum()):,} · "
      f"igual {int((cruce['cambio'] == 0).sum()):,} · "
      f"empeoran {int((cruce['cambio'] < 0).sum()):,}")
print(f"Cambian de club: {int((cruce['club_19'] != cruce['club_20']).sum()):,}")

print("\nLos cinco que más suben de un año a otro:")
print(cruce.nlargest(5, "cambio")[
    ["short_name_19", "overall_19", "overall_20", "cambio"]].to_string(index=False))
