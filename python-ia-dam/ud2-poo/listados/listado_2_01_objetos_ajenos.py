"""Leer la API de un objeto ajeno: qué es atributo y qué es método.

Todo lo que usarás en las unidades siguientes son objetos de otra gente. Lo
primero no es escribir clases, es saber leerlas.
"""

import pandas as pd

ventas = pd.DataFrame({
    "ciudad": ["Granada", "Sevilla", "Granada", "Málaga"],
    "unidades": [12, 7, 5, 9],
    "importe": [240.0, 133.0, 95.0, 171.0],
})

# Atributo: un dato que el objeto ya tiene. Sin paréntesis.
print("shape   ", ventas.shape)
print("columns ", list(ventas.columns))
print("dtypes  ", dict(ventas.dtypes.astype(str)))

# Método: algo que el objeto hace cuando se lo pides. Con paréntesis.
print("\nhead(2):")
print(ventas.head(2))

# El error te dice cuál es cuál.
try:
    ventas.shape()
except TypeError as error:
    print("\nventas.shape() ->", type(error).__name__, "-", error)

# Qué tiene dentro, sin salir del editor.
publicos = [nombre for nombre in dir(ventas) if not nombre.startswith("_")]
print(f"\nMiembros públicos de un DataFrame: {len(publicos)}")
print("Los cinco primeros:", publicos[:5])
