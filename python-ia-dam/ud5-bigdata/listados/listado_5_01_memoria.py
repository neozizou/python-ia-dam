"""Listado 5.1. Cuánta memoria ocupa un millón de filas, y cómo reducirla."""

import time
from pathlib import Path

import pandas as pd

RUTA = Path("datos") / "ventas_grandes.csv"

inicio = time.perf_counter()
ventas = pd.read_csv(RUTA, sep=";", decimal=",", parse_dates=["fecha"])
print(f"Lectura: {time.perf_counter() - inicio:.2f} s")
print(f"Filas: {len(ventas):,}")
print(f"Memoria: {ventas.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
print(ventas.dtypes)

# Los tipos por defecto son generosos. Ajustarlos ahorra mucha memoria:
#   category  -> para columnas de texto con pocos valores distintos
#   int32 / float32 -> cuando el rango y la precisión lo permiten
tipos = {
    "id_venta": "int32",
    "ciudad": "category",
    "producto": "category",
    "canal": "category",
    "unidades": "int8",
    "precio": "float32",
}

inicio = time.perf_counter()
ligeras = pd.read_csv(RUTA, sep=";", decimal=",", parse_dates=["fecha"], dtype=tipos)
print(f"\nLectura con tipos ajustados: {time.perf_counter() - inicio:.2f} s")
print(f"Memoria: {ligeras.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
print(ligeras.dtypes)
