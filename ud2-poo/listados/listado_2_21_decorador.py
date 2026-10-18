"""Ampliación · Decoradores: envolver una función sin tocarla.

Un decorador recibe una función y devuelve otra que la envuelve. Es lo que hacen
`@property`, `@classmethod` o `@dataclass`; también puedes escribirlos tú.
"""

import functools
import time
from decimal import Decimal

from tienda.modelo import Producto
from tienda.repositorio import ProductoRepositoryMemoria
from tienda.servicio import ProductoService


def medir(funcion):
    """Imprime cuánto tarda la función a la que envuelve."""

    @functools.wraps(funcion)             # conserva el nombre y el docstring originales
    def envoltura(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        print(f"  [{funcion.__name__} tardó {(time.perf_counter() - inicio) * 1000:.2f} ms]")
        return resultado

    return envoltura


@medir
def inventario_completo(servicio: ProductoService) -> Decimal:
    """Calcula el valor del inventario."""
    return servicio.valor_inventario()


servicio = ProductoService(ProductoRepositoryMemoria())
for i in range(2_000):
    servicio.alta(Producto(f"P-{i:04d}", f"Producto {i}", Decimal("19.90"), i % 10))

print("Valor:", inventario_completo(servicio), "€")
print("Nombre conservado por functools.wraps:", inventario_completo.__name__)
print("Docstring conservado:", inventario_completo.__doc__)
