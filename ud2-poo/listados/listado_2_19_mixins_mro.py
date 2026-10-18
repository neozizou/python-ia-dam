"""Ampliación · Mixins y orden de resolución de métodos (MRO).

Un mixin añade una capacidad suelta a una clase, sin ser un antepasado «de
verdad». Java no los tiene: lo más parecido son los métodos `default` de una
interfaz.
"""

from decimal import Decimal

from tienda.modelo import Producto


class ExportableCsvMixin:
    """Añade la capacidad de exportarse a CSV a cualquier clase con `campos_csv`."""

    def a_csv(self) -> str:
        return ";".join(str(getattr(self, campo)) for campo in self.campos_csv)


class ProductoExportable(ExportableCsvMixin, Producto):
    campos_csv = ("codigo", "nombre", "precio", "stock")


teclado = ProductoExportable("T-100", "Teclado mecánico", Decimal("79.90"), 12)
print(teclado.a_csv())

# El MRO es el orden en que Python busca un método. Se lee de izquierda a derecha.
print("\nMRO de ProductoExportable:")
for clase in ProductoExportable.__mro__:
    print("  ", clase.__name__)
