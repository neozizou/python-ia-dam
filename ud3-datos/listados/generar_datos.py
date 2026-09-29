"""Genera datos/ventas_2026.csv, el fichero de ejemplo de la UD3.

Es un fichero sintético pero realista: incluye valores vacíos, duplicados,
espacios sobrantes y precios en formato español, para poder practicar la limpieza.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(2026)

CIUDADES = ["Granada", "Málaga", "Sevilla", "Córdoba", "Almería", "Jaén", "Cádiz", "Huelva"]
PRODUCTOS = {
    "portátil": 899.90,
    "monitor": 180.00,
    "teclado": 25.00,
    "ratón": 12.50,
    "tablet": 349.00,
    "impresora": 149.90,
}
CANALES = ["tienda", "online", "teléfono"]

filas = []
inicio = date(2026, 1, 1)

for i in range(1200):
    producto = random.choice(list(PRODUCTOS))
    precio = PRODUCTOS[producto] * random.choice([1.0, 1.0, 0.9, 1.1])
    fila = {
        "id_venta": 1000 + i,
        "fecha": (inicio + timedelta(days=random.randint(0, 364))).isoformat(),
        "ciudad": random.choice(CIUDADES),
        "producto": producto,
        "canal": random.choice(CANALES),
        "unidades": random.randint(1, 12),
        "precio": f"{precio:.2f}".replace(".", ","),
        "cliente": f"CLI-{random.randint(1, 300):03d}",
    }
    filas.append(fila)

# Suciedad deliberada
for fila in random.sample(filas, 60):
    fila["unidades"] = ""                       # valores ausentes
for fila in random.sample(filas, 40):
    fila["canal"] = ""
for fila in random.sample(filas, 25):
    fila["ciudad"] = f"  {fila['ciudad'].upper()} "   # espacios y mayúsculas
for fila in random.sample(filas, 10):
    fila["unidades"] = random.randint(200, 400)       # valores atípicos

filas.extend(random.sample(filas, 15))          # duplicados exactos

destino = Path("datos") / "ventas_2026.csv"
destino.parent.mkdir(exist_ok=True)
with destino.open("w", encoding="utf-8", newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=list(filas[0]), delimiter=";")
    escritor.writeheader()
    escritor.writerows(filas)

print(f"{destino}: {len(filas)} filas")
