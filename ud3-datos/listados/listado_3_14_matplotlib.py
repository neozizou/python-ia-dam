"""matplotlib: la base de todos los gráficos de Python.

Casi siempre usarás seaborn o pandas por encima, pero los dos devuelven objetos
de matplotlib, así que para ajustar cualquier detalle hay que conocer sus dos
piezas: la **figura** (el lienzo) y los **ejes** (cada gráfico dentro).
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")                 # sin ventana: guarda en fichero
import matplotlib.pyplot as plt

from comun import cargar_limpio

SALIDA = Path("graficos")
SALIDA.mkdir(exist_ok=True)

sol = cargar_limpio(edicion=2020)

# Un gráfico: una figura con unos ejes.
figura, ejes = plt.subplots(figsize=(7, 4))
ejes.hist(sol["overall"], bins=30, color="#2f6fd0", edgecolor="white")
ejes.set_title("Cómo se reparten las valoraciones (FIFA 20)")
ejes.set_xlabel("Valoración media")
ejes.set_ylabel("Número de jugadores")
ejes.grid(axis="y", alpha=0.3)        # rejilla discreta, solo donde ayuda
figura.tight_layout()
figura.savefig(SALIDA / "distribucion_overall.png", dpi=120)
plt.close(figura)

# Varios gráficos en una figura: subplots devuelve una rejilla de ejes.
figura, (izq, der) = plt.subplots(1, 2, figsize=(11, 4))

izq.scatter(sol["age"], sol["overall"], s=4, alpha=0.15, color="#2f6fd0")
izq.set_title("Edad frente a valoración")
izq.set_xlabel("Edad (años)")
izq.set_ylabel("Valoración media")

con_valor = sol.dropna(subset=["value_eur"])
der.scatter(con_valor["overall"], con_valor["value_eur"], s=4, alpha=0.15,
            color="#1f9d6b")
der.set_yscale("log")                 # el dinero, siempre en escala logarítmica
der.set_title("Valoración frente a valor de mercado")
der.set_xlabel("Valoración media")
der.set_ylabel("Valor (€, escala logarítmica)")

figura.tight_layout()
figura.savefig(SALIDA / "dispersion.png", dpi=120)
plt.close(figura)

print("Guardados en graficos/:")
for fichero in sorted(SALIDA.glob("*.png")):
    print(f"  {fichero.name:<28} {fichero.stat().st_size // 1024} KB")

print("\nTres reglas que no se negocian:")
print("  1. Todo gráfico lleva título y los dos ejes etiquetados, con unidades.")
print("  2. El dinero va en escala logarítmica: si no, los diez primeros")
print("     aplastan a los dieciocho mil restantes.")
print("  3. Con muchos puntos, alpha baja: así se ve dónde se acumulan.")
