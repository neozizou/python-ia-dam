"""Listado 3.16. Análisis exploratorio: una variable cada vez."""

from comun import cargar_ventas

ventas = cargar_ventas()

# Numéricas: centro, dispersión y forma
print(ventas["importe"].describe().round(2))
print("mediana:", ventas["importe"].median().round(2))
print("asimetría:", ventas["importe"].skew().round(2))

# La media es mucho mayor que la mediana: la cola de importes altos tira de ella
print("\nPercentiles:")
print(ventas["importe"].quantile([0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).round(2))

# Categóricas: frecuencias absolutas y relativas
print("\nCanal:")
print(ventas["canal"].value_counts())
print((ventas["canal"].value_counts(normalize=True) * 100).round(1))
