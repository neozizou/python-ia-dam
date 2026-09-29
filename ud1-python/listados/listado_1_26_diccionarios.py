"""Listado 1.26. Crear, consultar, modificar y recorrer un diccionario."""

alumno = {"nombre": "Ana", "nota": 6.5, "ciclo": "DAM"}

print(alumno["nombre"])                   # 'Ana'
# print(alumno["telefono"])               # descomenta para ver el KeyError
print(alumno.get("email"))                # None: no lanza error
print(alumno.get("email", "sin email"))   # valor alternativo

alumno["nota"] = 7.0                      # modificar
alumno["email"] = "ana@example.com"       # añadir
del alumno["email"]                       # eliminar

print("nota" in alumno)                   # True: busca entre las CLAVES

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
