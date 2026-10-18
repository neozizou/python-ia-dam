"""Listado 1.17. Retorno múltiple y desempaquetado."""


def estadisticas(valores: list[float]) -> tuple[float, float, float]:
    """Devuelve el mínimo, el máximo y la media."""
    return min(valores), max(valores), sum(valores) / len(valores)


peor, mejor, promedio = estadisticas([94, 93, 91, 91, 89])
print(peor, mejor, promedio)       # 89 94 91.6

# Lo que devuelve es una tupla; desempaquetarla es opcional.
resultado = estadisticas([94, 93, 91])
print(resultado)                   # (91, 94, 92.66666666666667)
print(f"Media: {resultado[2]:.2f}")
