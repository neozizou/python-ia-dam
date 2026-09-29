"""Listado 4.2. Consultar: cursores, parámetros y filas con nombre."""

import sqlite3
from pathlib import Path

RUTA_BD = Path("datos") / "ventas.db"

conexion = sqlite3.connect(RUTA_BD)
conexion.row_factory = sqlite3.Row          # filas accesibles por nombre de columna
cursor = conexion.cursor()

cursor.execute("SELECT COUNT(*) AS total, SUM(unidades * precio) AS importe FROM venta")
fila = cursor.fetchone()
print(f"{fila['total']} ventas, {fila['importe']:,.2f} €")

# Consulta con parámetros: el valor NUNCA se concatena en el texto SQL
ciudad = "Granada"
cursor.execute(
    """
    SELECT producto, COUNT(*) AS ventas, ROUND(SUM(unidades * precio), 2) AS importe
    FROM venta
    WHERE ciudad = ?
    GROUP BY producto
    ORDER BY importe DESC
    """,
    (ciudad,),
)
for fila in cursor.fetchall():
    print(f"{fila['producto']:<10} {fila['ventas']:>4} {fila['importe']:>12,.2f} €")

# Parámetros con nombre, más legibles cuando hay varios
cursor.execute(
    "SELECT COUNT(*) FROM venta WHERE canal = :canal AND unidades > :minimo",
    {"canal": "online", "minimo": 5},
)
print(cursor.fetchone()[0], "ventas online de más de 5 unidades")

conexion.close()
