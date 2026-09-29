"""Listado 3.14. Gráficos con matplotlib."""

from pathlib import Path

import matplotlib.pyplot as plt

from comun import cargar_ventas

ventas = cargar_ventas()
GRAFICOS = Path("graficos")
GRAFICOS.mkdir(exist_ok=True)

mensual = ventas.set_index("fecha")["importe"].resample("ME").sum()
por_ciudad = ventas.groupby("ciudad")["importe"].sum().sort_values()

# Una figura con dos ejes (subplots)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

ax1.plot(mensual.index, mensual.values, marker="o", color="#1f77b4")
ax1.set_title("Facturación mensual 2026")
ax1.set_xlabel("Mes")
ax1.set_ylabel("Importe (€)")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)

ax2.barh(por_ciudad.index, por_ciudad.values, color="#2ca02c")
ax2.set_title("Facturación por ciudad")
ax2.set_xlabel("Importe (€)")

fig.tight_layout()
fig.savefig(GRAFICOS / "resumen.png", dpi=150)
plt.show()          # en un notebook el gráfico aparece bajo la celda
print("Guardado en", GRAFICOS / "resumen.png")
