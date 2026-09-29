"""Listado 2.14. Iteradores y generadores: procesar sin cargarlo todo en memoria."""

import csv
from pathlib import Path
from typing import Iterator


def filas_csv(ruta: Path) -> Iterator[dict]:
    """Devuelve las filas de una en una; no carga el fichero entero."""
    with ruta.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            yield fila          # yield: entrega un valor y espera al siguiente next()


ruta = Path("datos") / "ventas.csv"

generador = filas_csv(ruta)
print(type(generador))                    # <class 'generator'>
print(next(generador)["ciudad"])          # Granada: solo se ha leído una línea

for fila in filas_csv(ruta):              # el for consume el resto normalmente
    print(fila["producto"], end=" ")
print()

# Expresión generadora: como una comprensión, pero perezosa
unidades = (f["unidades"] for f in filas_csv(ruta) if f["unidades"])
print(sum(int(u) for u in unidades))      # 19
