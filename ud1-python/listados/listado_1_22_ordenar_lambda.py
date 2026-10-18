"""Listado 1.22. Ordenar con una función clave."""

jugadores = [("L. Messi", 94), ("Sergio Ramos", 89), ("J. Oblak", 91)]

# key recibe cada elemento y devuelve el valor por el que se ordena.
ranking = sorted(jugadores, key=lambda j: j[1], reverse=True)
print(ranking)           # [('L. Messi', 94), ('J. Oblak', 91), ('Sergio Ramos', 89)]

mejor = max(jugadores, key=lambda j: j[1])
print(mejor)             # ('L. Messi', 94)

# Ordenar por dos criterios: primero por media (de mayor a menor) y, a igualdad,
# por nombre alfabético. El menos solo vale para números.
plantilla = [("Hazard", 91), ("De Bruyne", 91), ("Oblak", 91), ("Messi", 94)]
print(sorted(plantilla, key=lambda j: (-j[1], j[0])))
