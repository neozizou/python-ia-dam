"""Dónde se guardan los productos.

`ProductoRepository` dice **qué** se puede hacer con los productos guardados, no
**cómo** se guardan. Aquí hay dos implementaciones: en memoria y en fichero. En
el proyecto Java de Acceso a Datos las siguientes unidades añaden JDBC, JPA,
ObjectDB y MongoDB sin tocar el contrato.
"""

from pathlib import Path
from typing import Protocol, runtime_checkable

from tienda.formatos import FormatoProductos, ProductoDto
from tienda.modelo import Producto


class ErrorAccesoDatos(Exception):
    """Error al leer o guardar datos.

    Envuelve el error original para que las capas de arriba no dependan de dónde
    están los datos.
    """


@runtime_checkable
class ProductoRepository(Protocol):
    """Operaciones de almacenamiento de productos."""

    def guardar(self, producto: Producto) -> None:
        """Da de alta el producto, o lo reemplaza si su código ya existía."""
        ...

    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        """Devuelve el producto, o `None` si no existe."""
        ...

    def buscar_todos(self) -> list[Producto]:
        """Devuelve todos los productos guardados; nunca `None`."""
        ...

    def borrar(self, codigo: str) -> bool:
        """Elimina un producto. Devuelve `True` si existía."""
        ...

    def existe(self, codigo: str) -> bool:
        """Indica si hay un producto con ese código."""
        ...


class ProductoRepositoryMemoria:
    """Implementación en memoria: los datos se pierden al cerrar el programa."""

    def __init__(self) -> None:
        self._productos: dict[str, Producto] = {}

    def guardar(self, producto: Producto) -> None:
        self._productos[producto.codigo] = producto

    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        return self._productos.get(codigo)

    def buscar_todos(self) -> list[Producto]:
        return list(self._productos.values())

    def borrar(self, codigo: str) -> bool:
        return self._productos.pop(codigo, None) is not None

    def existe(self, codigo: str) -> bool:
        return codigo in self._productos


class ProductoRepositoryFichero:
    """Implementación en fichero.

    Al crearse lee el fichero entero y, tras cada cambio, lo reescribe de forma
    segura: primero un fichero temporal y después un único movimiento.
    """

    def __init__(self, ruta: Path, formato: FormatoProductos) -> None:
        self._ruta = ruta
        self._formato = formato
        self._datos: dict[str, ProductoDto] = {}
        self._cargar()

    def guardar(self, producto: Producto) -> None:
        self._datos[producto.codigo] = ProductoDto.desde(producto)
        self._escribir()

    def buscar_por_codigo(self, codigo: str) -> Producto | None:
        dto = self._datos.get(codigo)
        return dto.a_producto() if dto else None

    def buscar_todos(self) -> list[Producto]:
        return [dto.a_producto() for dto in self._datos.values()]

    def borrar(self, codigo: str) -> bool:
        if self._datos.pop(codigo, None) is None:
            return False
        self._escribir()
        return True

    def existe(self, codigo: str) -> bool:
        return codigo in self._datos

    def _cargar(self) -> None:
        if not self._ruta.exists():
            return                                  # primera ejecución: catálogo vacío
        try:
            for dto in self._formato.leer(self._ruta):
                dto.a_producto()                    # valida: lanza si los datos no son correctos
                self._datos[dto.codigo] = dto
        except (OSError, ValueError) as error:
            raise ErrorAccesoDatos(f"No se pudo cargar {self._ruta}") from error

    def _escribir(self) -> None:
        try:
            self._ruta.parent.mkdir(parents=True, exist_ok=True)
            temporal = self._ruta.with_name(self._ruta.name + ".tmp")
            try:
                self._formato.escribir(temporal, list(self._datos.values()))
                temporal.replace(self._ruta)        # un solo paso: o está entero o no está
            finally:
                temporal.unlink(missing_ok=True)    # solo queda si algo ha fallado
        except OSError as error:
            raise ErrorAccesoDatos(f"No se pudo guardar {self._ruta}") from error
