"""Punto de entrada: python -m ventas"""

import logging
from pathlib import Path

from ventas import guardar_json, leer_ventas, total_por_ciudad


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    ventas = leer_ventas(Path("datos") / "ventas.csv")
    totales = total_por_ciudad(ventas)
    guardar_json({"total_por_ciudad": totales}, Path("datos") / "resumen.json")
    for ciudad, total in totales.items():
        print(f"{ciudad:<8} {total:>9.2f} €")


if __name__ == "__main__":
    main()
