"""Reglas de negocio de la tienda.

`ProductoService` recibe un repositorio y trabaja con él: no sabe ni le importa
si los datos están en memoria o en un fichero. Eso es composición.
"""

from decimal import Decimal

from tienda.modelo import Producto
from tienda.repositorio import ProductoRepository


class ProductoNoEncontradoError(Exception):
    """Se lanza cuando se pide un producto que no existe."""

    def __init__(self, codigo: str) -> None:
        super().__init__(f"No existe ningún producto con código {codigo}")


class ProductoService:
    """Qué se puede hacer con los productos, y qué no."""

    def __init__(self, repositorio: ProductoRepository) -> None:
        self._repositorio = repositorio

    def alta(self, producto: Producto) -> None:
        """Da de alta un producto nuevo."""
        if self._repositorio.existe(producto.codigo):
            raise ValueError(f"Ya existe un producto con código {producto.codigo}")
        self._repositorio.guardar(producto)

    def listar(self) -> list[Producto]:
        """Devuelve los productos ordenados por nombre."""
        return sorted(self._repositorio.buscar_todos(), key=lambda p: p.nombre)

    def buscar(self, codigo: str) -> Producto:
        """Devuelve un producto o lanza `ProductoNoEncontradoError`."""
        producto = self._repositorio.buscar_por_codigo(codigo)
        if producto is None:
            raise ProductoNoEncontradoError(codigo)
        return producto

    def cambiar_precio(self, codigo: str, nuevo_precio: Decimal) -> None:
        producto = self.buscar(codigo)
        producto.precio = nuevo_precio
        self._repositorio.guardar(producto)   # en memoria sobra; con un fichero es imprescindible

    def baja(self, codigo: str) -> None:
        if not self._repositorio.borrar(codigo):
            raise ProductoNoEncontradoError(codigo)

    def valor_inventario(self) -> Decimal:
        """Suma de precio × stock de todos los productos."""
        return sum((p.precio * p.stock for p in self._repositorio.buscar_todos()),
                   start=Decimal("0"))
