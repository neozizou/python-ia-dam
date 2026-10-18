"""De los números a los hallazgos.

Un análisis no termina en una tabla: termina en frases que alguien pueda usar
para decidir algo. Un hallazgo bien escrito tiene tres partes: qué has visto,
el dato que lo respalda y qué sugiere hacer.
"""

from comun import cargar_limpio, cargar_posiciones

sol = cargar_limpio(edicion=2020).merge(cargar_posiciones(), on="posicion", how="left")
panel = cargar_limpio()

print("=" * 68)
print("CINCO HALLAZGOS SOBRE EL MERCADO DE FIFA 20")
print("=" * 68)

# --- 1 ---
valor = sol["value_eur"].dropna()
print(f"\n1. El mercado está muy concentrado.")
print(f"   Dato: el 1 % más caro ({int(len(valor) * 0.01)} jugadores) acumula el "
      f"{valor.nlargest(int(len(valor) * 0.01)).sum() / valor.sum() * 100:.0f} % "
      f"del valor total.")
print("   Sugiere: cualquier media sobre el valor hay que leerla con cuidado;")
print("   usa la mediana para describir al jugador típico.")

# --- 2 ---
jovenes = sol[(sol["age"] <= 21) & (sol["potential"] - sol["overall"] >= 10)]
print(f"\n2. Hay una bolsa de jóvenes con mucho recorrido.")
print(f"   Dato: {len(jovenes)} jugadores de 21 años o menos tienen al menos")
print(f"   10 puntos de margen de mejora. Su valor mediano es "
      f"{jovenes['value_eur'].median():,.0f} €, frente a los "
      f"{valor.median():,.0f} € del conjunto.")
print("   Sugiere: es el segmento donde buscar si el presupuesto es corto.")

# --- 3 ---
# Para comparar salarios entre puestos hay que comparar jugadores del mismo
# nivel: si no, se mezcla el efecto del puesto con el de la calidad.
similares = sol[sol["overall"].between(70, 75)]
por_linea = similares.groupby("linea")["wage_eur"].median().sort_values(ascending=False)
print(f"\n3. A igual nivel, el puesto cambia el salario.")
print(f"   Dato: entre los jugadores de valoración 70 a 75 "
      f"({len(similares):,} jugadores),")
print(f"   el salario mediano va de {por_linea.iloc[0]:,.0f} € en "
      f"{por_linea.index[0].lower()} a {por_linea.iloc[-1]:,.0f} € en "
      f"{por_linea.index[-1].lower()}.")
print("   Sugiere: el puesto tiene que entrar en el modelo de la UD6.")

# --- 4 ---
cambio = panel.groupby("fifa")["value_eur"].median()
print(f"\n4. El mercado sube despacio pero sin pausa.")
print(f"   Dato: el valor mediano pasa de {cambio.iloc[0]:,.0f} € en "
      f"{cambio.index[0]} a {cambio.iloc[-1]:,.0f} € en {cambio.index[-1]}, "
      f"un {(cambio.iloc[-1] / cambio.iloc[0] - 1) * 100:.0f} % en cinco años.")
print("   Sugiere: comparar valores de ediciones distintas sin corregir la")
print("   subida general lleva a conclusiones falsas.")

# --- 5 ---
zurdos = sol.groupby("linea")["preferred_foot"].apply(
    lambda s: (s == "Left").mean() * 100)
print(f"\n5. Los zurdos se concentran en defensa.")
print(f"   Dato: son el {zurdos['Defensa']:.0f} % de los defensas y solo el "
      f"{zurdos['Ataque']:.0f} % de los delanteros.")
print("   Sugiere: el pie bueno no es una variable neutra; conviene mirarlo")
print("   junto con el puesto y no por separado.")

print("\n" + "=" * 68)
print("Fíjate en que ninguno dice 'la media es 66,2'. Un número no es un")
print("hallazgo: lo es la frase que explica qué significa y qué hacer con él.")
