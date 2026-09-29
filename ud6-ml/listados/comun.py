"""Carga del conjunto de datos de la UD6."""

from pathlib import Path

import pandas as pd

RUTA = Path("datos") / "ventas_ml.csv"


def cargar() -> pd.DataFrame:
    """Devuelve el DataFrame de ventas preparado para modelar."""
    return pd.read_csv(RUTA, sep=";", decimal=",")
