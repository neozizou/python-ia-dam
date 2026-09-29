"""Listado 3.9. Agrupar y agregar: el equivalente a GROUP BY."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"]).drop_duplicates()
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")
ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
ventas["importe"] = (ventas["unidades"] * ventas["precio"]).round(2)

# Una agregación sobre una columna
print(ventas.groupby("ciudad")["importe"].sum().sort_values(ascending=False))

# Varias agregaciones con nombres propios
resumen = (
    ventas.groupby("ciudad")
    .agg(
        ventas=("id_venta", "count"),
        unidades=("unidades", "sum"),
        importe=("importe", "sum"),
        ticket_medio=("importe", "mean"),
    )
    .round(2)
    .sort_values("importe", ascending=False)
)
print(resumen)

# Agrupar por dos columnas
print(ventas.groupby(["ciudad", "canal"])["importe"].sum().head(8))
