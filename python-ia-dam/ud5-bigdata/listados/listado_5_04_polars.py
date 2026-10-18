"""Listado 5.4. Polars: evaluación perezosa sobre el mismo fichero."""

import time
from pathlib import Path

import pandas as pd
import polars as pl

CSV = Path("datos") / "ventas_grandes.csv"

# pandas: lee todo y después agrupa
inicio = time.perf_counter()
ventas = pd.read_csv(CSV, sep=";", decimal=",")
resultado_pandas = (
    ventas.assign(importe=ventas["unidades"] * ventas["precio"])
    .groupby("ciudad")["importe"].sum().sort_values(ascending=False)
)
t_pandas = time.perf_counter() - inicio

# Polars: describe el plan y lo ejecuta optimizado al llamar a collect()
inicio = time.perf_counter()
consulta = (
    pl.scan_csv(CSV, separator=";", decimal_comma=True)      # scan_ = perezoso
    .with_columns((pl.col("unidades") * pl.col("precio")).alias("importe"))
    .group_by("ciudad")
    .agg(pl.col("importe").sum())
    .sort("importe", descending=True)
)
resultado_polars = consulta.collect()
t_polars = time.perf_counter() - inicio

print(resultado_polars)
print(f"pandas: {t_pandas:.2f} s")
print(f"polars: {t_polars:.2f} s")
print("\nPlan de ejecución optimizado por Polars:")
print(consulta.explain())
