"""Listado 2.6. Duck typing: importa lo que sabe hacer, no de qué clase es."""


class LectorCSV:
    def leer(self) -> list[dict]:
        return [{"ciudad": "Granada", "importe": 2699.7}]


class LectorJSON:
    def leer(self) -> list[dict]:
        return [{"ciudad": "Málaga", "importe": 845.0}]


class ApiSimulada:                 # no hereda de nada, pero sirve igual
    def leer(self) -> list[dict]:
        return [{"ciudad": "Sevilla", "importe": 899.9}]


def cargar(origen) -> list[dict]:
    """Funciona con cualquier objeto que tenga un método leer()."""
    return origen.leer()


for origen in (LectorCSV(), LectorJSON(), ApiSimulada()):
    print(cargar(origen))
