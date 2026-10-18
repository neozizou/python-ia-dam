"""Listado 4.5. pandas y SQL: to_sql y read_sql."""

import sqlite3
from pathlib import Path

import pandas as pd

from comun import cargar_ventas

RUTA_BD = Path("datos") / "ventas.db"
ventas = cargar_ventas()
ciudades = pd.read_csv(Path("datos") / "ciudades.csv", sep=";")

with sqlite3.connect(RUTA_BD) as conexion:
    # Un DataFrame entero a una tabla, en una línea
    ciudades.to_sql("ciudad", conexion, if_exists="replace", index=False)

    # Y una consulta a un DataFrame, en otra
    resumen = pd.read_sql(
        """
        SELECT c.provincia,
               COUNT(*)                        AS ventas,
               ROUND(SUM(v.unidades * v.precio), 2) AS importe,
               c.poblacion_miles
        FROM venta v
        JOIN ciudad c ON v.ciudad = c.ciudad
        GROUP BY c.provincia, c.poblacion_miles
        ORDER BY importe DESC
        """,
        conexion,
    )

resumen["euros_por_habitante"] = (
    resumen["importe"] / (resumen["poblacion_miles"] * 1000)
).round(2)
print(resumen)
