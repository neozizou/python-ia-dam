"""Listado 1.36. Lectura robusta de ventas.csv (mejora del listado 1.33)."""

import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


def leer_ventas(ruta: Path) -> list[dict]:
    """Devuelve las filas válidas del CSV de ventas con los tipos convertidos."""
    validas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        for num_linea, fila in enumerate(lector, start=2):   # la línea 1 es la cabecera
            try:
                fila["unidades"] = int(fila["unidades"])
                fila["precio"] = a_float(fila["precio"])
            except ValueError as e:
                logging.warning("Línea %d descartada: %s", num_linea, e)
                continue
            validas.append(fila)
    return validas


try:
    ventas = leer_ventas(Path("datos") / "ventas.csv")
except FileNotFoundError as e:
    logging.error("No se encuentra el fichero %s", e.filename)
else:
    logging.info("%d ventas válidas", len(ventas))
finally:
    logging.info("Proceso terminado")
