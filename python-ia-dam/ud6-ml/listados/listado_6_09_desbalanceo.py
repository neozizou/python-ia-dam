"""Listado 6.9. Clases desbalanceadas, umbral y ROC-AUC."""

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from comun import cargar

ventas = cargar()
numericas = ["mes", "descuento", "precio", "unidades"]
categoricas = ["ciudad", "producto", "canal"]
X = ventas[numericas + categoricas]
y = ventas["devuelta"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

preparacion = ColumnTransformer([
    ("num", StandardScaler(), numericas),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
])


def construir(**opciones):
    return Pipeline([("preparacion", preparacion),
                     ("clasificacion", LogisticRegression(max_iter=1000, **opciones))])


base = construir().fit(X_entrena, y_entrena)
equilibrado = construir(class_weight="balanced").fit(X_entrena, y_entrena)

for nombre, modelo in [("sin ajuste", base), ("class_weight='balanced'", equilibrado)]:
    prediccion = modelo.predict(X_prueba)
    probabilidad = modelo.predict_proba(X_prueba)[:, 1]
    print(f"{nombre:<26} recall={recall_score(y_prueba, prediccion):.3f}  "
          f"ROC-AUC={roc_auc_score(y_prueba, probabilidad):.3f}")

# El umbral por defecto es 0.5, pero se puede mover según el coste de cada error
probabilidad = base.predict_proba(X_prueba)[:, 1]
print("\nEfecto del umbral en el modelo sin ajustar:")
for umbral in (0.5, 0.35, 0.25, 0.15):
    prediccion = (probabilidad >= umbral).astype(int)
    detectadas = recall_score(y_prueba, prediccion)
    avisos = prediccion.sum()
    print(f"  umbral {umbral:.2f}: detecta el {detectadas:.0%} de las devoluciones "
          f"con {avisos} avisos de {len(y_prueba)}")
