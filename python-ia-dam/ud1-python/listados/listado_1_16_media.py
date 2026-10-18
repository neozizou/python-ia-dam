"""Listado 1.16. Una función bien escrita."""


def media(valores: list[float]) -> float:
    """Devuelve la media aritmética de una lista no vacía de números."""
    return sum(valores) / len(valores)


print(media([94, 93, 91, 91]))     # 92.25
help(media)                        # muestra el docstring
