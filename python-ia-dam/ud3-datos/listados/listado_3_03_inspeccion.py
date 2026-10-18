"""Las seis órdenes con las que se empieza SIEMPRE un conjunto de datos nuevo.

Antes de calcular nada, hay que saber qué hay dentro. Estas seis respuestas
—tamaño, tipos, huecos, estadísticos, valores únicos y una muestra— evitan la
mayoría de los errores de análisis, porque casi todos vienen de suponer algo
sobre los datos que no era cierto.
"""

from pathlib import Path

import pandas as pd

pd.set_option("display.width", 100)

RUTA = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"
jugadores = pd.read_csv(RUTA, low_memory=False)
sol = jugadores[jugadores["fifa"] == 2020]

# 1. ¿Cuánto hay?
print("1. shape:", sol.shape)

# 2. ¿De qué tipo es cada columna, y cuántos huecos tiene?
print("\n2. info() de seis columnas:")
sol[["short_name", "age", "club", "overall", "value_eur", "pace"]].info()

# 3. ¿Cómo se reparten los números?
print("\n3. describe() de las numéricas:")
print(sol[["age", "overall", "potential", "value_eur"]].describe().round(1).to_string())

# 4. ¿Y los textos? describe() también sirve, pero dice otras cosas.
print("\n4. describe() de las categóricas:")
print(sol[["nationality", "club", "preferred_foot"]].describe().to_string())

# 5. ¿Qué valores distintos hay en una columna, y cuántos de cada uno?
print("\n5. value_counts() del pie bueno:")
print(sol["preferred_foot"].value_counts().to_string())
print("\n   ...y en proporción:")
print(sol["preferred_foot"].value_counts(normalize=True).mul(100).round(1).to_string())

# 6. Una muestra al azar dice más que las primeras filas, que suelen estar ordenadas.
print("\n6. sample(3):")
print(sol.sample(3, random_state=7)[["short_name", "club", "overall"]].to_string(index=False))
