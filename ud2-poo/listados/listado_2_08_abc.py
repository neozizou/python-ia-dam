"""Listado 2.8. Clases abstractas: el contrato de un lector de datos."""

import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path


class Lector(ABC):
    """Contrato común: todo lector sabe leer y devolver filas."""

    def __init__(self, ruta: Path):
        self.ruta = ruta

    @abstractmethod
    def leer(self) -> list[dict]:
        """Devuelve las filas del fichero como lista de diccionarios."""

    def resumen(self) -> str:                 # método concreto heredado por todos
        return f"{self.ruta.name}: {len(self.leer())} filas"


class LectorCSV(Lector):
    def __init__(self, ruta: Path, delimitador: str = ";"):
        super().__init__(ruta)
        self.delimitador = delimitador

    def leer(self) -> list[dict]:
        with self.ruta.open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f, delimiter=self.delimitador))


class LectorJSON(Lector):
    def leer(self) -> list[dict]:
        with self.ruta.open(encoding="utf-8") as f:
            return json.load(f)


try:
    Lector(Path("datos/ventas.csv"))          # no se puede instanciar
except TypeError as e:
    print("TypeError:", e)

lector = LectorCSV(Path("datos/ventas.csv"))
print(lector.resumen())                       # ventas.csv: 5 filas
