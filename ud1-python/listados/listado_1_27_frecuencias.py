"""Listado 1.27. Frecuencia de palabras con dict y con Counter."""

from collections import Counter

texto = "el perro y el gato y el raton"

frecuencias = {}
for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(frecuencias)    # {'el': 3, 'perro': 1, 'y': 2, 'gato': 1, 'raton': 1}

# La versión de la biblioteca estándar
print(Counter(texto.split()).most_common(2))   # [('el', 3), ('y', 2)]
