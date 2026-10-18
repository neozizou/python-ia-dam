"""Listado 1.23. Operaciones habituales con listas."""

notas = [6.5, 4.0, 9.1]

notas.append(7.25)        # añade al final
notas.insert(0, 5.0)      # inserta en una posición
print(notas)              # [5.0, 6.5, 4.0, 9.1, 7.25]

ultima = notas.pop()      # extrae y devuelve el último: 7.25
notas.remove(4.0)         # elimina la primera aparición de un valor
print(ultima, notas)      # 7.25 [5.0, 6.5, 9.1]

print(sorted(notas, reverse=True))   # devuelve una lista NUEVA ordenada
notas.sort(reverse=True)             # ordena la lista ORIGINAL y devuelve None
print(notas)                         # [9.1, 6.5, 5.0]

print(9.1 in notas)       # True: pertenencia
print(len(notas))         # 3
