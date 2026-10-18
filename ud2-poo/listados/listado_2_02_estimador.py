"""Un estimador de scikit-learn: parámetros al construir, atributos al aprender.

El convenio es constante en toda la biblioteca: lo que tú decides va en el
constructor; lo que el objeto aprende aparece después, con un guion bajo final.
"""

from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor

X, y = make_regression(n_samples=200, n_features=4, noise=10.0, random_state=42)

# Parámetros: decisiones tuyas, disponibles desde el primer momento.
bosque = RandomForestRegressor(n_estimators=50, max_depth=4, random_state=42)
print("n_estimators:", bosque.n_estimators)
print("max_depth:   ", bosque.max_depth)

# Antes de entrenar, lo aprendido todavía no existe.
print("\n¿Tiene feature_importances_ antes de fit?", hasattr(bosque, "feature_importances_"))

bosque.fit(X, y)

# Después de fit: atributos nuevos, todos terminados en guion bajo.
aprendidos = [n for n in vars(bosque) if n.endswith("_") and not n.startswith("_")]
print("¿Y después?                              ", hasattr(bosque, "feature_importances_"))
print("Atributos aprendidos:", sorted(aprendidos))
print("Importancia de cada variable:", bosque.feature_importances_.round(3))
