"""Listado 1.33. resumen_ventas.py: de CSV a JSON."""

import csv
import json
from pathlib import Path

CARPETA_DATOS = Path("datos")
entrada = CARPETA_DATOS / "ventas.csv"
salida = CARPETA_DATOS / "resumen.json"


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


total_por_ciudad = {}
descartadas = 0

with entrada.open(encoding="utf-8", newline="") as f:
    lector = csv.DictReader(f, delimiter=";")
    for fila in lector:                      # cada fila es un dict
        if not fila["unidades"]:             # campo vacío: no se puede calcular
            descartadas += 1
            continue
        importe = int(fila["unidades"]) * a_float(fila["precio"])
        ciudad = fila["ciudad"]
        total_por_ciudad[ciudad] = total_por_ciudad.get(ciudad, 0) + importe

resumen = {
    "fichero": entrada.name,
    "filas_descartadas": descartadas,
    "total_por_ciudad": {c: round(t, 2) for c, t in total_por_ciudad.items()},
}

with salida.open("w", encoding="utf-8") as f:
    json.dump(resumen, f, ensure_ascii=False, indent=2)
