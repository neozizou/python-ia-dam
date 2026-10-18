"""Listado 5.5. DuckDB: SQL directamente sobre los ficheros."""

import time
from pathlib import Path

import duckdb

PARQUET = Path("datos") / "ventas_grandes.parquet"
CSV = Path("datos") / "ventas_grandes.csv"

# No hay que cargar nada: la consulta lee el fichero y devuelve un DataFrame
inicio = time.perf_counter()
resumen = duckdb.sql(f"""
    SELECT ciudad,
           COUNT(*)                        AS ventas,
           ROUND(SUM(unidades * precio), 2) AS importe
    FROM '{PARQUET}'
    GROUP BY ciudad
    ORDER BY importe DESC
""").df()
print(resumen)
print(f"Consulta sobre Parquet: {time.perf_counter() - inicio:.2f} s")

# También lee CSV, y acepta comodines: 'datos/*.parquet' une todos los ficheros
inicio = time.perf_counter()
duckdb.sql(f"""
    SELECT producto, ROUND(AVG(precio), 2) AS precio_medio
    FROM read_csv('{CSV}', delim=';', decimal_separator=',')
    GROUP BY producto
""").show()
print(f"Consulta sobre CSV: {time.perf_counter() - inicio:.2f} s")
