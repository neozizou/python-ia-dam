"""Listado 6.4. ColumnTransformer y Pipeline: la preparación, dentro del modelo."""

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
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

# Cada grupo de columnas recibe su tratamiento
preparacion = ColumnTransformer([
    ("numericas", StandardScaler(), numericas),
    ("categoricas", OneHotEncoder(handle_unknown="ignore"), categoricas),
])

# El pipeline encadena preparación y modelo en un solo objeto con fit/predict
modelo = Pipeline([
    ("preparacion", preparacion),
    ("regresion", LinearRegression()),
])

modelo.fit(X_entrena, y_entrena)
print("R² en prueba:", round(modelo.score(X_prueba, y_prueba), 3))
print("Columnas tras la preparación:",
      modelo.named_steps["preparacion"].get_feature_names_out().shape[0])
