"""Un contrato, dos implementaciones: el código de arriba no cambia.

`inventario` no sabe dónde están los datos. Le vale cualquier objeto que tenga
los métodos de ProductoRepository, haya heredado de algo o no.
"""

from decimal import Decimal
from pathlib import Path

from tienda.formatos import FormatoCsv
from tienda.modelo import Producto
from tienda.repositorio import (ProductoRepository, ProductoRepositoryFichero,
                                ProductoRepositoryMemoria)
from tienda.servicio import ProductoService

RUTA = Path("datos/catalogo_demo.csv")


def inventario(repositorio: ProductoRepository) -> str:
    """Resume el catálogo. Solo usa el contrato, nunca una clase concreta."""
    servicio = ProductoService(repositorio)
    productos = servicio.listar()
    nombres = ", ".join(p.nombre for p in productos)
    return f"{len(productos)} productos ({nombres}) por {servicio.valor_inventario()} €"


def llenar(repositorio: ProductoRepository) -> ProductoRepository:
    servicio = ProductoService(repositorio)
    servicio.alta(Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12))
    servicio.alta(Producto("R-200", "Ratón inalámbrico", Decimal("24.50"), 30))
    return repositorio


RUTA.unlink(missing_ok=True)

print("En memoria:", inventario(llenar(ProductoRepositoryMemoria())))
print("En fichero:", inventario(llenar(ProductoRepositoryFichero(RUTA, FormatoCsv()))))

print("\nContenido de", RUTA)
print(RUTA.read_text(encoding="utf-8").strip())

# Ninguna de las dos clases hereda de ProductoRepository...
print("\n¿Memoria hereda del contrato?",
      ProductoRepository in ProductoRepositoryMemoria.__mro__)
# ...pero lo cumple, porque tiene los métodos que el contrato pide.
print("¿Memoria lo cumple?", isinstance(ProductoRepositoryMemoria(), ProductoRepository))
print("¿Y una lista?      ", isinstance([], ProductoRepository))
