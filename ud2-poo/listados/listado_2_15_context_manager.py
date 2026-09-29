"""Listado 2.15. Gestores de contexto: with para tus propios objetos."""

import time
from contextlib import contextmanager


class Cronometro:
    """Mide el tiempo de un bloque with."""

    def __init__(self, etiqueta: str):
        self.etiqueta = etiqueta

    def __enter__(self) -> "Cronometro":
        self.inicio = time.perf_counter()
        return self                      # lo que recibe la variable tras «as»

    def __exit__(self, tipo_exc, valor_exc, traza) -> bool:
        self.segundos = time.perf_counter() - self.inicio
        print(f"{self.etiqueta}: {self.segundos:.4f} s")
        return False                     # False: si hubo excepción, se propaga


with Cronometro("suma de un millón de enteros"):
    total = sum(range(1_000_000))


@contextmanager                          # la versión corta, con un generador
def cronometro(etiqueta: str):
    inicio = time.perf_counter()
    try:
        yield                            # aquí se ejecuta el cuerpo del with
    finally:
        print(f"{etiqueta}: {time.perf_counter() - inicio:.4f} s")


with cronometro("ordenar una lista"):
    ordenada = sorted(range(100_000), reverse=True)
