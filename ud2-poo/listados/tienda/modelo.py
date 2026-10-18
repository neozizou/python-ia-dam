"""Clases del dominio de la tienda, con sus validaciones.

Es el mismo modelo que el paquete `modelo` del proyecto Java de Acceso a Datos
(UD0): `Producto`, `Categoria`, `LineaPedido` y `EstadoPedido`. Lo que cambia es
cómo se escribe cada cosa en Python.
"""

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class Producto:
    """Producto del catálogo.

    Dos productos son iguales si tienen el mismo código.
    """

    def __init__(self, codigo: str, nombre: str, precio: Decimal, stock: int = 0) -> None:
        if not codigo or not codigo.strip():
            raise ValueError("El código es obligatorio")
        if stock < 0:
            raise ValueError(f"Stock no válido: {stock}")
        self._codigo = codigo          # no cambia una vez creado
        self.nombre = nombre
        self.precio = precio           # pasa por el setter de la propiedad
        self._stock = stock

    @classmethod
    def desde_linea(cls, linea: str) -> "Producto":
        """Crea un producto a partir de «codigo;nombre;precio;stock»."""
        codigo, nombre, precio, stock = linea.split(";")
        return cls(codigo, nombre, Decimal(precio), int(stock))

    @property
    def codigo(self) -> str:
        """Identificador del producto. Solo lectura."""
        return self._codigo

    @property
    def precio(self) -> Decimal:
        return self._precio

    @precio.setter
    def precio(self, valor: Decimal) -> None:
        if valor is None or valor < 0:
            raise ValueError(f"Precio no válido: {valor}")
        self._precio = valor

    @property
    def stock(self) -> int:
        """Unidades disponibles. Solo lectura: se cambia con `reponer`."""
        return self._stock

    def reponer(self, unidades: int) -> None:
        """Suma unidades al stock."""
        if unidades <= 0:
            raise ValueError("Las unidades deben ser positivas")
        self._stock += unidades

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Producto):
            return NotImplemented
        return self._codigo == otro._codigo

    def __hash__(self) -> int:
        return hash(self._codigo)

    def __repr__(self) -> str:
        return (f"Producto[{self._codigo}, {self.nombre}, "
                f"{self._precio} €, stock {self._stock}]")


@dataclass(frozen=True)
class Categoria:
    """Categoría de productos. Inmutable."""

    id: int
    nombre: str


@dataclass(frozen=True)
class LineaPedido:
    """Una línea de un pedido: qué producto, cuántas unidades y a qué precio."""

    producto: Producto
    cantidad: int
    precio_unitario: Decimal

    def __post_init__(self) -> None:
        if self.cantidad <= 0:
            raise ValueError(f"Cantidad no válida: {self.cantidad}")

    @property
    def importe(self) -> Decimal:
        return self.precio_unitario * self.cantidad


class EstadoPedido(Enum):
    """Estados por los que pasa un pedido."""

    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"

    def es_final(self) -> bool:
        """Un pedido entregado o cancelado ya no puede cambiar de estado."""
        return self in (EstadoPedido.ENTREGADO, EstadoPedido.CANCELADO)
