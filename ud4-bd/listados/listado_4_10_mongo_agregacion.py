"""Listado 4.10. Agregaciones en MongoDB: el equivalente a GROUP BY."""

from conexion_mongo import obtener_cliente
from comun import cargar_ventas

cliente = obtener_cliente()
coleccion = cliente["tienda"]["ventas"]
coleccion.drop()
ventas = cargar_ventas()
coleccion.insert_many(
    ventas.assign(fecha=ventas["fecha"].dt.strftime("%Y-%m-%d")).to_dict("records")
)

# Una tubería: cada etapa recibe lo que produjo la anterior
tuberia = [
    {"$match": {"canal": {"$ne": "desconocido"}}},                 # WHERE
    {"$group": {"_id": "$ciudad",                                   # GROUP BY
                "ventas": {"$sum": 1},
                "importe": {"$sum": "$importe"},
                "ticket_medio": {"$avg": "$importe"}}},
    {"$sort": {"importe": -1}},                                     # ORDER BY
    {"$limit": 5},                                                  # LIMIT
]

for fila in coleccion.aggregate(tuberia):
    print(f"{fila['_id']:<10} {fila['ventas']:>4} ventas  "
          f"{fila['importe']:>12,.2f} €  media {fila['ticket_medio']:>9,.2f} €")
