"""Un diccionario para describir un jugador: cada dato con su nombre.

Una lista guarda cosas en orden y se accede por posición. Un diccionario las
guarda con una etiqueta y se accede por esa etiqueta, que es mucho más legible
cuando cada dato significa algo distinto.
"""

# En una lista tendrías que acordarte de que la posición 3 es la media.
messi_en_lista = ["L. Messi", 32, "FC Barcelona", 94]
print("Con lista:      ", messi_en_lista[3])

# Con un diccionario, el propio código dice qué es cada cosa.
messi = {
    "nombre": "L. Messi",
    "edad": 32,
    "club": "FC Barcelona",
    "media": 94,
    "posiciones": ["RW", "CF", "ST"],
}
print("Con diccionario:", messi["media"])

# Leer una clave que no existe lanza KeyError; `get` devuelve None o lo que digas.
print("\nPaís (no está):      ", messi.get("pais"))
print("País con valor por defecto:", messi.get("pais", "desconocido"))

# Añadir y modificar es asignar. No hay que declarar nada antes.
messi["pais"] = "Argentina"
messi["edad"] += 1
print("\nTras un año:", messi["edad"], "años, país", messi["pais"])

# Recorrer: por claves, por valores o por las dos cosas a la vez.
print("\nFicha completa:")
for clave, valor in messi.items():
    print(f"  {clave:<12} {valor}")

# Un valor puede ser cualquier cosa, incluida otra lista u otro diccionario.
print("\nPrimera posición:", messi["posiciones"][0])
print("¿Juega de portero?", "GK" in messi["posiciones"])
