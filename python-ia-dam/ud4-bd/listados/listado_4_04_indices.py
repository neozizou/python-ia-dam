"""Listado 4.4. Índices: el mismo SELECT, antes y después."""

import sqlite3
import time
from pathlib import Path

conexion = sqlite3.connect(Path("datos") / "ventas.db")
consulta = "SELECT COUNT(*) FROM venta WHERE ciudad = ? AND producto = ?"

print("Plan SIN índice:")
for fila in conexion.execute("EXPLAIN QUERY PLAN " + consulta, ("Granada", "monitor")):
    print(" ", fila[-1])

inicio = time.perf_counter()
for _ in range(2000):
    conexion.execute(consulta, ("Granada", "monitor")).fetchone()
sin_indice = time.perf_counter() - inicio

conexion.execute("CREATE INDEX idx_ciudad_producto ON venta (ciudad, producto)")

print("Plan CON índice:")
for fila in conexion.execute("EXPLAIN QUERY PLAN " + consulta, ("Granada", "monitor")):
    print(" ", fila[-1])

inicio = time.perf_counter()
for _ in range(2000):
    conexion.execute(consulta, ("Granada", "monitor")).fetchone()
con_indice = time.perf_counter() - inicio

print(f"2000 consultas sin índice: {sin_indice:.3f} s")
print(f"2000 consultas con índice: {con_indice:.3f} s")
conexion.close()
