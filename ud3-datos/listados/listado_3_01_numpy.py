"""Listado 3.1. NumPy: vectorización frente a bucles."""

import time

import numpy as np

# Un array es homogéneo y de tamaño fijo, como un vector de C++ pero con operaciones
precios = np.array([899.90, 180.00, 25.00, 12.50])
unidades = np.array([3, 2, 10, 5])

importes = precios * unidades          # operación elemento a elemento, sin bucle
print(importes)                        # [2699.7  360.    250.     62.5]
print(importes.sum(), importes.mean(), importes.max())
print(importes[importes > 300])        # máscara booleana: filtra sin bucle

# Por qué importa: mismo cálculo sobre 5 millones de valores
n = 5_000_000
lista = list(range(n))
array = np.arange(n)

inicio = time.perf_counter()
total_python = sum(x * 2 for x in lista)
t_python = time.perf_counter() - inicio

inicio = time.perf_counter()
total_numpy = (array * 2).sum()
t_numpy = time.perf_counter() - inicio

print(f"Python puro: {t_python:.3f} s")
print(f"NumPy:       {t_numpy:.3f} s  ({t_python / t_numpy:.0f} veces más rápido)")

# Valores ausentes: NaN («not a number») se propaga
con_nulos = np.array([1.0, np.nan, 3.0])
print(con_nulos.sum(), np.nansum(con_nulos))    # nan 4.0
