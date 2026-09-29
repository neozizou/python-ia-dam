"""Función de carga y limpieza compartida por los listados 3.11 en adelante.

Reúne lo aprendido en los apartados 3.2 a 3.8.
"""

from pathlib import Path

import pandas as pd

RUTA = Path("datos") / "ventas_2026.csv"


def cargar_ventas(ruta: Path = RUTA) -> pd.DataFrame:
    """Lee el CSV de ventas y devuelve un DataFrame limpio y con columnas derivadas."""
    ventas = pd.read_csv(ruta, sep=";", decimal=",", parse_dates=["fecha"])
    ventas = ventas.drop_duplicates()
    ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
    ventas["canal"] = ventas["canal"].fillna("desconocido")
    ventas["unidades"] = ventas["unidades"].fillna(ventas["unidades"].median())
    ventas["unidades"] = ventas["unidades"].astype("int64")
    return ventas.assign(
        importe=lambda df: (df["unidades"] * df["precio"]).round(2),
        mes=lambda df: df["fecha"].dt.month,
    )
