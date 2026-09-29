"""Listado 3.10. Tablas dinámicas y tablas de contingencia."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"]).drop_duplicates()
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")
ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
ventas["canal"] = ventas["canal"].fillna("desconocido")
ventas["importe"] = (ventas["unidades"] * ventas["precio"]).round(2)

tabla = pd.pivot_table(
    ventas,
    index="ciudad",
    columns="canal",
    values="importe",
    aggfunc="sum",
    fill_value=0,
).round(0)
print(tabla)

# Recuento cruzado de dos variables categóricas
print(pd.crosstab(ventas["producto"], ventas["canal"]))
