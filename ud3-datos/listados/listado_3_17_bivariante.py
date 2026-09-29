"""Listado 3.17. Análisis exploratorio: relaciones entre variables."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from comun import cargar_ventas

ventas = cargar_ventas()

# Numérica frente a categórica
print(ventas.groupby("canal")["importe"].agg(["count", "mean", "median"]).round(2))

# Numérica frente a numérica: matriz de correlación
numericas = ventas[["unidades", "precio", "importe", "mes"]]
correlacion = numericas.corr().round(2)
print("\nCorrelación de Pearson:")
print(correlacion)

sns.set_theme(style="white")
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(correlacion, annot=True, cmap="Blues", vmin=-1, vmax=1, ax=ax)
ax.set_title("Correlación entre variables numéricas")
fig.tight_layout()

GRAFICOS = Path("graficos")
GRAFICOS.mkdir(exist_ok=True)
fig.savefig(GRAFICOS / "correlacion.png", dpi=150)
print("\nGuardado en", GRAFICOS / "correlacion.png")
