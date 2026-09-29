"""Listado 6.2. Características, objetivo y partición en entrenamiento y prueba."""

from sklearn.model_selection import train_test_split

from comun import cargar

ventas = cargar()

# X: lo que el modelo puede mirar. y: lo que queremos predecir
caracteristicas = ["mes", "ciudad", "producto", "canal", "descuento", "precio"]
X = ventas[caracteristicas]
y = ventas["unidades"]

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42      # random_state fija el reparto
)

print(f"Entrenamiento: {len(X_entrena):,} filas")
print(f"Prueba:        {len(X_prueba):,} filas")
print(f"Media de unidades: entrena {y_entrena.mean():.2f} | prueba {y_prueba.mean():.2f}")
print(X.dtypes)
