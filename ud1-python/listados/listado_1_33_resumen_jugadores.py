"""Leer las 100.995 filas del fichero y resumirlas, solo con la biblioteca estándar.

Esto es, en pequeño, lo que hace el hito 0. Fíjate en tres cosas: el CSV se lee
fila a fila y no entero en memoria; todo lo que llega del fichero es **texto**,
aunque parezca un número; y los datos que faltan hay que decidir qué se hace
con ellos, no se arreglan solos.
"""

import csv
import time
from collections import Counter
from pathlib import Path

DATOS = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"
EDICION = 2020


def main() -> None:
    inicio = time.perf_counter()

    filas = 0
    medias: list[int] = []
    valores: list[int] = []
    sin_valor = 0
    por_pais: Counter[str] = Counter()
    por_pie: Counter[str] = Counter()

    with DATOS.open(encoding="utf-8", newline="") as fichero:
        for fila in csv.DictReader(fichero):
            # Todo llega como texto: hay que convertirlo antes de comparar.
            if int(fila["fifa"]) != EDICION:
                continue

            filas += 1
            medias.append(int(fila["overall"]))
            por_pais[fila["nationality"]] += 1
            por_pie[fila["preferred_foot"]] += 1

            valor = int(fila["value_eur"])
            if valor == 0:              # agentes libres: el cero es «no hay dato»
                sin_valor += 1
            else:
                valores.append(valor)

    segundos = time.perf_counter() - inicio

    print(f"FIFA {EDICION}: {filas:,} jugadores leídos en {segundos:.1f} s")
    print(f"Sin valor de mercado: {sin_valor} ({sin_valor / filas * 100:.1f} %)")

    print(f"\nMedia de la columna 'overall': {sum(medias) / len(medias):.1f}")
    print(f"Mejor: {max(medias)} · Peor: {min(medias)}")

    print(f"\nValor medio (sin contar los ceros): {sum(valores) / len(valores):,.0f} €")
    ordenados = sorted(valores)
    print(f"Valor mediano:                      {ordenados[len(ordenados) // 2]:,} €")

    print("\nCinco países con más jugadores:")
    for pais, total in por_pais.most_common(5):
        print(f"  {pais:<16} {total:>5}  {total / filas * 100:4.1f} %")

    print("\nPie bueno:")
    for pie, total in por_pie.most_common():
        print(f"  {pie:<8} {total:>5}  {total / filas * 100:4.1f} %")


if __name__ == "__main__":
    main()
