"""Listado 5.7. Procesamiento en flujo: una pasada, memoria constante."""

import csv
from collections import deque
from pathlib import Path
from typing import Iterator

RUTA = Path("datos") / "ventas_grandes.csv"


def flujo_de_ventas(ruta: Path) -> Iterator[dict]:
    """Simula un flujo de eventos: entrega una venta cada vez (UD2, generadores)."""
    with ruta.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            fila["importe"] = int(fila["unidades"]) * float(fila["precio"].replace(",", "."))
            yield fila


total = 0.0
eventos = 0
por_ciudad: dict[str, float] = {}
ultimas = deque(maxlen=1000)          # ventana deslizante de los 1000 últimos eventos
alertas = 0

for venta in flujo_de_ventas(RUTA):
    eventos += 1
    total += venta["importe"]
    por_ciudad[venta["ciudad"]] = por_ciudad.get(venta["ciudad"], 0) + venta["importe"]
    ultimas.append(venta["importe"])

    if eventos % 250_000 == 0:        # métricas en vivo, sin guardar el histórico
        media_ventana = sum(ultimas) / len(ultimas)
        print(f"{eventos:>9,} eventos | total {total / 1e6:8.1f} M€ | "
              f"media últimos 1000: {media_ventana:8.2f} €")

    if venta["importe"] > 10_000:
        alertas += 1

print(f"\nFin del flujo: {eventos:,} eventos, {alertas:,} ventas por encima de 10.000 €")
print("Ciudad líder:", max(por_ciudad, key=por_ciudad.get))
