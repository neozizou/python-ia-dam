"""Listado 4.11. Esquema flexible e índices en MongoDB."""

from conexion_mongo import obtener_cliente

cliente = obtener_cliente()
catalogo = cliente["tienda"]["catalogo"]
catalogo.drop()

# Documentos de la misma colección con campos distintos: no hay ALTER TABLE
catalogo.insert_many([
    {"nombre": "portátil", "precio": 899.90,
     "especificaciones": {"ram_gb": 16, "ssd_gb": 512}},
    {"nombre": "ratón", "precio": 12.50, "inalambrico": True},
    {"nombre": "monitor", "precio": 180.00,
     "especificaciones": {"pulgadas": 27}, "etiquetas": ["oficina", "hogar"]},
])

print(list(catalogo.find({"especificaciones.ram_gb": {"$gte": 8}}, {"_id": 0, "nombre": 1})))
print(list(catalogo.find({"etiquetas": "oficina"}, {"_id": 0, "nombre": 1})))

catalogo.create_index("nombre")                      # índice simple
catalogo.create_index([("precio", -1)])              # descendente
print("Índices:", sorted(catalogo.index_information()))

# La flexibilidad tiene precio: nada impide guardar "precio": "899,90" como texto
catalogo.insert_one({"nombre": "teclado", "precio": "25,00"})
print("Precios que no son números:",
      catalogo.count_documents({"precio": {"$type": "string"}}))
