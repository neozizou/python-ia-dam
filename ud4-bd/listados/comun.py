"""Carga y limpieza de las ventas, reutilizada desde la UD3."""

from pathlib import Path

import pandas as pd

RUTA_CSV = Path("datos") / "ventas_2026.csv"


def cargar_ventas(ruta: Path = RUTA_CSV) -> pd.DataFrame:
    """Devuelve el DataFrame de ventas limpio y con la columna importe."""
    ventas = pd.read_csv(ruta, sep=";", decimal=",", parse_dates=["fecha"])
    ventas = ventas.drop_duplicates()
    ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
    ventas["canal"] = ventas["canal"].fillna("desconocido")
    ventas["unidades"] = ventas["unidades"].fillna(ventas["unidades"].median())
    ventas["unidades"] = ventas["unidades"].astype("int64")
    return ventas.assign(importe=lambda df: (df["unidades"] * df["precio"]).round(2))
