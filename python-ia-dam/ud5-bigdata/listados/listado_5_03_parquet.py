"""Listado 5.3. CSV frente a Parquet."""

import time
from pathlib import Path

import pandas as pd

CSV = Path("datos") / "ventas_grandes.csv"
PARQUET = Path("datos") / "ventas_grandes.parquet"

ventas = pd.read_csv(CSV, sep=";", decimal=",", parse_dates=["fecha"])
ventas.to_parquet(PARQUET, compression="snappy")        # conserva los tipos

print(f"CSV:     {CSV.stat().st_size / 1024**2:6.1f} MB")
print(f"Parquet: {PARQUET.stat().st_size / 1024**2:6.1f} MB")

inicio = time.perf_counter()
pd.read_csv(CSV, sep=";", decimal=",", parse_dates=["fecha"])
t_csv = time.perf_counter() - inicio

inicio = time.perf_counter()
pd.read_parquet(PARQUET)
t_parquet = time.perf_counter() - inicio

# Parquet es columnar: leer dos columnas no obliga a leer las siete
inicio = time.perf_counter()
pd.read_parquet(PARQUET, columns=["ciudad", "precio"])
t_columnas = time.perf_counter() - inicio

print(f"Leer el CSV completo:        {t_csv:.2f} s")
print(f"Leer el Parquet completo:    {t_parquet:.2f} s")
print(f"Leer 2 columnas del Parquet: {t_columnas:.2f} s")
