"""Elegir filas y columnas: `[]`, `.loc` y `.iloc`.

La confusión más habitual de quien empieza con pandas es mezclar las tres
formas. La regla es corta: los corchetes sueltos eligen **columnas**, `.loc`
elige por **etiqueta** y `.iloc` por **posición**.
"""

from comun import cargar_limpio

sol = cargar_limpio(edicion=2020)

# Una columna es una Series; dos o más, un DataFrame.
print("Una columna ->", type(sol["overall"]).__name__)
print("Varias      ->", type(sol[["short_name", "overall"]]).__name__)

# Filtrar filas: una condición dentro de los corchetes.
estrellas = sol[sol["overall"] >= 90]
print(f"\nJugadores con media 90 o más: {len(estrellas)}")

# Varias condiciones: paréntesis obligatorios, y & | en lugar de and / or.
jovenes_promesa = sol[(sol["age"] <= 21) & (sol["potential"] >= 85)]
print(f"Menores de 22 con potencial 85+: {len(jovenes_promesa)}")
print(jovenes_promesa.nlargest(5, "potential")[
    ["short_name", "age", "club", "overall", "potential"]].to_string(index=False))

# .loc: filas por condición, columnas por nombre, en una sola orden.
print("\n.loc con condición y columnas:")
print(sol.loc[sol["nationality"] == "Spain",
              ["short_name", "club", "overall"]].head(3).to_string(index=False))

# .iloc: por posición, como una lista. Útil para mirar, poco para analizar.
print("\n.iloc[0, :3]:", list(sol.iloc[0, :3]))

# isin evita escribir una cadena de condiciones con |.
tres_grandes = sol[sol["club"].isin(["FC Barcelona", "Real Madrid", "Atlético Madrid"])]
print(f"\nJugadores de los tres grandes: {len(tres_grandes)}")

# between, para rangos.
veteranos = sol[sol["age"].between(34, 40)]
print(f"Entre 34 y 40 años: {len(veteranos)}")

# Y el aviso clásico: esto modifica una copia, no el original.
print("\nOrdenar no modifica: sol sigue igual tras sort_values()")
print(sol.sort_values("overall", ascending=False).head(2)["short_name"].tolist())
