"""Listado 3.3. Series, DataFrame y primera inspección."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"])

# Una columna es una Series; varias, un DataFrame
print(type(ventas["precio"]), type(ventas[["ciudad", "precio"]]))

print(ventas.info())                      # tipos, nulos y memoria
print(ventas.describe())                  # estadísticos de las columnas numéricas
print(ventas["producto"].value_counts())  # recuento por categoría
print(ventas["ciudad"].nunique(), "ciudades distintas")
print(ventas["ciudad"].unique()[:10])
