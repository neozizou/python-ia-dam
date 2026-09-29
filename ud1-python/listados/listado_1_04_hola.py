"""Listado 1.4. hola.py: primer script."""

import sys

nombre = input("¿Cómo te llamas? ")
version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"Hola, {nombre}. Estás usando Python {version}.")

# True si se está ejecutando dentro de un entorno virtual
print("¿Entorno virtual?", sys.prefix != sys.base_prefix)
