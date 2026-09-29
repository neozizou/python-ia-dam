"""Listado 1.20. Valores por defecto mutables: el error y su corrección."""


def anadir_mal(elemento, lista=[]):        # MAL
    lista.append(elemento)
    return lista


print(anadir_mal(1))    # [1]
print(anadir_mal(2))    # [1, 2]   ← la lista «por defecto» sobrevive entre llamadas


def anadir(elemento, lista=None):          # BIEN
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista


print(anadir(1))        # [1]
print(anadir(2))        # [2]
