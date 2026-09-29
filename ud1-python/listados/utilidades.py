"""Listado 1.39. utilidades.py: módulo con autoprueba.

Funciones de texto reutilizables.
"""


def normalizar(texto: str) -> str:
    """Quita espacios sobrantes y pasa a minúsculas."""
    return " ".join(texto.split()).lower()


if __name__ == "__main__":
    # Solo se ejecuta con: python utilidades.py
    assert normalizar("  Hola   MUNDO ") == "hola mundo"
    print("Pruebas superadas")
