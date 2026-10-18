"""Listado 6.12. Ajuste de hiperparámetros con GridSearchCV."""

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, train_test_split
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
    ("bosque", RandomForestRegressor(random_state=42, n_jobs=-1)),
])

# Los nombres de los parámetros llevan el prefijo del paso del pipeline
rejilla = {
    "bosque__n_estimators": [100, 300],
    "bosque__max_depth": [6, 10, None],
    "bosque__min_samples_leaf": [1, 5],
}

busqueda = GridSearchCV(modelo, rejilla, cv=5, scoring="neg_mean_absolute_error",
                        n_jobs=-1)
busqueda.fit(X_entrena, y_entrena)      # 12 combinaciones x 5 particiones = 60 ajustes

print("Mejores parámetros:", busqueda.best_params_)
print(f"MAE en validación cruzada: {-busqueda.best_score_:.3f}")
print(f"MAE en el conjunto de prueba: "
      f"{-busqueda.score(X_prueba, y_prueba):.3f}")

# El mejor modelo, ya reentrenado con todos los datos de entrenamiento
mejor_modelo = busqueda.best_estimator_
