"""Listado 4.1. Crear una base de datos SQLite y cargar los datos."""

import sqlite3
from pathlib import Path

from comun import cargar_ventas

RUTA_BD = Path("datos") / "ventas.db"
RUTA_BD.unlink(missing_ok=True)          # empezamos de cero cada vez

ventas = cargar_ventas()

with sqlite3.connect(RUTA_BD) as conexion:     # el with confirma o deshace la transacción
    conexion.execute("""
        CREATE TABLE venta (
            id_venta  INTEGER PRIMARY KEY,
            fecha     TEXT    NOT NULL,
            ciudad    TEXT    NOT NULL,
            producto  TEXT    NOT NULL,
            canal     TEXT,
            unidades  INTEGER NOT NULL CHECK (unidades >= 0),
            precio    REAL    NOT NULL,
            cliente   TEXT
        )
    """)

    filas = [
        (
            int(f.id_venta), f.fecha.date().isoformat(), f.ciudad, f.producto,
            f.canal, int(f.unidades), float(f.precio), f.cliente,
        )
        for f in ventas.itertuples()
    ]
    conexion.executemany(
        "INSERT INTO venta VALUES (?, ?, ?, ?, ?, ?, ?, ?)", filas
    )

print(f"{RUTA_BD}: {len(filas)} filas insertadas "
      f"({RUTA_BD.stat().st_size / 1024:.0f} KB)")
