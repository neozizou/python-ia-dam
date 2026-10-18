"""Ampliación · Herencia y polimorfismo: las formas de pago de la tienda.

Es la jerarquía del Listado 0.22 de Acceso a Datos, escrita en Python. La
herencia sirve cuando varias clases comparten de verdad un comportamiento: aquí,
todas las formas de pago tienen titular y todas calculan una comisión.
"""

from abc import ABC, abstractmethod
from decimal import ROUND_HALF_UP, Decimal


class MetodoPago(ABC):
    """Clase abstracta: no se pueden crear objetos de ella, solo de sus hijas."""

    def __init__(self, titular: str) -> None:
        self.titular = titular

    @abstractmethod
    def comision(self, importe: Decimal) -> Decimal:
        """Cada forma de pago calcula su propia comisión."""

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.titular})"


class Tarjeta(MetodoPago):

    def __init__(self, titular: str, ultimos_digitos: str) -> None:
        super().__init__(titular)                 # primero, la parte heredada
        self.ultimos_digitos = ultimos_digitos

    def comision(self, importe: Decimal) -> Decimal:
        return (importe * Decimal("0.015")).quantize(Decimal("0.01"), ROUND_HALF_UP)


class Bizum(MetodoPago):

    def comision(self, importe: Decimal) -> Decimal:
        return Decimal("0.00")


importe = Decimal("80.00")
for metodo in (Tarjeta("Ana", "4242"), Bizum("Luis")):
    print(f"{metodo}: {metodo.comision(importe)} €")

# ABC impide crear la clase abstracta o una hija que no implemente lo obligatorio.
try:
    MetodoPago("Nadie")
except TypeError as error:
    print("\nCrear MetodoPago ->", error)
