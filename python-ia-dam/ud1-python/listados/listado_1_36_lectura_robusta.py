"""Leer un fichero real sin que un dato raro tire el programa.

Un programa que se cae en la fila 40.000 de 100.995 es inútil: pierdes el
trabajo anterior y no sabes qué pasó. La estrategia es otra: intentar procesar
cada fila, apartar las que no se pueden, seguir adelante y contar al final qué
se quedó fuera y por qué.

Ese recuento no es burocracia. Es lo que te avisa cuando el error no está en
los datos, sino en tu código.
"""

import csv
from collections import Counter
from pathlib import Path

DATOS = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"


def anio_ingenuo(texto: str) -> int:
    """Primer intento: convertir el año de contrato a entero."""
    if texto == "":
        raise ValueError("viene vacío")
    return int(texto)


def anio_correcto(texto: str) -> int:
    """Segundo intento, sabiendo que el CSV escribe los años como '2021.0'."""
    if texto == "":
        raise ValueError("viene vacío")
    return int(float(texto))        # primero a decimal, luego se trunca


def recorrer(convertir) -> tuple[int, Counter[str], list[int]]:
    """Aplica `convertir` a cada fila y devuelve qué ha salido y qué ha fallado."""
    procesadas, descartadas, anios = 0, Counter(), []
    with DATOS.open(encoding="utf-8", newline="") as fichero:
        for fila in csv.DictReader(fichero):
            try:
                anios.append(convertir(fila["contract_valid_until"]))
                procesadas += 1
            except ValueError as error:
                descartadas[str(error)[:34]] += 1
    return procesadas, descartadas, anios


for nombre, funcion in (("ingenuo", anio_ingenuo), ("correcto", anio_correcto)):
    procesadas, descartadas, anios = recorrer(funcion)
    total = procesadas + sum(descartadas.values())
    print(f"--- Intento {nombre} ---")
    print(f"  Procesadas: {procesadas:>7,} de {total:,} ({procesadas / total * 100:.1f} %)")
    for motivo, veces in descartadas.most_common(2):
        print(f"  Descartadas: {veces:>6,}  {motivo}")
    if procesadas:
        print(f"  Contratos entre {min(anios)} y {max(anios)}")
    else:
        print("  No ha sobrevivido ninguna fila: el fallo es del código, no de los datos.")
    print()
