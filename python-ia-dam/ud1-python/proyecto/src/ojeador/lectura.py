"""Leer el fichero de jugadores y convertir los tipos."""

import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
POR_DEFECTO = RAIZ / "datos-comunes" / "jugadores.csv"

NUMERICAS = ("fifa", "age", "overall", "potential", "value_eur", "wage_eur")


def leer_edicion(edicion: int, ruta: Path = POR_DEFECTO) -> list[dict]:
    """Devuelve los jugadores de una edición, con los números ya convertidos.

    Las filas con algún número ilegible se descartan en silencio: para este
    paquete pequeño basta, pero en el hito 0 habrá que contarlas y registrarlas.
    """
    jugadores = []
    with ruta.open(encoding="utf-8", newline="") as fichero:
        for fila in csv.DictReader(fichero):
            try:
                convertida = {c: int(fila[c]) for c in NUMERICAS}
            except ValueError:
                continue
            if convertida["fifa"] != edicion:
                continue
            convertida.update({c: fila[c] for c in ("short_name", "nationality", "club")})
            jugadores.append(convertida)
    return jugadores
