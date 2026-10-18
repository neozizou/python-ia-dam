"""Ampliación · Escribir un gestor de contexto propio.

Si una pareja de acciones va siempre junta —abrir y cerrar, empezar y confirmar—
se puede envolver en un `with` para no olvidarse nunca de la segunda.
"""

from contextlib import contextmanager
from decimal import Decimal

from tienda.modelo import Producto
from tienda.repositorio import ProductoRepository, ProductoRepositoryMemoria
from tienda.servicio import ProductoService


@contextmanager
def cambios(repositorio: ProductoRepository):
    """Deja el catálogo como estaba si algo falla dentro del bloque."""
    copia = [(p.codigo, p.nombre, p.precio, p.stock) for p in repositorio.buscar_todos()]
    try:
        yield repositorio                       # aquí se ejecuta el cuerpo del with
    except Exception as error:
        for codigo, nombre, precio, stock in copia:
            repositorio.guardar(Producto(codigo, nombre, precio, stock))
        print("  Deshecho:", error)
        raise
    finally:
        print("  Catálogo:", [(p.codigo, str(p.precio))
                              for p in repositorio.buscar_todos()])


repositorio = ProductoRepositoryMemoria()
servicio = ProductoService(repositorio)
servicio.alta(Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12))

print("Bloque que termina bien:")
with cambios(repositorio):
    servicio.cambiar_precio("T-100", Decimal("69.90"))

print("\nBloque que falla a mitad:")
try:
    with cambios(repositorio):
        servicio.cambiar_precio("T-100", Decimal("59.90"))
        servicio.buscar("NO-EXISTE")
except Exception:
    pass
