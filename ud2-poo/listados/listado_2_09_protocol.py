"""Listado 2.9. typing.Protocol: contratos sin herencia."""

from typing import Protocol


class Leible(Protocol):
    """Cualquier objeto con este método encaja, herede o no de aquí."""

    def leer(self) -> list[dict]: ...


class LectorMemoria:                       # no hereda de Leible
    def leer(self) -> list[dict]:
        return [{"ciudad": "Granada", "importe": 2699.7}]


def cargar(origen: Leible) -> int:
    """El editor avisa si le pasas algo sin método leer()."""
    return len(origen.leer())


print(cargar(LectorMemoria()))             # 1
