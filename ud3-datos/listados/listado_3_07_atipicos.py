"""Listado 3.7. Valores atípicos con el criterio del rango intercuartílico."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"]).drop_duplicates()
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")

print(ventas["unidades"].describe())

q1 = ventas["unidades"].quantile(0.25)
q3 = ventas["unidades"].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr

atipicos = ventas[ventas["unidades"] > limite_superior]
print(f"Q1={q1}  Q3={q3}  IQR={iqr}  límite={limite_superior}")
print(len(atipicos), "ventas atípicas")
print(atipicos[["id_venta", "ciudad", "producto", "unidades"]].head())

# Un atípico no siempre es un error: decide y documenta la decisión
ventas_filtradas = ventas[ventas["unidades"] <= limite_superior]
print(len(ventas), "->", len(ventas_filtradas))
