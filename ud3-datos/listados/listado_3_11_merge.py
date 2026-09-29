"""Listado 3.11. Combinar tablas: merge y concat."""

from pathlib import Path

import pandas as pd

from comun import cargar_ventas

ventas = cargar_ventas()
ciudades = pd.read_csv(Path("datos") / "ciudades.csv", sep=";")
print(ciudades.head(3))

# merge es el JOIN de SQL: how puede ser 'inner', 'left', 'right' u 'outer'
completo = ventas.merge(ciudades, on="ciudad", how="left")
print(completo[["ciudad", "provincia", "poblacion_miles", "importe"]].head(3))
print(completo["provincia"].isna().sum(), "filas sin provincia")

# Métrica que solo es posible tras unir las dos tablas
por_ciudad = completo.groupby(["ciudad", "poblacion_miles"])["importe"].sum().reset_index()
por_ciudad["euros_por_habitante"] = (
    por_ciudad["importe"] / (por_ciudad["poblacion_miles"] * 1000)
).round(2)
print(por_ciudad.sort_values("euros_por_habitante", ascending=False))

# concat apila DataFrames con las mismas columnas (UNION de SQL)
primer_trimestre = ventas[ventas["mes"] <= 3]
segundo_trimestre = ventas[ventas["mes"].between(4, 6)]
semestre = pd.concat([primer_trimestre, segundo_trimestre], ignore_index=True)
print(len(primer_trimestre), "+", len(segundo_trimestre), "=", len(semestre))
