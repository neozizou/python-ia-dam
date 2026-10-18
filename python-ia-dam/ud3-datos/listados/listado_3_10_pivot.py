"""Tablas dinámicas: el mismo `groupby`, pero en rejilla.

`pivot_table` coloca un grupo en las filas y otro en las columnas. Es más
legible que un `groupby` de dos niveles cuando quieres comparar.
"""

import pandas as pd

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)

# Filas: línea del campo. Columnas: tramo de edad. Celdas: media de valoración.
sol["tramo"] = pd.cut(sol["age"], [15, 21, 25, 30, 50],
                      labels=["Promesa", "Joven", "Madurez", "Veterano"])

tabla = sol.pivot_table(values="overall", index="posicion", columns="tramo",
                        aggfunc="mean", observed=True).round(1)
print("Valoración media por posición y edad:")
print(tabla.head(8).to_string())

# Para contar con totales, `crosstab` es más directo que `pivot_table`:
# está hecho justo para eso y no necesita columna de valores.
print("\nCuántos jugadores hay en cada casilla, con totales:")
print(pd.crosstab(sol["es_portero"], sol["tramo"],
                  margins=True, margins_name="Total").to_string())

# Una rejilla puede tener casillas vacías: combinaciones que no existen.
print("\nValor mediano por posición y esfuerzo en defensa (en miles de €):")
rejilla = sol.pivot_table(values="value_eur", index="posicion",
                          columns="esfuerzo_defensa", aggfunc="median")
print((rejilla / 1000).round(0).head(6).to_string())
print("\nLos huecos no son ceros: son combinaciones sin ningún jugador.")
print("Si los rellenas con 0, estarás diciendo que esos jugadores no valen nada.")

print("\nUn pivot_table no es un resultado nuevo: es un groupby colocado")
print("en rejilla para que se pueda leer de un vistazo.")
