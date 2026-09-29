"""Listado 1.38. Las tres formas de import."""

import statistics                      # 1. el módulo completo
print(statistics.mean([4.5, 7.0, 9.25]))

from pathlib import Path               # 2. un nombre concreto
ruta = Path("datos")
print(ruta.exists())

import datetime as dt                  # 3. con un alias
hoy = dt.date.today()
print(hoy)
