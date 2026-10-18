"""Análisis univariante: entender una columna cada vez.

Antes de cruzar variables hay que conocerlas de una en una. Para una columna
numérica se mira centro, dispersión y forma; para una categórica, cuántas
categorías hay y cómo de repartidas están.
"""

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)

# ------------------------------------------------------------- Una numérica
print("=== overall ===")
descripcion = sol["overall"].describe()
print(descripcion.round(1).to_string())

print(f"\nCentro:      media {sol['overall'].mean():.1f} · "
      f"mediana {sol['overall'].median():.0f}")
print(f"Dispersión:  desviación típica {sol['overall'].std():.1f} · "
      f"rango {sol['overall'].min()}–{sol['overall'].max()}")
print(f"Forma:       asimetría {sol['overall'].skew():.2f}")
print("  Media y mediana casi iguales y asimetría cerca de cero:")
print("  es una distribución simétrica, parecida a una campana.")

print("\n=== value_eur ===")
valor = sol["value_eur"].dropna()
print(f"Centro:      media {valor.mean():,.0f} € · mediana {valor.median():,.0f} €")
print(f"Forma:       asimetría {valor.skew():.2f}")
print("  Aquí la media casi triplica a la mediana y la asimetría es enorme:")
print("  distribución con cola larga. La media NO describe al jugador típico.")

# Percentiles: dicen más que la media cuando hay cola.
print("\nPercentiles del valor:")
for p in (0.10, 0.25, 0.50, 0.75, 0.90, 0.99):
    print(f"  {p:>5.0%}  {valor.quantile(p):>12,.0f} €")

# ----------------------------------------------------------- Una categórica
print("\n=== nationality ===")
paises = sol["nationality"].value_counts()
print(f"Categorías distintas: {len(paises)}")
print(f"Las 5 primeras concentran el "
      f"{paises.head(5).sum() / len(sol) * 100:.1f} % de los jugadores")
print(f"Hay {(paises == 1).sum()} países con un solo jugador")
print("\nTop 5:")
print(paises.head(5).to_string())

print("\n  Una categórica con 162 valores y una cola enorme de países con")
print("  uno o dos jugadores no se puede usar tal cual en un modelo: en la")
print("  UD6 habrá que agrupar la cola en 'Otros'.")
