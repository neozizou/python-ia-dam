"""Listado 6.1. La API de scikit-learn: fit, predict, score."""

from sklearn.linear_model import LinearRegression

# Ejemplo mínimo: predecir el importe a partir de las unidades
X = [[1], [2], [3], [4], [5]]      # características: siempre una tabla 2D
y = [25, 50, 74, 101, 124]         # objetivo: un vector

modelo = LinearRegression()
modelo.fit(X, y)                   # 1. aprender de los datos

print(modelo.predict([[6], [10]])) # 2. predecir datos nuevos
print(round(modelo.score(X, y), 4))# 3. evaluar (R² en regresión)
print(f"pendiente={modelo.coef_[0]:.2f}  ordenada={modelo.intercept_:.2f}")
