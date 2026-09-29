"""Genera datos/ventas_grandes.csv, el fichero de trabajo de la UD5.

Un millón de filas ocupan unos 60 MB, así que el fichero NO se sube al
repositorio: cada uno lo genera en su portátil.

    python generar_datos_grandes.py            # 1.000.000 de filas
    python generar_datos_grandes.py 5000000    # cinco millones
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

FILAS = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
DESTINO = Path("datos") / "ventas_grandes.csv"
DESTINO.parent.mkdir(exist_ok=True)

generador = np.random.default_rng(2026)
ciudades = ["Granada", "Málaga", "Sevilla", "Córdoba", "Almería", "Jaén", "Cádiz", "Huelva"]
productos = ["portátil", "monitor", "teclado", "ratón", "tablet", "impresora"]
canales = ["tienda", "online", "teléfono"]
precios = np.array([899.90, 180.00, 25.00, 12.50, 349.00, 149.90])

indice_producto = generador.integers(0, len(productos), FILAS)

datos = pd.DataFrame({
    "id_venta": np.arange(FILAS, dtype="int64"),
    "fecha": pd.to_datetime("2026-01-01") + pd.to_timedelta(
        generador.integers(0, 365, FILAS), unit="D"
    ),
    "ciudad": np.take(ciudades, generador.integers(0, len(ciudades), FILAS)),
    "producto": np.take(productos, indice_producto),
    "canal": np.take(canales, generador.integers(0, len(canales), FILAS)),
    "unidades": generador.integers(1, 13, FILAS),
    "precio": np.round(precios[indice_producto] * generador.choice([0.9, 1.0, 1.1], FILAS), 2),
})

datos.to_csv(DESTINO, index=False, sep=";", decimal=",", date_format="%Y-%m-%d")
print(f"{DESTINO}: {FILAS:,} filas, {DESTINO.stat().st_size / 1024**2:.1f} MB")
