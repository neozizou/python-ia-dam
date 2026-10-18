"""Listado 6.5. Fuga de datos: escalar antes de dividir es hacer trampa."""

import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler

from comun import cargar

ventas = cargar()
X = ventas[["precio", "descuento", "mes"]]
y = ventas["unidades"]

# MAL: el escalador ve TODOS los datos, incluidos los de prueba
escalador = StandardScaler()
X_todo_escalado = escalador.fit_transform(X)
_, X_prueba_mal, _, _ = train_test_split(X_todo_escalado, y, test_size=0.2, random_state=42)
print("Media aprendida con todos los datos:", escalador.mean_.round(3))

# BIEN: el escalador aprende solo del entrenamiento
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2,
                                                            random_state=42)
escalador_correcto = StandardScaler().fit(X_entrena)
print("Media aprendida solo con entrenamiento:", escalador_correcto.mean_.round(3))

print("\nLa diferencia es pequeña aquí, pero con imputaciones, selección de")
print("variables o datos temporales puede inflar mucho el resultado.")
print("Regla: cualquier paso que APRENDA algo va dentro del Pipeline.")
