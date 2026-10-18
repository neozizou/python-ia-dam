"""Listado 1.21. Modificar frente a reasignar."""


def modificar(lista):
    lista.append(99)      # cambia el objeto recibido: quien llama lo ve


def reasignar(lista):
    lista = [0]           # solo mueve la etiqueta local: quien llama no lo ve


datos = [1, 2]
modificar(datos)
print(datos)              # [1, 2, 99]
reasignar(datos)
print(datos)              # [1, 2, 99]
