"""Listado 6.13. Qué variables usa el modelo."""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from comun import cargar

ventas = cargar()
categoricas = ["ciudad", "producto", "canal"]
X = ventas[["mes", "descuento", "precio"] + categoricas]
y = ventas["unidades"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)

modelo = Pipeline([
    ("preparacion", ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"),
                                        categoricas)], remainder="passthrough")),
    ("bosque", RandomForestRegressor(n_estimators=200, max_depth=10,
                                     min_samples_leaf=5, random_state=42, n_jobs=-1)),
]).fit(X_entrena, y_entrena)

# 1. Importancia interna del bosque, por columna ya transformada
nombres = modelo.named_steps["preparacion"].get_feature_names_out()
importancias = pd.Series(modelo.named_steps["bosque"].feature_importances_, index=nombres)
print("Las 6 columnas más usadas por el bosque:")
print(importancias.sort_values(ascending=False).head(6).round(3))

# 2. Importancia por permutación: cuánto empeora al barajar cada variable ORIGINAL
resultado = permutation_importance(modelo, X_prueba, y_prueba, n_repeats=10,
                                   random_state=42, scoring="neg_mean_absolute_error",
                                   n_jobs=-1)
permutacion = pd.Series(resultado.importances_mean, index=X.columns)
print("\nImportancia por permutación (empeoramiento del MAE):")
print(permutacion.sort_values(ascending=False).round(3))
print("\nLa importancia dice qué usa el modelo, no qué CAUSA la venta.")
