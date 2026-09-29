"""Listado 1.19. Número variable de argumentos: *args y **kwargs."""


def resumen(*valores, **opciones):
    """valores llega como tupla; opciones, como diccionario."""
    decimales = opciones.get("decimales", 2)
    total = sum(valores)
    return f"{len(valores)} valores, total {total:.{decimales}f}"


print(resumen(1.5, 2.25, 3))                # 3 valores, total 6.75
print(resumen(1.5, 2.25, 3, decimales=0))   # 3 valores, total 7
