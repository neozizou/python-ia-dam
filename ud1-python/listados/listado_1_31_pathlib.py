"""Listado 1.31. Operaciones básicas con Path."""

from pathlib import Path

ruta = Path("datos") / "ventas.csv"

print(ruta.name)        # 'ventas.csv'
print(ruta.stem)        # 'ventas'
print(ruta.suffix)      # '.csv'
print(ruta.parent)      # datos
print(ruta.exists())    # True si ejecutas desde la carpeta listados/

print(list(Path("datos").glob("*.csv")))    # todos los CSV de la carpeta
