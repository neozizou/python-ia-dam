"""Listado 1.37. Validar con raise."""


def validar_media(media: int) -> int:
    """Devuelve la media si está entre 1 y 99; si no, lanza ValueError."""
    if not 1 <= media <= 99:
        raise ValueError(f"Media fuera de rango: {media}")
    return media


print(validar_media(94))
try:
    validar_media(120)
except ValueError as e:
    print("Error:", e)      # Error: Media fuera de rango: 120
