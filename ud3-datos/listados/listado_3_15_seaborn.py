"""Listado 3.15. Gráficos estadísticos con seaborn."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from comun import cargar_ventas

sns.set_theme(style="whitegrid")          # estilo común para todos los gráficos

ventas = cargar_ventas()
GRAFICOS = Path("graficos")
GRAFICOS.mkdir(exist_ok=True)

fig, ejes = plt.subplots(2, 2, figsize=(13, 9))

# 1. Distribución de una variable numérica
sns.histplot(data=ventas, x="importe", bins=40, ax=ejes[0, 0])
ejes[0, 0].set_title("Distribución del importe por venta")

# 2. Comparar una numérica entre categorías
sns.boxplot(data=ventas, x="canal", y="importe", ax=ejes[0, 1])
ejes[0, 1].set_title("Importe según el canal")

# 3. Comparar un agregado entre categorías
por_producto = ventas.groupby("producto")["importe"].sum().reset_index()
sns.barplot(data=por_producto, x="importe", y="producto", ax=ejes[1, 0])
ejes[1, 0].set_title("Facturación por producto")

# 4. Relación entre dos numéricas
sns.scatterplot(data=ventas, x="unidades", y="importe", hue="canal", alpha=0.6,
                ax=ejes[1, 1])
ejes[1, 1].set_title("Unidades frente a importe")

fig.tight_layout()
fig.savefig(GRAFICOS / "seaborn.png", dpi=150)
print("Guardado en", GRAFICOS / "seaborn.png")
