"""Lectura y conversión de los datos de ventas."""

import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


def leer_ventas(ruta: Path) -> list[dict]:
    """Devuelve las filas válidas del CSV de ventas con los tipos convertidos."""
    validas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        for num_linea, fila in enumerate(lector, start=2):
            try:
                fila["unidades"] = int(fila["unidades"])
                fila["precio"] = a_float(fila["precio"])
            except ValueError as e:
                logger.warning("Línea %d descartada: %s", num_linea, e)
                continue
            validas.append(fila)
    return validas
