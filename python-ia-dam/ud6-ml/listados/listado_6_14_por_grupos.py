"""Listado 6.14. Evaluar por grupos: la media esconde diferencias."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
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

evaluacion = X_prueba.copy()
evaluacion["real"] = y_prueba
evaluacion["prediccion"] = modelo.predict(X_prueba)

print(f"MAE global: {mean_absolute_error(evaluacion['real'], evaluacion['prediccion']):.2f}\n")

for columna in ("producto", "canal"):
    tabla = (
        evaluacion.groupby(columna)
        .apply(lambda g: pd.Series({
            "casos": len(g),
            "MAE": mean_absolute_error(g["real"], g["prediccion"]),
            "error_medio": (g["prediccion"] - g["real"]).mean(),
        }), include_groups=False)
        .round(2)
        .sort_values("MAE", ascending=False)
    )
    print(tabla, "\n")

print("Un error medio positivo indica que el modelo SOBREESTIMA en ese grupo.")
