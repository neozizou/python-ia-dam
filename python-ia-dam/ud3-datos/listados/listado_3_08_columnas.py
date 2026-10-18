"""Columnas derivadas: el dato que no viene, pero se puede calcular.

Casi ningún análisis interesante sale de las columnas tal como vienen. Lo
habitual es construir las que responden a tu pregunta.
"""

import numpy as np

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)

# 1. Aritmética entre columnas: se aplica fila a fila, sin bucle.
sol["margen"] = sol["potential"] - sol["overall"]
sol["salario_anual"] = sol["wage_eur"] * 52

# 2. Clasificar por tramos: pd.cut reparte en intervalos.
import pandas as pd
sol["tramo_edad"] = pd.cut(sol["age"], bins=[15, 21, 25, 30, 50],
                           labels=["Promesa", "Joven", "Madurez", "Veterano"])

# 3. Una condición: np.where es el "si... entonces... si no".
sol["titular"] = np.where(sol["overall"] >= 70, "sí", "no")

# 4. Varias condiciones: np.select, en orden, con un valor por defecto.
sol["nivel"] = np.select(
    [sol["overall"] >= 85, sol["overall"] >= 75, sol["overall"] >= 65],
    ["Estrella", "Titular", "Rotación"],
    default="Reserva")

# 5. Texto: extraer una parte de una columna.
sol["inicial"] = sol["short_name"].str[0]

print(sol[["short_name", "age", "tramo_edad", "overall", "nivel", "margen"]]
      .head(6).to_string(index=False))

print("\nJugadores por tramo de edad:")
print(sol["tramo_edad"].value_counts().sort_index().to_string())

print("\nJugadores por nivel:")
print(sol["nivel"].value_counts().to_string())

print("\nMargen de mejora medio por tramo de edad:")
print(sol.groupby("tramo_edad", observed=True)["margen"].mean().round(1).to_string())
print("\nLos jóvenes tienen mucho margen y los veteranos ninguno. Era de esperar,")
print("y que salga así es la mejor señal de que la columna está bien construida.")
