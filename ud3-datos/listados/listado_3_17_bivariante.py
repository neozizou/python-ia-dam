"""Análisis bivariante: cómo se relacionan dos columnas.

Tres combinaciones posibles: número con número (correlación), número con
categoría (comparar grupos) y categoría con categoría (tabla de contingencia).
"""

from comun import cargar_limpio, cargar_posiciones

sol = cargar_limpio(edicion=2020).merge(cargar_posiciones(), on="posicion", how="left")

# ------------------------------------------------- Número frente a número
print("=== Correlaciones con la valoración ===")
numericas = ["age", "overall", "potential", "value_eur", "wage_eur",
             "height_cm", "weight_kg", "pace", "shooting", "passing"]
correlaciones = sol[numericas].corr(numeric_only=True)["overall"].sort_values(
    ascending=False)
print(correlaciones.round(2).to_string())

print("\n  Entre 0,7 y 1 la relación es fuerte; cerca de 0, no hay relación")
print("  lineal (que no es lo mismo que no haya ninguna relación).")
print(f"\n  Altura y valoración: {sol[['height_cm', 'overall']].corr().iloc[0, 1]:.2f}."
      " Ser alto no te hace mejor jugador.")

# Y una correlación global puede esconder dos comportamientos distintos.
print("\n  Altura y valoración, separando por puesto:")
for nombre, grupo in (("todos", sol),
                      ("porteros", sol[sol["es_portero"]]),
                      ("de campo", sol[~sol["es_portero"]])):
    r = grupo[["height_cm", "overall"]].corr().iloc[0, 1]
    print(f"    {nombre:<10} {r:+.2f}   ({len(grupo):,} jugadores)")
print("\n  En los porteros la altura sí cuenta algo; en el conjunto se diluye.")
print("  Calcular una correlación sobre grupos que no se parecen es la forma")
print("  más fácil de no ver lo que está pasando.")

# ---------------------------------------------- Número frente a categoría
print("\n=== Salario por línea del campo ===")
print(sol.groupby("linea")["wage_eur"].describe()[
    ["count", "mean", "50%", "max"]].round(0).to_string())

# ------------------------------------------- Categoría frente a categoría
import pandas as pd
print("\n=== Pie bueno por línea (en porcentaje de cada línea) ===")
tabla = pd.crosstab(sol["linea"], sol["preferred_foot"], normalize="index")
print((tabla * 100).round(1).to_string())
print("\n  Los zurdos son el 23,6 % del total, pero no se reparten igual por")
print("  líneas. Ahí hay una pregunta interesante para el análisis.")
