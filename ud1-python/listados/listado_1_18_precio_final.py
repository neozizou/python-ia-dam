"""Listado 1.18. Valores por defecto y parámetros solo por nombre."""


def precio_final(base: float, iva: float = 0.21, *, descuento: float = 0.0) -> float:
    """Aplica el descuento y después el IVA.

    Los parámetros que siguen a * solo se pueden pasar por nombre.
    """
    return round(base * (1 - descuento) * (1 + iva), 2)


print(precio_final(100))                   # 121.0
print(precio_final(100, 0.10))             # 110.0
print(precio_final(100, descuento=0.2))    # 96.8
print(precio_final(iva=0.04, base=50))     # 52.0  (por nombre, en cualquier orden)

# Descomenta la línea siguiente para ver el TypeError:
# precio_final(100, 0.21, 0.2)             # descuento debe ir por nombre
