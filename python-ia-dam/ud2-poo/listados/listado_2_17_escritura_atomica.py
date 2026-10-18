"""Por qué el repositorio en fichero escribe primero en un temporal.

Si el programa se interrumpe a mitad de la escritura, el catálogo entero se
pierde. Escribiendo en un fichero aparte y moviéndolo después, o está el
contenido viejo o está el nuevo, pero nunca medio fichero.
"""

from pathlib import Path

RUTA = Path("datos/catalogo_atomico.json")
VIEJO = '[{"codigo": "T-100"}]'
NUEVO = '[{"codigo": "T-100"}, {"codigo": "R-200"}]'

RUTA.parent.mkdir(parents=True, exist_ok=True)


def escribir_mal(ruta: Path, contenido: str) -> None:
    """Abre el fichero de destino y lo vacía antes de tener el contenido nuevo."""
    with ruta.open("w", encoding="utf-8") as fichero:
        fichero.write(contenido[:10])
        raise RuntimeError("corte de luz")


def escribir_bien(ruta: Path, contenido: str) -> None:
    """Escribe en un temporal y lo mueve de un solo paso."""
    temporal = ruta.with_name(ruta.name + ".tmp")
    try:
        temporal.write_text(contenido, encoding="utf-8")
        raise RuntimeError("corte de luz")
        temporal.replace(ruta)            # no se llega aquí: el original sigue intacto
    finally:
        temporal.unlink(missing_ok=True)


RUTA.write_text(VIEJO, encoding="utf-8")
try:
    escribir_mal(RUTA, NUEVO)
except RuntimeError:
    print("Tras fallar escribiendo encima:", RUTA.read_text(encoding="utf-8"))

RUTA.write_text(VIEJO, encoding="utf-8")
try:
    escribir_bien(RUTA, NUEVO)
except RuntimeError:
    print("Tras fallar con temporal:      ", RUTA.read_text(encoding="utf-8"))

print("¿Queda basura en la carpeta?", sorted(p.name for p in RUTA.parent.glob("*.tmp")) or "no")
RUTA.unlink()
