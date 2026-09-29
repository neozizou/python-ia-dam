"""Listado 6.16. Entrenar el modelo definitivo y guardarlo."""

import json
from pathlib import Path

import joblib
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from comun import cargar

CARPETA = Path("modelos")
CARPETA.mkdir(exist_ok=True)

ventas = cargar()
categoricas = ["ciudad", "producto", "canal"]
columnas = ["mes", "descuento", "precio"] + categoricas
X = ventas[columnas]
y = ventas["unidades"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)

modelo = Pipeline([
    ("preparacion", ColumnTransformer([("cat", OneHotEncoder(handle_unknown="ignore"),
                                        categoricas)], remainder="passthrough")),
    ("bosque", RandomForestRegressor(n_estimators=300, max_depth=10,
                                     min_samples_leaf=5, random_state=42, n_jobs=-1)),
]).fit(X_entrena, y_entrena)

prediccion = modelo.predict(X_prueba)
metricas = {
    "mae": round(mean_absolute_error(y_prueba, prediccion), 3),
    "r2": round(r2_score(y_prueba, prediccion), 3),
    "version_sklearn": sklearn.__version__,
    "columnas": columnas,
}

# El pipeline se guarda entero: preparación y modelo juntos
joblib.dump(modelo, CARPETA / "modelo_unidades.joblib", compress=3)
(CARPETA / "metricas.json").write_text(json.dumps(metricas, indent=2, ensure_ascii=False),
                                       encoding="utf-8")

print(metricas)
print(f"Tamaño del modelo: "
      f"{(CARPETA / 'modelo_unidades.joblib').stat().st_size / 1024**2:.1f} MB")

# Comprobación: cargarlo y predecir un caso nuevo
cargado = joblib.load(CARPETA / "modelo_unidades.joblib")
caso = {"mes": 6, "descuento": 0.1, "precio": 809.91,
        "ciudad": "Granada", "producto": "portátil", "canal": "online"}
import pandas as pd
print("Predicción para un caso nuevo:",
      round(cargado.predict(pd.DataFrame([caso]))[0], 2), "unidades")
