"""Listado 1.16. Una función bien escrita."""


def media(valores: list[float]) -> float:
    """Devuelve la media aritmética de una lista no vacía de números."""
    return sum(valores) / len(valores)


print(media([4.5, 7.0, 9.25, 6.0]))    # 6.6875
help(media)                            # muestra el docstring
