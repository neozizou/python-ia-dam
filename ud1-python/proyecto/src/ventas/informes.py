"""Cálculos y exportación de informes a partir de las ventas."""

import json
from pathlib import Path


def total_por_ciudad(ventas: list[dict]) -> dict[str, float]:
    """Importe total por ciudad, ordenado de mayor a menor."""
    totales = {}
    for v in ventas:
        totales[v["ciudad"]] = totales.get(v["ciudad"], 0) + v["unidades"] * v["precio"]
    ordenados = sorted(totales.items(), key=lambda par: par[1], reverse=True)
    return {ciudad: round(total, 2) for ciudad, total in ordenados}


def guardar_json(datos: dict, ruta: Path) -> None:
    """Guarda un diccionario en un fichero JSON legible."""
    with ruta.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
