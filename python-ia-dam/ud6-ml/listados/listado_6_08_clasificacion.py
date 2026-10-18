"""Listado 6.8. Clasificación: predecir una categoría."""

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from comun import cargar

ventas = cargar()
numericas = ["mes", "descuento", "precio", "unidades"]
categoricas = ["ciudad", "producto", "canal"]

X = ventas[numericas + categoricas]
y = ventas["devuelta"]                      # 1 = el pedido se devolvió
print("Reparto de clases:", y.value_counts(normalize=True).round(3).to_dict())

# stratify mantiene la proporción de clases en ambas particiones
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

modelo = Pipeline([
    ("preparacion", ColumnTransformer([
        ("num", StandardScaler(), numericas),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
    ])),
    ("clasificacion", LogisticRegression(max_iter=1000)),
])
modelo.fit(X_entrena, y_entrena)
prediccion = modelo.predict(X_prueba)

print("\nMatriz de confusión (filas: real, columnas: predicho)")
print(confusion_matrix(y_prueba, prediccion))
print("\n", classification_report(y_prueba, prediccion,
                                  target_names=["no devuelta", "devuelta"]))
