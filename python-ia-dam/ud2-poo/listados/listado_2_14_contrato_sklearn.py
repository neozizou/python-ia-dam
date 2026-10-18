"""El mismo patrón, en scikit-learn: un contrato y muchas implementaciones.

`Pipeline` no conoce ninguna clase concreta. Le basta con que cada paso tenga
`fit` y `transform`, y el último, `fit` y `predict`. Es exactamente lo que hace
`ProductoService` con `ProductoRepository`.
"""

import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_regression(n_samples=200, n_features=3, noise=8.0, random_state=42)

modelo = Pipeline([
    ("escalado", StandardScaler()),       # tiene fit y transform
    ("regresion", LinearRegression()),    # tiene fit y predict
])
modelo.fit(X, y)
print("R² del pipeline:", round(modelo.score(X, y), 3))


class EscaladoPorMaximo:
    """Un transformador propio: no hereda de scikit-learn, solo cumple el contrato."""

    def fit(self, X, y=None) -> "EscaladoPorMaximo":
        self.maximos_ = np.abs(X).max(axis=0)
        return self                      # devolver self permite encadenar

    def transform(self, X):
        return X / self.maximos_


# Se cambia una pieza y el resto del programa sigue igual.
propio = Pipeline([
    ("escalado", EscaladoPorMaximo()),
    ("regresion", LinearRegression()),
])
propio.fit(X, y)
print("R² con el transformador propio:", round(propio.score(X, y), 3))

print("\nMétodos que exige cada sitio:")
print("  ProductoService  ->  guardar, buscar_por_codigo, buscar_todos, borrar, existe")
print("  Pipeline         ->  fit, transform  (y fit, predict en el último paso)")
