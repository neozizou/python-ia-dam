"""La clase Producto en uso: validar al crear, validar al cambiar.

Ejecútalo desde la carpeta `listados/`:  python listado_2_04_producto_en_uso.py
"""

from decimal import Decimal

from tienda.modelo import Producto

teclado = Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12)
print(teclado)

# `precio` se lee como un atributo, pero por debajo hay un método que valida.
teclado.precio = Decimal("69.90")
print("Rebajado:", teclado.precio, "€")

try:
    teclado.precio = Decimal("-5")
except ValueError as error:
    print("Precio negativo ->", error)

# `codigo` y `stock` son de solo lectura: no tienen setter.
try:
    teclado.codigo = "T-999"
except AttributeError as error:
    print("Cambiar el código ->", error)

teclado.reponer(8)
print("Stock tras reponer:", teclado.stock)

# El constructor no deja crear objetos incorrectos.
try:
    Producto("", "Sin código", Decimal("10.00"))
except ValueError as error:
    print("Código vacío ->", error)

# Constructor alternativo: lo que en Java sería un segundo constructor.
raton = Producto.desde_linea("R-200;Ratón inalámbrico;24.50;30")
print("Desde una línea de CSV:", raton)
