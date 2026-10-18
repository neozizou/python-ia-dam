"""Ampliación · Métodos especiales: que tus objetos se comporten como los del lenguaje.

Definir `__add__`, `__len__` o `__iter__` integra tu clase en la sintaxis de
Python. Es potente y conviene usarlo poco: solo cuando la operación significa de
verdad lo que el símbolo sugiere.
"""

from decimal import Decimal

from tienda.modelo import LineaPedido, Producto


class Pedido:
    """Una colección de líneas que se comporta como una secuencia."""

    def __init__(self, *lineas: LineaPedido) -> None:
        self._lineas = list(lineas)

    def __len__(self) -> int:
        return len(self._lineas)

    def __getitem__(self, indice: int) -> LineaPedido:
        return self._lineas[indice]

    def __iter__(self):
        return iter(self._lineas)

    def __add__(self, linea: LineaPedido) -> "Pedido":
        return Pedido(*self._lineas, linea)

    @property
    def total(self) -> Decimal:
        return sum((linea.importe for linea in self._lineas), start=Decimal("0"))

    def __repr__(self) -> str:
        return f"Pedido({len(self)} líneas, {self.total} €)"


teclado = Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12)
raton = Producto("R-200", "Ratón inalámbrico", Decimal("24.50"), 30)

pedido = Pedido(LineaPedido(teclado, 2, Decimal("79.90")))
pedido = pedido + LineaPedido(raton, 1, Decimal("24.50"))

print(pedido)
print("len(pedido)  ", len(pedido))
print("pedido[0]    ", pedido[0].producto.nombre)
print("¿Se puede recorrer con for?", [l.producto.codigo for l in pedido])
