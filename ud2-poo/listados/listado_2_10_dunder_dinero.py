"""Listado 2.10. Métodos especiales: que tus objetos se comporten como los nativos."""

from functools import total_ordering


@total_ordering                      # genera <=, >, >= a partir de __eq__ y __lt__
class Importe:
    def __init__(self, euros: float):
        self.euros = round(euros, 2)

    def __repr__(self) -> str:       # para el programador (depuración)
        return f"Importe({self.euros})"

    def __str__(self) -> str:        # para el usuario (print)
        return f"{self.euros:.2f} €"

    def __eq__(self, otro) -> bool:
        return isinstance(otro, Importe) and self.euros == otro.euros

    def __lt__(self, otro) -> bool:
        return self.euros < otro.euros

    def __add__(self, otro) -> "Importe":
        return Importe(self.euros + otro.euros)


a = Importe(899.90)
b = Importe(180.00)

print(a + b)                 # 1079.90 €
print(a > b, a == Importe(899.9))     # True True
print(sorted([a, b]))        # [Importe(180.0), Importe(899.9)]
print(repr(a))               # Importe(899.9)
