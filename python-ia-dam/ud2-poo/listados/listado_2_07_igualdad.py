"""Igualdad e identidad: `==`, `is`, `__eq__` y `__hash__`.

Dos productos con el mismo código son el mismo producto, aunque sean dos objetos
distintos en memoria.
"""

from decimal import Decimal

from tienda.modelo import Categoria, Producto

uno = Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12)
otro = Producto("T-100", "Teclado mecánico retroiluminado", Decimal("89.90"), 3)
mismo = uno

print("uno == otro ", uno == otro)     # True: comparamos por código
print("uno is otro ", uno is otro)     # False: son dos objetos distintos
print("uno is mismo", uno is mismo)    # True: la misma etiqueta sobre el mismo objeto

# Como __hash__ acompaña a __eq__, el producto sirve de clave y entra en un set.
catalogo = {uno, otro}
print("\nProductos distintos en el conjunto:", len(catalogo))

existencias = {uno: 12}
print("Existencias consultadas con otro objeto:", existencias[otro])

# Las dataclass escriben __eq__ y __repr__ por ti, comparando todos los campos.
print("\nCategoria(1, 'Periféricos') == Categoria(1, 'Periféricos'):",
      Categoria(1, "Periféricos") == Categoria(1, "Periféricos"))
print(Categoria(1, "Periféricos"))
