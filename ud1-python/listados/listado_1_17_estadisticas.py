"""Listado 1.17. Retorno múltiple y desempaquetado."""


def estadisticas(valores: list[float]) -> tuple[float, float, float]:
    """Devuelve el mínimo, el máximo y la media."""
    return min(valores), max(valores), sum(valores) / len(valores)


minimo, maximo, promedio = estadisticas([4.5, 7.0, 9.25, 6.0])
print(minimo, maximo, promedio)        # 4.5 9.25 6.6875
