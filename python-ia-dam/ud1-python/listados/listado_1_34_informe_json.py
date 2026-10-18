"""Guardar un informe como JSON y volver a leerlo.

JSON es el formato en el que viajan los datos entre programas. A diferencia de
un CSV, guarda estructuras anidadas: un diccionario dentro de otro, listas
dentro de diccionarios. Es lo que necesitas para un informe, donde cada columna
tiene varios datos asociados.
"""

import json
from pathlib import Path

RUTA = Path("datos/informe_ejemplo.json")
RUTA.parent.mkdir(parents=True, exist_ok=True)

informe = {
    "fichero": "jugadores.csv",
    "edicion": 2020,
    "filas": 18278,
    "columnas": {
        "overall": {"tipo": "entero", "minimo": 48, "maximo": 94, "media": 66.2},
        "nationality": {"tipo": "texto", "distintos": 162},
        "value_eur": {"tipo": "entero", "vacios": 250, "porcentaje_vacios": 1.4},
    },
}

# De objetos de Python a texto. indent lo deja legible; ensure_ascii=False
# escribe las tildes tal cual en vez de como é.
RUTA.write_text(json.dumps(informe, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Escrito {RUTA} ({RUTA.stat().st_size} bytes)")

# Y de vuelta: el JSON leído es un diccionario normal de Python.
recuperado = json.loads(RUTA.read_text(encoding="utf-8"))
print("\nTipo al recuperarlo:", type(recuperado).__name__)
print("Media de overall:   ", recuperado["columnas"]["overall"]["media"])
print("Columnas del informe:", list(recuperado["columnas"]))

print("\n¿Es igual al original?", recuperado == informe)

# JSON no sabe guardar cualquier cosa de Python.
try:
    json.dumps({"paises": {"Spain", "Brazil"}})
except TypeError as error:
    print("\nGuardar un conjunto ->", error)

print("Hay que convertirlo antes:", json.dumps({"paises": sorted({"Spain", "Brazil"})}))

RUTA.unlink()
