"""Listado 4.3. Inyección SQL: por qué se usan siempre parámetros."""

import sqlite3
from pathlib import Path

conexion = sqlite3.connect(Path("datos") / "ventas.db")

# Lo que escribiría un atacante en un formulario de búsqueda
entrada = "Granada' OR '1'='1"

# MAL: construir el SQL concatenando texto
sql_peligroso = f"SELECT COUNT(*) FROM venta WHERE ciudad = '{entrada}'"
print("SQL generado:", sql_peligroso)
print("Filas devueltas:", conexion.execute(sql_peligroso).fetchone()[0])   # ¡todas!

# BIEN: el valor viaja como parámetro y nunca se interpreta como SQL
seguro = conexion.execute(
    "SELECT COUNT(*) FROM venta WHERE ciudad = ?", (entrada,)
).fetchone()[0]
print("Filas devueltas con parámetro:", seguro)      # 0: no existe esa ciudad

conexion.close()
