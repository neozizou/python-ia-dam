"""`groupby`: partir, calcular y volver a juntar.

Es la operación más importante de pandas y la que más se usa. Hace en una línea
lo que en la UD1 costaba dos diccionarios y un bucle: partir los datos en
grupos, calcular algo en cada uno y devolver el resultado.
"""

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)

# Lo mínimo: una columna para agrupar, una para calcular, una operación.
print("Media de valoración por posición:")
print(sol.groupby("posicion")["overall"].mean().round(1)
      .sort_values(ascending=False).head(5).to_string())

# Varias operaciones a la vez, con nombres propios para las columnas.
print("\nResumen por línea del campo:")
resumen = sol.groupby("posicion").agg(
    jugadores=("sofifa_id", "size"),
    media=("overall", "mean"),
    edad=("age", "mean"),
    valor_mediano=("value_eur", "median"),
).round(1).sort_values("valor_mediano", ascending=False)
print(resumen.head(8).to_string())

# Agrupar por dos columnas da un índice de dos niveles.
print("\nValoración media por posición y pie bueno (primeras filas):")
doble = sol.groupby(["posicion", "preferred_foot"])["overall"].mean().round(1)
print(doble.head(6).to_string())

# Filtrar grupos pequeños: con menos de 100 jugadores la media no dice nada.
print("\nPaíses con mejor media (mínimo 100 jugadores):")
por_pais = sol.groupby("nationality").agg(
    jugadores=("sofifa_id", "size"), media=("overall", "mean"))
grandes = por_pais[por_pais["jugadores"] >= 100]
print(grandes.nlargest(5, "media").round(1).to_string())

print(f"\n  Sin ese filtro, el primero sería un país con "
      f"{por_pais.nlargest(1, 'media')['jugadores'].iloc[0]} jugador(es):")
print("  ", por_pais.nlargest(3, "media").round(1).to_string().replace("\n", "\n   "))
