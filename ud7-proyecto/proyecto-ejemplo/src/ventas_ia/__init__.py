"""Proyecto integrador: análisis y predicción de ventas.

La interfaz pública del paquete es lo único que usan la aplicación y los scripts.
"""

from .datos import cargar_limpio
from .modelo import CARACTERISTICAS, OBJETIVO, cargar_modelo, construir_pipeline, entrenar
from .evaluacion import metricas, metricas_por_grupo

__all__ = [
    "cargar_limpio",
    "construir_pipeline",
    "entrenar",
    "cargar_modelo",
    "metricas",
    "metricas_por_grupo",
    "CARACTERISTICAS",
    "OBJETIVO",
]
