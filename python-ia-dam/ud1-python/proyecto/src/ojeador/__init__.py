"""Ojeador: consultas rápidas sobre el fichero de jugadores del curso.

Un paquete pequeño, de dos módulos, para ver cómo se organiza el código en
Python. Lo que exporta aquí es su **interfaz pública**: lo que puede usar quien
importe el paquete sin tener que saber cómo está organizado por dentro.
"""

from .lectura import leer_edicion
from .consultas import mas_caros, media_por_pais

__all__ = ["leer_edicion", "mas_caros", "media_por_pais"]
