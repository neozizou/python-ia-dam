"""Listado 3.8. Columnas derivadas: assign, operaciones vectorizadas y apply."""

from pathlib import Path

import numpy as np
import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"]).drop_duplicates()
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")

ventas = ventas.assign(
    importe=lambda df: (df["unidades"] * df["precio"]).round(2),
    mes=lambda df: df["fecha"].dt.month,
    trimestre=lambda df: df["fecha"].dt.quarter,
)

# Clasificar sin bucles: np.where para dos casos, pd.cut para intervalos
ventas["tamaño"] = np.where(ventas["importe"] > 1000, "grande", "normal")
ventas["rango_precio"] = pd.cut(
    ventas["precio"],
    bins=[0, 50, 200, 1000],
    labels=["bajo", "medio", "alto"],
)

print(ventas[["producto", "unidades", "precio", "importe", "tamaño", "rango_precio"]].head())
print(ventas["tamaño"].value_counts())
print(ventas["rango_precio"].value_counts())
