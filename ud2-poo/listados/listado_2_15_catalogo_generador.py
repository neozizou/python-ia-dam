"""Recorrer un catálogo grande sin cargarlo entero en memoria.

`cargar_lista` devuelve todos los productos de golpe; `recorrer` los entrega de
uno en uno. El resultado es el mismo; la memoria que hace falta, no.
"""

import csv
import gc
import tracemalloc
from collections.abc import Callable, Iterator
from decimal import Decimal
from pathlib import Path

from tienda.modelo import Producto

RUTA = Path("datos/catalogo_grande.csv")


def generar_fichero(filas: int = 200_000) -> None:
    """Crea un CSV de ejemplo si todavía no existe."""
    if RUTA.exists():
        return
    RUTA.parent.mkdir(parents=True, exist_ok=True)
    with RUTA.open("w", encoding="utf-8", newline="") as fichero:
        escritor = csv.writer(fichero, delimiter=";")
        escritor.writerow(["codigo", "nombre", "precio", "stock"])
        for i in range(filas):
            escritor.writerow([f"P-{i:06d}", f"Producto {i}", f"{10 + i % 90}.50", i % 25])


def cargar_lista(ruta: Path) -> list[Producto]:
    """Lee el fichero entero y devuelve una lista con todos los productos."""
    with ruta.open(encoding="utf-8", newline="") as fichero:
        return [Producto(f["codigo"], f["nombre"], Decimal(f["precio"]), int(f["stock"]))
                for f in csv.DictReader(fichero, delimiter=";")]


def recorrer(ruta: Path) -> Iterator[Producto]:
    """Entrega los productos de uno en uno, según se van leyendo."""
    with ruta.open(encoding="utf-8", newline="") as fichero:
        for f in csv.DictReader(fichero, delimiter=";"):
            yield Producto(f["codigo"], f["nombre"], Decimal(f["precio"]), int(f["stock"]))


def medir(tarea: Callable[[], Decimal]) -> tuple[Decimal, float]:
    """Ejecuta la tarea y devuelve su resultado y la memoria máxima, en MB."""
    gc.collect()
    tracemalloc.start()
    resultado = tarea()
    maximo = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return resultado, maximo / 1024 / 1024


generar_fichero()

print("cargar_lista devuelve:", type(cargar_lista(RUTA)).__name__)
print("recorrer devuelve:    ", type(recorrer(RUTA)).__name__, "(todavía no ha leído nada)")

total_lista, memoria_lista = medir(
    lambda: sum(p.precio * p.stock for p in cargar_lista(RUTA)))
total_flujo, memoria_flujo = medir(
    lambda: sum(p.precio * p.stock for p in recorrer(RUTA)))

print(f"\nValor del inventario con la lista:     {total_lista} € "
      f"({memoria_lista:5.1f} MB de memoria)")
print(f"Valor del inventario con el generador: {total_flujo} € "
      f"({memoria_flujo:5.1f} MB de memoria)")

# Un generador se agota: sirve para una sola pasada.
flujo = recorrer(RUTA)
print("\nPrimer producto: ", next(flujo))
print("Segundo producto:", next(flujo))
