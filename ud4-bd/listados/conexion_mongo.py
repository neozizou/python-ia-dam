"""Devuelve un cliente de MongoDB real o una imitación local.

Si existe la variable de entorno MONGODB_URI (por ejemplo, la de un clúster
gratuito de MongoDB Atlas), se conecta de verdad. Si no, usa mongomock, que
imita la API de pymongo en memoria y permite practicar sin conexión.
"""

import os


def obtener_cliente():
    uri = os.environ.get("MONGODB_URI")
    if uri:
        from pymongo import MongoClient

        return MongoClient(uri, serverSelectionTimeoutMS=5000)

    import mongomock

    print("(Sin MONGODB_URI: usando mongomock, una imitación local de MongoDB)")
    return mongomock.MongoClient()
