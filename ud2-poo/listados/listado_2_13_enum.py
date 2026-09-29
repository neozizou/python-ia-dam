"""Listado 2.13. Enumeraciones: conjuntos cerrados de valores."""

from enum import Enum


class Estado(Enum):
    MATRICULADO = "matriculado"
    APROBADO = "aprobado"
    SUSPENSO = "suspenso"


estado = Estado.APROBADO

print(estado, estado.name, estado.value)      # Estado.APROBADO APROBADO aprobado
print(estado is Estado.APROBADO)              # True: comparación por identidad
print(Estado("suspenso"))                     # Estado.SUSPENSO: desde el valor
print([e.value for e in Estado])              # recorrible
