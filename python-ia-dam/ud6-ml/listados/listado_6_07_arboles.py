"""Listado 6.7. Árboles y bosques: capturar relaciones no lineales."""

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

from comun import cargar

ventas = cargar()
numericas = ["mes", "descuento", "precio"]
categoricas = ["ciudad", "producto", "canal"]
X = ventas[numericas + categoricas]
y = ventas["unidades"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)

preparacion = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
], remainder="passthrough")     # los árboles no necesitan escalado

modelos = {
    "Regresión lineal": LinearRegression(),
    "Árbol (profundidad 5)": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Árbol sin podar": DecisionTreeRegressor(random_state=42),
    "Bosque aleatorio": RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1),
}

print(f"{'Modelo':<24} {'MAE entrena':>12} {'MAE prueba':>11} {'R² prueba':>10}")
for nombre, estimador in modelos.items():
    modelo = Pipeline([("preparacion", preparacion), ("modelo", estimador)])
    modelo.fit(X_entrena, y_entrena)
    mae_entrena = mean_absolute_error(y_entrena, modelo.predict(X_entrena))
    mae_prueba = mean_absolute_error(y_prueba, modelo.predict(X_prueba))
    r2 = r2_score(y_prueba, modelo.predict(X_prueba))
    print(f"{nombre:<24} {mae_entrena:>12.2f} {mae_prueba:>11.2f} {r2:>10.3f}")
