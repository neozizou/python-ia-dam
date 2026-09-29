"""Listado 1.34. Leer un JSON y trabajar con él.

Ejecuta antes el listado 1.33 para generar datos/resumen.json.
"""

import json

with open("datos/resumen.json", encoding="utf-8") as f:
    resumen = json.load(f)                     # dict de Python

ciudad, total = max(resumen["total_por_ciudad"].items(), key=lambda par: par[1])
print(f"Ciudad con más ventas: {ciudad} ({total:.2f} €)")
