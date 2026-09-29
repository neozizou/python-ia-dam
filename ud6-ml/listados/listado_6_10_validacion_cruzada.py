"""Listado 6.10. Validación cruzada: una sola partición engaña."""

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from comun import cargar

ventas = cargar()
categoricas = ["ciudad", "producto", "canal"]
X = ventas[["mes", "descuento", "precio"] + categoricas]
y = ventas["unidades"]

modelo = Pipeline([
    ("preparacion", ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"),
                                        categoricas)], remainder="passthrough")),
    ("modelo", RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)),
])

# Una sola partición: el resultado depende del azar de random_state
for semilla in (0, 1, 2):
    X_e, X_p, y_e, y_p = train_test_split(X, y, test_size=0.2, random_state=semilla)
    modelo.fit(X_e, y_e)
    print(f"random_state={semilla}: R² = {modelo.score(X_p, y_p):.3f}")

# Validación cruzada: 5 particiones, cada dato es de prueba exactamente una vez
particiones = KFold(n_splits=5, shuffle=True, random_state=42)
puntuaciones = cross_val_score(modelo, X, y, cv=particiones, scoring="r2")
print(f"\nR² en 5 particiones: {np.round(puntuaciones, 3)}")
print(f"Media {puntuaciones.mean():.3f} ± {puntuaciones.std():.3f}")

# Para clasificación se usa StratifiedKFold, que conserva la proporción de clases
