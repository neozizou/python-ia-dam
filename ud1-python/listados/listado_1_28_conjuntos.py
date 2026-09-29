"""Listado 1.28. Operaciones con conjuntos."""

matriculados = {"Ana", "Luis", "Eva", "Juan"}
aprobados = {"Ana", "Eva", "Marta"}

print(matriculados & aprobados)     # intersección
print(matriculados - aprobados)     # diferencia
print(matriculados | aprobados)     # unión
print(matriculados ^ aprobados)     # diferencia simétrica

print(sorted(set([3, 1, 3, 2, 1])))   # quitar duplicados: [1, 2, 3]
# Al imprimir un conjunto, el orden de los elementos puede variar.
