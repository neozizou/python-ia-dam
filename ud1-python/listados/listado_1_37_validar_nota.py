"""Listado 1.37. Validar con raise."""


def validar_nota(nota: float) -> float:
    """Devuelve la nota si está entre 0 y 10; si no, lanza ValueError."""
    if not 0 <= nota <= 10:
        raise ValueError(f"Nota fuera de rango: {nota}")
    return nota


print(validar_nota(7.5))
try:
    validar_nota(11)
except ValueError as e:
    print("Error:", e)      # Error: Nota fuera de rango: 11
