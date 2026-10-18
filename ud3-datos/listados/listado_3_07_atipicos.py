"""Valores atípicos: encontrarlos es fácil; decidir qué hacer, no.

Un atípico es un valor que se aleja mucho del resto. Puede ser un error de
captura, o puede ser el dato más interesante del fichero. La técnica te dice
cuáles son; quién son te dice qué hacer con ellos.
"""

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)
valor = sol["value_eur"].dropna()

# El criterio del rango intercuartílico: fuera de Q3 + 1,5·IQR es atípico.
q1, q3 = valor.quantile([0.25, 0.75])
iqr = q3 - q1
limite = q3 + 1.5 * iqr

print(f"Q1 {q1:>12,.0f} €")
print(f"Q3 {q3:>12,.0f} €")
print(f"Límite superior {limite:>12,.0f} €")

atipicos = sol[sol["value_eur"] > limite]
print(f"\nAtípicos: {len(atipicos):,} de {len(valor):,} ({len(atipicos)/len(valor)*100:.1f} %)")

# Y ahora la pregunta que importa: ¿quiénes son?
print("\nLos cinco más altos:")
print(atipicos.nlargest(5, "value_eur")[
    ["short_name", "club", "overall", "value_eur"]].to_string(index=False))

print("\nNo son errores. Es una distribución con cola larga: unos pocos")
print("jugadores valen cien veces más que la mediana, y eso es el fútbol.")

# Que la distribución sea asimétrica se ve en un número.
print(f"\nAsimetría del valor:            {valor.skew():>6.2f}  (0 sería simétrica)")
import numpy as np
print(f"Asimetría del logaritmo:        {np.log10(valor).skew():>6.2f}")
print("\nPor eso los gráficos de dinero se dibujan en escala logarítmica,")
print("y por eso en la UD6 el modelo predecirá el logaritmo del salario.")

# Comparación de resúmenes, para ver cuánto arrastran los atípicos.
print(f"\nMedia:   {valor.mean():>12,.0f} €")
print(f"Mediana: {valor.median():>12,.0f} €")
print("La media está muy por encima de la mediana: la arrastran los de arriba.")
print("Con datos así, la mediana describe mejor 'el jugador típico'.")
