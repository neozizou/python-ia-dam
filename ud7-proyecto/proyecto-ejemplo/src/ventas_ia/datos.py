"""Carga y limpieza de los datos de ventas (UD3 y UD4)."""

import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

RUTA_POR_DEFECTO = Path("datos") / "ventas_ml.csv"


def cargar_limpio(ruta: Path = RUTA_POR_DEFECTO) -> pd.DataFrame:
    """Devuelve el DataFrame de ventas limpio y listo para modelar.

    Reúne en un solo sitio todas las decisiones de limpieza, para que la
    aplicación, los scripts y los notebooks trabajen exactamente con los
    mismos datos.
    """
    if not ruta.exists():
        raise FileNotFoundError(f"No se encuentra el fichero de datos: {ruta}")

    ventas = pd.read_csv(ruta, sep=";", decimal=",")
    antes = len(ventas)

    ventas = ventas.drop_duplicates()
    ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
    ventas["canal"] = ventas["canal"].fillna("desconocido")
    ventas = ventas.dropna(subset=["unidades", "precio"])
    ventas["unidades"] = ventas["unidades"].astype("int64")
    ventas["importe"] = (ventas["unidades"] * ventas["precio"]).round(2)

    logger.info("Datos cargados: %d filas (%d descartadas)", len(ventas), antes - len(ventas))
    return ventas
