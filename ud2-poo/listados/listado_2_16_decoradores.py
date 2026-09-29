"""Listado 2.16. Decoradores: envolver una función sin tocar su código."""

import functools
import time


def medir(func):
    """Decorador que muestra cuánto tarda la función."""

    @functools.wraps(func)               # conserva nombre y docstring del original
    def envoltorio(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.perf_counter() - inicio:.4f} s")
        return resultado

    return envoltorio


@medir                                   # equivale a: suma_cuadrados = medir(suma_cuadrados)
def suma_cuadrados(n: int) -> int:
    """Suma los cuadrados de los n primeros enteros."""
    return sum(i * i for i in range(n))


print(suma_cuadrados(100_000))
print(suma_cuadrados.__name__, "-", suma_cuadrados.__doc__)
