"""Listado 6.15. Aprendizaje no supervisado: agrupar sin etiquetas."""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from comun import cargar

ventas = cargar()
X = ventas[["precio", "unidades", "descuento"]]

# k-means SIEMPRE necesita escalado: trabaja con distancias
print("k  inercia   silueta")
for k in range(2, 7):
    modelo = Pipeline([("escalado", StandardScaler()),
                       ("kmeans", KMeans(n_clusters=k, n_init=10, random_state=42))])
    etiquetas = modelo.fit_predict(X)
    inercia = modelo.named_steps["kmeans"].inertia_
    print(f"{k}  {inercia:8.0f}   {silhouette_score(X, etiquetas):.3f}")

modelo = Pipeline([("escalado", StandardScaler()),
                   ("kmeans", KMeans(n_clusters=3, n_init=10, random_state=42))])
ventas["grupo"] = modelo.fit_predict(X)

print("\nPerfil de cada grupo:")
print(ventas.groupby("grupo")[["precio", "unidades", "descuento"]].mean().round(2))
print("\nProducto dominante en cada grupo:")
print(ventas.groupby("grupo")["producto"].agg(lambda s: s.value_counts().idxmax()))
