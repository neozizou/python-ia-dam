"""Contar cuántos jugadores hay de cada país: el patrón más útil del curso.

Un diccionario que cuenta apariciones resuelve una cantidad enorme de
problemas. Aquí lo escribimos de tres formas, de la más manual a la que usarás
siempre, para que se vea qué hace cada una por debajo.
"""

from collections import Counter

PAISES = ["Argentina", "Portugal", "Brazil", "Slovenia", "Belgium", "Belgium",
          "Brazil", "Spain", "Belgium", "Spain", "Brazil", "Spain"]

# Forma 1: a mano. Hay que comprobar si la clave ya existe.
cuenta = {}
for pais in PAISES:
    if pais in cuenta:
        cuenta[pais] += 1
    else:
        cuenta[pais] = 1
print("A mano:       ", cuenta)

# Forma 2: `get` con valor por defecto. Una línea menos y sin el if.
cuenta = {}
for pais in PAISES:
    cuenta[pais] = cuenta.get(pais, 0) + 1
print("Con get:      ", cuenta)

# Forma 3: Counter, que ya viene hecho en la biblioteca estándar.
cuenta = Counter(PAISES)
print("Con Counter:  ", dict(cuenta))

# Counter además sabe ordenar por frecuencia, que es lo que casi siempre quieres.
print("\nLos tres países con más jugadores:")
for pais, total in cuenta.most_common(3):
    print(f"  {pais:<12} {total} jugadores")

# Ordenar un diccionario normal por su valor, sin Counter:
por_frecuencia = sorted(cuenta.items(), key=lambda par: par[1], reverse=True)
print("\nOrdenado a mano:", por_frecuencia[:3])
