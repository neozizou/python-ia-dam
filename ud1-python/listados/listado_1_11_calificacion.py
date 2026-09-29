"""Listado 1.11. Calificación a partir de una nota."""

nota = 7.5

if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif nota < 5:
    calificacion = "Insuficiente"
elif nota < 6:
    calificacion = "Suficiente"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print(calificacion)      # Notable

# Expresión condicional (el «ternario» de Python)
estado = "aprobado" if nota >= 5 else "suspenso"
print(estado)            # aprobado
