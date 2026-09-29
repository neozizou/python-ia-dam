"""Listado 6.11. Sobreajuste: cuándo el modelo memoriza en vez de aprender."""

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

from comun import cargar

ventas = cargar()
categoricas = ["ciudad", "producto", "canal"]
X = ventas[["mes", "descuento", "precio"] + categoricas]
y = ventas["unidades"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)

profundidades = range(1, 21)
error_entrena, error_prueba = [], []

for profundidad in profundidades:
    modelo = Pipeline([
        ("preparacion", ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"),
                                            categoricas)], remainder="passthrough")),
        ("arbol", DecisionTreeRegressor(max_depth=profundidad, random_state=42)),
    ]).fit(X_entrena, y_entrena)
    error_entrena.append(mean_absolute_error(y_entrena, modelo.predict(X_entrena)))
    error_prueba.append(mean_absolute_error(y_prueba, modelo.predict(X_prueba)))

mejor = min(zip(error_prueba, profundidades))
print(f"Mejor profundidad: {mejor[1]} (MAE en prueba {mejor[0]:.2f})")
for p, e, s in zip(profundidades, error_entrena, error_prueba):
    if p in (1, 3, 5, 8, 12, 20):
        print(f"profundidad {p:>2}: entrena {e:.2f} | prueba {s:.2f}")

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(profundidades, error_entrena, marker="o", label="Entrenamiento")
ax.plot(profundidades, error_prueba, marker="o", label="Prueba")
ax.axvline(mejor[1], color="gray", linestyle="--", alpha=0.7)
ax.set_xlabel("Profundidad máxima del árbol")
ax.set_ylabel("MAE (unidades)")
ax.set_title("Subajuste, punto óptimo y sobreajuste")
ax.legend()
ax.grid(alpha=0.3)
fig.tight_layout()
Path("graficos").mkdir(exist_ok=True)
fig.savefig(Path("graficos") / "sobreajuste.png", dpi=150)
print("Gráfico guardado en graficos/sobreajuste.png")
