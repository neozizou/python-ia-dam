"""Listado 1.18. Parámetros por defecto y parámetros solo por nombre."""


def coste_traspaso(valor: float, comision: float = 0.10, *,
                   descuento: float = 0.0) -> float:
    """Calcula lo que cuesta fichar a un jugador.

    Primero se aplica el descuento sobre el valor de mercado y después la
    comisión del agente. Los parámetros que siguen a `*` solo se pueden pasar
    por nombre, para que nadie escriba un 0.2 suelto sin decir qué significa.
    """
    return round(valor * (1 - descuento) * (1 + comision), 2)


print(coste_traspaso(95_500_000))                      # 105050000.0
print(coste_traspaso(95_500_000, 0.05))                # 100275000.0
print(coste_traspaso(95_500_000, descuento=0.2))       # 84040000.0

# Esto falla a propósito: descuento no se puede pasar por posición.
try:
    coste_traspaso(95_500_000, 0.10, 0.2)
except TypeError as error:
    print("\nPor posición ->", error)
