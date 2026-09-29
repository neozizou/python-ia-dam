"""Listado 6.3. Escalar números y codificar categorías."""

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from comun import cargar

ventas = cargar()

# 1. Escalado: media 0 y desviación 1. Necesario en modelos con distancias o pesos
escalador = StandardScaler()
numericas = escalador.fit_transform(ventas[["precio", "descuento"]])
print(pd.DataFrame(numericas, columns=["precio", "descuento"]).describe().round(2).loc[["mean", "std"]])

# 2. Codificación: una columna 0/1 por categoría. Los modelos no entienden texto
codificador = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
categorias = codificador.fit_transform(ventas[["canal"]])
print(codificador.get_feature_names_out())
print(categorias[:3])

# handle_unknown="ignore" evita que el modelo falle si mañana aparece un canal nuevo
