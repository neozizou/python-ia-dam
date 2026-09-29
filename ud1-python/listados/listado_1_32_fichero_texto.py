"""Listado 1.32. Escribir y leer un fichero de texto."""

from pathlib import Path

ruta = Path("datos") / "registro.txt"

with ruta.open("w", encoding="utf-8") as f:
    f.write("inicio del proceso\n")
    f.write("ERROR: fichero no encontrado\n")
    f.write("fin del proceso\n")

with ruta.open(encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):    # línea a línea
        if linea.startswith("ERROR"):
            print(f"Línea {numero}: {linea.rstrip()}")

# Línea 2: ERROR: fichero no encontrado
