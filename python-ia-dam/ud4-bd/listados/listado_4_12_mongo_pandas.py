"""Listado 4.12. Del resultado de MongoDB a un DataFrame."""

import pandas as pd

from conexion_mongo import obtener_cliente
from comun import cargar_ventas

cliente = obtener_cliente()
coleccion = cliente["tienda"]["ventas"]
coleccion.drop()
ventas = cargar_ventas()
coleccion.insert_many(
    ventas.assign(fecha=ventas["fecha"].dt.strftime("%Y-%m-%d")).to_dict("records")
)

cursor = coleccion.find({"importe": {"$gt": 2000}}, {"_id": 0})
grandes = pd.DataFrame(list(cursor))         # el cursor se consume una sola vez

print(grandes.shape)
print(grandes.groupby("producto")["importe"].sum().round(2).sort_values(ascending=False))
