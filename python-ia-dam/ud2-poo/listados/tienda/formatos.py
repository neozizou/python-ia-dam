"""Formatos de fichero para el catálogo de productos.

`FormatoProductos` describe la forma que tiene que tener un formato; `FormatoCsv`
y `FormatoJson` la cumplen sin heredar de nada. Es el mismo diseño que el paquete
`fichero` del proyecto Java de Acceso a Datos (UD1).
"""

import csv
import json
from dataclasses import asdict, dataclass
from decimal import Decimal
from pathlib import Path
from typing import Protocol, runtime_checkable

from tienda.modelo import Producto


@dataclass(frozen=True)
class ProductoDto:
    """Un producto tal como se guarda en un fichero: datos planos, sin comportamiento."""

    codigo: str
    nombre: str
    precio: str                       # texto, para no perder decimales al serializar
    stock: int

    @classmethod
    def desde(cls, producto: Producto) -> "ProductoDto":
        """Copia los datos de un producto del modelo."""
        return cls(producto.codigo, producto.nombre, str(producto.precio), producto.stock)

    def a_producto(self) -> Producto:
        """Crea un producto del modelo; su constructor valida los datos leídos."""
        return Producto(self.codigo, self.nombre, Decimal(self.precio), self.stock)


@runtime_checkable
class FormatoProductos(Protocol):
    """Un formato de fichero capaz de leer y escribir una lista de productos."""

    def leer(self, ruta: Path) -> list[ProductoDto]:
        """Lee todos los productos de un fichero, en el orden en que aparecen."""
        ...

    def escribir(self, ruta: Path, productos: list[ProductoDto]) -> None:
        """Escribe los productos en un fichero, reemplazando su contenido."""
        ...


class FormatoCsv:
    """Texto separado por punto y coma, con una línea de cabecera. Codificación UTF-8."""

    CAMPOS = ("codigo", "nombre", "precio", "stock")

    def leer(self, ruta: Path) -> list[ProductoDto]:
        with ruta.open(encoding="utf-8", newline="") as fichero:
            lector = csv.DictReader(fichero, delimiter=";")
            productos = []
            for numero, fila in enumerate(lector, start=2):
                try:
                    productos.append(ProductoDto(fila["codigo"], fila["nombre"],
                                                 fila["precio"], int(fila["stock"])))
                except (KeyError, TypeError, ValueError) as error:
                    raise ValueError(f"Línea {numero} de {ruta.name}: {error}") from error
            return productos

    def escribir(self, ruta: Path, productos: list[ProductoDto]) -> None:
        with ruta.open("w", encoding="utf-8", newline="") as fichero:
            escritor = csv.DictWriter(fichero, fieldnames=self.CAMPOS, delimiter=";")
            escritor.writeheader()
            escritor.writerows(asdict(dto) for dto in productos)


class FormatoJson:
    """Una lista JSON de objetos, con sangría para poder leerla a simple vista."""

    def leer(self, ruta: Path) -> list[ProductoDto]:
        texto = ruta.read_text(encoding="utf-8")
        if not texto.strip():
            return []
        try:
            return [ProductoDto(**objeto) for objeto in json.loads(texto)]
        except (json.JSONDecodeError, TypeError) as error:
            raise ValueError(f"JSON no válido en {ruta.name}: {error}") from error

    def escribir(self, ruta: Path, productos: list[ProductoDto]) -> None:
        datos = [asdict(dto) for dto in productos]
        ruta.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")
