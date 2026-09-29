"""Listado 3.6. Duplicados, texto y tipos."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"])

print(ventas.duplicated().sum(), "filas duplicadas")
ventas = ventas.drop_duplicates()
print(len(ventas), "filas tras eliminarlas")

print(sorted(ventas["ciudad"].unique())[:6])     # '  GRANADA ' y 'Granada' conviven

ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()   # métodos .str
print(sorted(ventas["ciudad"].unique()))

ventas["canal"] = ventas["canal"].fillna("desconocido")
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")   # cambiar de tipo
print(ventas.dtypes)

# Fechas: una vez convertidas, se consultan por partes
print(ventas["fecha"].dt.year.unique(), ventas["fecha"].dt.month.min())
