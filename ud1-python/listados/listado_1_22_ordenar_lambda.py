"""Listado 1.22. Ordenar con una función clave."""

alumnos = [("Ana", 6.5), ("Luis", 4.0), ("Eva", 9.1)]

ranking = sorted(alumnos, key=lambda a: a[1], reverse=True)
print(ranking)            # [('Eva', 9.1), ('Ana', 6.5), ('Luis', 4.0)]

mejor = max(alumnos, key=lambda a: a[1])
print(mejor)              # ('Eva', 9.1)
