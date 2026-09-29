"""Listado 4.8. El modelo documental con TinyDB, sin instalar ningún servidor."""

from pathlib import Path

from tinydb import Query, TinyDB

RUTA = Path("datos") / "catalogo.json"
RUTA.unlink(missing_ok=True)

bd = TinyDB(RUTA, indent=2, ensure_ascii=False)
productos = bd.table("productos")

# Cada documento es un diccionario: pueden tener campos distintos
productos.insert({"nombre": "portátil", "precio": 899.90, "stock": 12,
                  "especificaciones": {"ram_gb": 16, "ssd_gb": 512}})
productos.insert({"nombre": "ratón", "precio": 12.50, "stock": 120,
                  "inalambrico": True})
productos.insert({"nombre": "monitor", "precio": 180.00, "stock": 30,
                  "especificaciones": {"pulgadas": 27}})

P = Query()
print(productos.search(P.precio > 100))
print(productos.search(P.especificaciones.ram_gb == 16))     # busca dentro del documento
productos.update({"stock": 25}, P.nombre == "monitor")
print(productos.get(P.nombre == "monitor"))
print(len(productos), "documentos en", RUTA)
