"""Listado 6.6. Regresión: predecir un número y medir el error."""

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from comun import cargar

ventas = cargar()
numericas = ["mes", "descuento", "precio"]
categoricas = ["ciudad", "producto", "canal"]

X = ventas[numericas + categoricas]
y = ventas["unidades"]
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)

modelo = Pipeline([
    ("preparacion", ColumnTransformer([
        ("num", StandardScaler(), numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
    ])),
    ("regresion", LinearRegression()),
])
modelo.fit(X_entrena, y_entrena)
prediccion = modelo.predict(X_prueba)

print(f"MAE:  {mean_absolute_error(y_prueba, prediccion):.2f} unidades")
print(f"RMSE: {root_mean_squared_error(y_prueba, prediccion):.2f} unidades")
print(f"R²:   {r2_score(y_prueba, prediccion):.3f}")

# Referencia obligatoria: ¿lo hace mejor que predecir siempre la media?
media = y_entrena.mean()
print(f"\nModelo ingenuo (siempre la media = {media:.2f}):")
print(f"MAE:  {mean_absolute_error(y_prueba, [media] * len(y_prueba)):.2f} unidades")
