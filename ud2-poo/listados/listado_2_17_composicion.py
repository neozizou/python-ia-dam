"""Listado 2.17. Composición: un objeto usa a otros en lugar de heredar de ellos."""

import csv
from pathlib import Path


class LectorCSV:
    def __init__(self, ruta: Path, delimitador: str = ";"):
        self.ruta = ruta
        self.delimitador = delimitador

    def leer(self) -> list[dict]:
        with self.ruta.open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f, delimiter=self.delimitador))


class Calculadora:
    @staticmethod
    def total_por_clave(filas: list[dict], clave: str, campo: str) -> dict[str, float]:
        totales: dict[str, float] = {}
        for fila in filas:
            if fila[campo]:
                totales[fila[clave]] = totales.get(fila[clave], 0) + float(fila[campo])
        return totales


class Informe:
    """No hereda de LectorCSV ni de Calculadora: los USA."""

    def __init__(self, lector: LectorCSV, calculadora: Calculadora):
        self.lector = lector
        self.calculadora = calculadora

    def unidades_por_ciudad(self) -> dict[str, float]:
        filas = self.lector.leer()
        return self.calculadora.total_por_clave(filas, "ciudad", "unidades")


informe = Informe(LectorCSV(Path("datos") / "ventas.csv"), Calculadora())
print(informe.unidades_por_ciudad())
