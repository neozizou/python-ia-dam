"""seaborn: los gráficos estadísticos que más se repiten, ya hechos.

seaborn está construido sobre matplotlib y entiende los DataFrame. Donde en
matplotlib agrupas tú y luego dibujas, aquí le dices qué columna va en cada eje
y él se encarga.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

from comun import cargar_limpio, cargar_posiciones

SALIDA = Path("graficos")
SALIDA.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")       # rejilla discreta y fondo claro

sol = cargar_limpio(edicion=2020).merge(cargar_posiciones(), on="posicion", how="left")

# 1. Comparar una distribución entre grupos: la caja dice mucho en poco sitio.
figura, ejes = plt.subplots(figsize=(8, 4))
sns.boxplot(data=sol, x="linea", y="overall", ax=ejes,
            order=["Portería", "Defensa", "Centro del campo", "Ataque"],
            color="#dbe8fb")
ejes.set_title("Valoración por línea del campo (FIFA 20)")
ejes.set_xlabel("")
ejes.set_ylabel("Valoración media")
figura.tight_layout()
figura.savefig(SALIDA / "caja_por_linea.png", dpi=120)
plt.close(figura)

# 2. Una distribución con su forma: el histograma con curva de densidad.
figura, ejes = plt.subplots(figsize=(8, 4))
sns.histplot(data=sol, x="age", hue="es_portero", bins=25, ax=ejes,
             palette=["#2f6fd0", "#d9822b"], alpha=0.6)
ejes.set_title("Edad de porteros y jugadores de campo")
ejes.set_xlabel("Edad (años)")
ejes.set_ylabel("Jugadores")
figura.tight_layout()
figura.savefig(SALIDA / "edad_porteros.png", dpi=120)
plt.close(figura)

# 3. La relación entre dos variables numéricas, con la recta de ajuste.
muestra = sol.dropna(subset=["wage_eur"]).sample(2000, random_state=42)
figura, ejes = plt.subplots(figsize=(7, 4.5))
sns.regplot(data=muestra, x="overall", y="wage_eur", ax=ejes,
            scatter_kws={"s": 8, "alpha": 0.25, "color": "#2f6fd0"},
            line_kws={"color": "#c0392b"})
ejes.set_yscale("log")
ejes.set_title("Valoración y salario semanal (muestra de 2.000 jugadores)")
ejes.set_xlabel("Valoración media")
ejes.set_ylabel("Salario semanal (€, escala logarítmica)")
figura.tight_layout()
figura.savefig(SALIDA / "salario_vs_media.png", dpi=120)
plt.close(figura)

print("Guardados:", [f.name for f in sorted(SALIDA.glob("*.png"))])
print("\nQué elegir:")
print("  boxplot   comparar una distribución entre pocos grupos")
print("  histplot  ver la forma de una distribución")
print("  regplot   relación entre dos números, con la tendencia dibujada")
print("  barplot   comparar una magnitud entre categorías")
print("\nY lo que NO hay que usar: un gráfico de tarta con más de tres trozos,")
print("y dos ejes verticales distintos en el mismo gráfico. Los dos engañan.")
