"""Crea las piezas y las conecta.

Es el único módulo que sabe qué implementación de repositorio se está usando.
Ejecútalo desde la carpeta `listados/`:

    python -m tienda.app
"""

from decimal import Decimal
from pathlib import Path

from tienda.formatos import FormatoJson
from tienda.modelo import Producto
from tienda.repositorio import ProductoRepositoryFichero, ProductoRepositoryMemoria
from tienda.servicio import ProductoService

RUTA_CATALOGO = Path("datos/catalogo.json")

CATALOGO_INICIAL = [
    Producto("T-100", "Teclado mecánico", Decimal("79.90"), 12),
    Producto("R-200", "Ratón inalámbrico", Decimal("24.50"), 30),
    Producto("M-300", "Monitor 27 pulgadas", Decimal("219.00"), 5),
]


def catalogo_nuevo() -> list[Producto]:
    """Devuelve copias de los productos de ejemplo, sin compartir objetos."""
    return [Producto(p.codigo, p.nombre, p.precio, p.stock) for p in CATALOGO_INICIAL]


def main() -> None:
    servicio = ProductoService(ProductoRepositoryMemoria())
    for producto in catalogo_nuevo():
        servicio.alta(producto)

    print("Catálogo en memoria:")
    for producto in servicio.listar():
        print(" ", producto)
    print("Valor del inventario:", servicio.valor_inventario(), "€")

    # La misma aplicación, cambiando solo el repositorio: ahora los datos persisten.
    RUTA_CATALOGO.unlink(missing_ok=True)
    en_fichero = ProductoService(ProductoRepositoryFichero(RUTA_CATALOGO, FormatoJson()))
    for producto in catalogo_nuevo():
        en_fichero.alta(producto)

    print(f"\nGuardado en {RUTA_CATALOGO}: {len(en_fichero.listar())} productos")
    print("Primeras líneas del fichero:")
    for linea in RUTA_CATALOGO.read_text(encoding="utf-8").splitlines()[:7]:
        print(" ", linea)


if __name__ == "__main__":
    main()
