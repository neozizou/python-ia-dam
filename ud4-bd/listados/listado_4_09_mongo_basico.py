"""Listado 4.9. MongoDB desde Python: insertar y consultar."""

from conexion_mongo import obtener_cliente
from comun import cargar_ventas

cliente = obtener_cliente()
bd = cliente["tienda"]
coleccion = bd["ventas"]
coleccion.drop()

# Un DataFrame se convierte en una lista de documentos
ventas = cargar_ventas()
documentos = ventas.assign(fecha=ventas["fecha"].dt.strftime("%Y-%m-%d")).to_dict("records")
resultado = coleccion.insert_many(documentos)
print(len(resultado.inserted_ids), "documentos insertados")

# find(filtro, proyección): el filtro es un diccionario
filtro = {"ciudad": "Granada", "importe": {"$gt": 1000}}
proyeccion = {"_id": 0, "producto": 1, "canal": 1, "importe": 1}
print(coleccion.count_documents(filtro), "ventas grandes en Granada")

for documento in coleccion.find(filtro, proyeccion).sort("importe", -1).limit(3):
    print(documento)

# Operadores frecuentes: $gt $gte $lt $lte $ne $in $nin $and $or $regex
print(coleccion.count_documents({"producto": {"$in": ["portátil", "tablet"]}}))
print(coleccion.count_documents({"canal": {"$ne": "online"}}))
