"""Listado 5.2. Leer por trozos: procesar más datos de los que caben en memoria."""

import time
from pathlib import Path

import pandas as pd

RUTA = Path("datos") / "ventas_grandes.csv"

inicio = time.perf_counter()
acumulado = pd.Series(dtype="float64")
filas = 0

# chunksize devuelve un iterador: cada vuelta trae 200.000 filas y libera las anteriores
for trozo in pd.read_csv(RUTA, sep=";", decimal=",", chunksize=200_000,
                         usecols=["ciudad", "unidades", "precio"]):
    trozo["importe"] = trozo["unidades"] * trozo["precio"]
    parcial = trozo.groupby("ciudad")["importe"].sum()
    acumulado = acumulado.add(parcial, fill_value=0)     # agregación incremental
    filas += len(trozo)

print(f"{filas:,} filas procesadas en {time.perf_counter() - inicio:.2f} s")
print((acumulado / 1_000_000).round(2).sort_values(ascending=False).to_string(
    header=False, name=False))
print("(millones de euros por ciudad)")
