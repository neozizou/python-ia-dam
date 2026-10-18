"""Listado 1.32. Escribir y leer un fichero de texto."""

from pathlib import Path

ruta = Path("datos/registro.txt")

with ruta.open("w", encoding="utf-8") as fichero:      # "w" crea o vacía
    fichero.write("inicio del repaso de fichas\n")     # el salto de línea es tuyo
    fichero.writelines(["ERROR: edición 2021 no encontrada\n", "fin del repaso\n"])

with ruta.open(encoding="utf-8") as fichero:           # por defecto, "r" de lectura
    for numero, linea in enumerate(fichero, start=1):
        if linea.startswith("ERROR"):
            print(f"Línea {numero}: {linea.rstrip()}")  # rstrip quita el \n final
