"""Listado 3.2. Cargar un CSV y mirarlo por primera vez."""

from pathlib import Path

import pandas as pd

ruta = Path("datos") / "ventas_2026.csv"

ventas = pd.read_csv(
    ruta,
    sep=";",                    # separador español
    decimal=",",                # coma decimal: 809,91 -> 809.91
    parse_dates=["fecha"],      # convierte la columna a fechas
    encoding="utf-8",
)

print(ventas.shape)             # (filas, columnas)
print(ventas.columns.tolist())
print(ventas.head(3))
print(ventas.dtypes)
