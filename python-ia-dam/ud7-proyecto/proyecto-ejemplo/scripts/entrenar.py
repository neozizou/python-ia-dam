"""Entrena el modelo definitivo y guarda el resultado.

    python scripts/entrenar.py
"""

import logging

from ventas_ia import cargar_limpio, entrenar, metricas, metricas_por_grupo
from ventas_ia.modelo import guardar

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main() -> None:
    ventas = cargar_limpio()
    modelo, X_prueba, y_prueba = entrenar(ventas)
    prediccion = modelo.predict(X_prueba)

    resultados = metricas(y_prueba, prediccion)
    print("Métricas en el conjunto de prueba:", resultados)
    print("\nError por producto:")
    print(metricas_por_grupo(X_prueba, y_prueba, prediccion, "producto"))

    guardar(modelo, resultados)
    print("\nModelo guardado en modelos/modelo.joblib")


if __name__ == "__main__":
    main()
