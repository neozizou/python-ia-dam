"""Listado 1.24. Alias, copia y el error de la matriz."""

a = [1, 2, 3]
b = a              # alias: a y b son la misma lista
b.append(4)
print(a)           # [1, 2, 3, 4]

c = a.copy()       # copia independiente (también vale a[:] o list(a))
c.append(5)
print(a)           # [1, 2, 3, 4]

matriz = [[0] * 3] * 2              # MAL: dos referencias a la misma fila
matriz[0][0] = 9
print(matriz)                       # [[9, 0, 0], [9, 0, 0]]

matriz = [[0] * 3 for _ in range(2)]    # BIEN: dos filas distintas
matriz[0][0] = 9
print(matriz)                           # [[9, 0, 0], [0, 0, 0]]
