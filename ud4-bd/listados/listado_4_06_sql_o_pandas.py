"""Listado 4.6. La misma pregunta, en SQL y en pandas."""

import sqlite3
from pathlib import Path

import pandas as pd

from comun import cargar_ventas

pregunta = "importe por canal en Granada, de mayor a menor"

# Opción A: que trabaje la base de datos y traiga solo el resultado
with sqlite3.connect(Path("datos") / "ventas.db") as conexion:
    en_sql = pd.read_sql(
        """
        SELECT canal, ROUND(SUM(unidades * precio), 2) AS importe
        FROM venta
        WHERE ciudad = ?
        GROUP BY canal
        ORDER BY importe DESC
        """,
        conexion,
        params=("Granada",),
    )

# Opción B: traerlo todo y agrupar en memoria con pandas
ventas = cargar_ventas()
en_pandas = (
    ventas[ventas["ciudad"] == "Granada"]
    .groupby("canal", as_index=False)["importe"]
    .sum()
    .round(2)
    .sort_values("importe", ascending=False)
)

print(pregunta)
print(en_sql)
print(en_pandas.reset_index(drop=True))
print("¿Mismo resultado?", en_sql["importe"].sum().round(2) == en_pandas["importe"].sum().round(2))
