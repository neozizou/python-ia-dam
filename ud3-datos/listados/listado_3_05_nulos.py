"""Listado 3.5. Valores ausentes."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"])

print(ventas.isna().sum())                       # nulos por columna
print((ventas.isna().mean() * 100).round(1))     # porcentaje

# Tres estrategias, según lo que signifique el nulo
sin_unidades = ventas.dropna(subset=["unidades"])          # 1. descartar la fila
print(len(ventas), "->", len(sin_unidades))

canal_relleno = ventas["canal"].fillna("desconocido")      # 2. valor de relleno
print(canal_relleno.value_counts())

mediana = ventas["unidades"].median()                      # 3. imputar
unidades_imputadas = ventas["unidades"].fillna(mediana)
print(f"mediana usada: {mediana}")
print(ventas["unidades"].isna().sum(), "->", unidades_imputadas.isna().sum())
