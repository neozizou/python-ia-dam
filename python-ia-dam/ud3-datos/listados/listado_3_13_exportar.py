"""Guardar el resultado: CSV para compartir, Parquet para trabajar.

Un análisis que hay que repetir desde cero cada vez no sirve. El resultado
limpio se guarda, y a partir de ahí todo lo demás parte de ahí.
"""

import time
from pathlib import Path

from comun import cargar_limpio

SALIDA = Path("datos/procesado")
SALIDA.mkdir(parents=True, exist_ok=True)

panel = cargar_limpio()
print(f"Datos limpios: {panel.shape}")

# CSV: lo entiende todo el mundo, pero no guarda los tipos.
csv = SALIDA / "jugadores_limpio.csv"
inicio = time.perf_counter()
panel.to_csv(csv, index=False)
t_csv = time.perf_counter() - inicio

# Parquet: binario, comprimido y con los tipos dentro.
parquet = SALIDA / "jugadores_limpio.parquet"
inicio = time.perf_counter()
panel.to_parquet(parquet, index=False)
t_parquet = time.perf_counter() - inicio

print(f"\n{'':12} {'tamaño':>10} {'escritura':>11}")
for nombre, ruta, segundos in (("CSV", csv, t_csv), ("Parquet", parquet, t_parquet)):
    print(f"{nombre:<12} {ruta.stat().st_size / 1024**2:>7.1f} MB {segundos * 1000:>8.0f} ms")

print(f"\nParquet ocupa {csv.stat().st_size / parquet.stat().st_size:.0f} veces menos.")

# Y la diferencia que de verdad importa: los tipos.
import pandas as pd
del_csv = pd.read_csv(csv)
del_parquet = pd.read_parquet(parquet)

print("\nTipo de value_eur al recuperarlo:")
print(f"  desde CSV:     {del_csv['value_eur'].dtype}")
print(f"  desde Parquet: {del_parquet['value_eur'].dtype}  <- el que habíamos puesto")

print("\nRegla práctica: Parquet para los pasos intermedios de tu análisis,")
print("CSV solo cuando alguien lo tenga que abrir con Excel.")
