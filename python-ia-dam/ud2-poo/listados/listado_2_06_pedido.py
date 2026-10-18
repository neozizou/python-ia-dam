"""Las piezas inmutables del modelo: dataclass y enumeración."""

from dataclasses import replace
from decimal import Decimal

from tienda.modelo import EstadoPedido, LineaPedido, Producto

monitor = Producto("M-300", "Monitor 27 pulgadas", Decimal("219.00"), 5)
linea = LineaPedido(monitor, cantidad=2, precio_unitario=Decimal("219.00"))

print("Importe de la línea:", linea.importe, "€")

# frozen=True: una vez creada, no se toca. Para cambiar algo, se hace una copia.
try:
    linea.cantidad = 3
except Exception as error:
    print("Modificar la línea ->", type(error).__name__, "-", error)

print("Copia con otra cantidad:", replace(linea, cantidad=3).importe, "€")

# La validación del constructor también vale para las dataclass.
try:
    LineaPedido(monitor, cantidad=0, precio_unitario=Decimal("219.00"))
except ValueError as error:
    print("Cantidad cero ->", error)

# La enumeración: un conjunto cerrado de valores, con comportamiento propio.
print("\nEstados:", [estado.name for estado in EstadoPedido])
for estado in (EstadoPedido.PENDIENTE, EstadoPedido.ENTREGADO):
    print(f"  {estado.name:<10} ¿final? {estado.es_final()}")
