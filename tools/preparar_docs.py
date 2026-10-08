"""Prepara la carpeta docs/ que MkDocs convierte en el sitio web.

Los apuntes viven junto a su código, en ud1-python/, ud2-poo/, etc., porque así
son cómodos de mantener y de leer en GitHub. Para el sitio web hace falta una
carpeta única, así que este script copia cada fichero a docs/ y reescribe los
enlaces:

- los enlaces entre páginas del sitio pasan a su nueva ruta;
- los enlaces a ficheros de código apuntan a GitHub, donde se pueden leer y
  descargar.

    python tools/preparar_docs.py
"""

import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
REPOSITORIO = "https://github.com/neozizou/python-ia-dam/blob/main"

# origen -> destino dentro de docs/
PAGINAS = {
    "README.md": "index.md",
    "ud1-python/UD1-python-para-quien-ya-programa.md": "ud1.md",
    "ud2-poo/UD2-programacion-orientada-a-objetos.md": "ud2.md",
    "ud3-datos/UD3-analisis-de-datos.md": "ud3.md",
    "ud4-bd/UD4-sql-y-nosql.md": "ud4.md",
    "ud5-bigdata/UD5-big-data.md": "ud5.md",
    "ud6-ml/UD6-machine-learning.md": "ud6.md",
    "ud7-proyecto/UD7-proyecto-y-despliegue.md": "ud7.md",
    "ud7-proyecto/plantillas/ficha-modelo.md": "plantillas/ficha-modelo.md",
    "ud7-proyecto/plantillas/checklist-despliegue.md": "plantillas/checklist-despliegue.md",
    "ud7-proyecto/proyecto-ejemplo/README.md": "proyecto-ejemplo.md",
}

# Enlaces entre páginas: cómo aparecen en los apuntes -> a dónde deben ir
ENLACES_INTERNOS = {
    "../README.md": "index.md",
    # pie de navegación de cada unidad (rutas vistas desde la carpeta udN-…)
    "../ud1-python/UD1-python-para-quien-ya-programa.md": "ud1.md",
    "../ud2-poo/UD2-programacion-orientada-a-objetos.md": "ud2.md",
    "../ud3-datos/UD3-analisis-de-datos.md": "ud3.md",
    "../ud4-bd/UD4-sql-y-nosql.md": "ud4.md",
    "../ud5-bigdata/UD5-big-data.md": "ud5.md",
    "../ud6-ml/UD6-machine-learning.md": "ud6.md",
    "../ud7-proyecto/UD7-proyecto-y-despliegue.md": "ud7.md",
    # índice del módulo (rutas vistas desde la raíz)
    "ud1-python/UD1-python-para-quien-ya-programa.md": "ud1.md",
    "ud2-poo/UD2-programacion-orientada-a-objetos.md": "ud2.md",
    "ud3-datos/UD3-analisis-de-datos.md": "ud3.md",
    "ud4-bd/UD4-sql-y-nosql.md": "ud4.md",
    "ud5-bigdata/UD5-big-data.md": "ud5.md",
    "ud6-ml/UD6-machine-learning.md": "ud6.md",
    "ud7-proyecto/UD7-proyecto-y-despliegue.md": "ud7.md",
    "plantillas/ficha-modelo.md": "plantillas/ficha-modelo.md",
    "plantillas/checklist-despliegue.md": "plantillas/checklist-despliegue.md",
    "proyecto-ejemplo/README.md": "proyecto-ejemplo.md",
}

PATRON_IMAGEN = re.compile(r"!\[([^\]]*)\]\((?!https?://)([^)]+)\)")
PATRON_ENLACE = re.compile(r"(?<!!)\[([^\]]+)\]\((?!https?://)([^)]+)\)")


def copiar_figuras(origen: str) -> str:
    """Copia las figuras de la unidad a docs/figuras/<unidad>/ y devuelve su carpeta."""
    carpeta_origen = Path(origen).parent
    figuras = RAIZ / carpeta_origen / "figuras"
    if not figuras.is_dir():
        return ""
    unidad = carpeta_origen.name
    destino = DOCS / "figuras" / unidad
    destino.mkdir(parents=True, exist_ok=True)
    for figura in figuras.glob("*.svg"):
        shutil.copy2(figura, destino / figura.name)
    return f"figuras/{unidad}"


def reescribir(texto: str, origen: str, destino: str) -> str:
    """Devuelve el Markdown con los enlaces y las imágenes adaptados al sitio web."""
    carpeta_origen = Path(origen).parent
    profundidad = len(Path(destino).parts) - 1        # páginas dentro de subcarpetas
    carpeta_figuras = copiar_figuras(origen)

    def sustituir_imagen(coincidencia: re.Match) -> str:
        alternativo, ruta = coincidencia.group(1), coincidencia.group(2)
        nombre = Path(ruta).name
        prefijo = "../" * profundidad
        return f"![{alternativo}]({prefijo}{carpeta_figuras}/{nombre})"

    texto = PATRON_IMAGEN.sub(sustituir_imagen, texto)

    def sustituir(coincidencia: re.Match) -> str:
        etiqueta, ruta = coincidencia.group(1), coincidencia.group(2)
        camino, _, ancla = ruta.partition("#")

        if not camino:                                # enlace interno de la página
            return f"[{etiqueta}]({ruta})"

        if camino in ENLACES_INTERNOS:
            nueva = ENLACES_INTERNOS[camino]
            prefijo = "../" * profundidad
            return f"[{etiqueta}]({prefijo}{nueva}{'#' + ancla if ancla else ''})"

        # Cualquier otra cosa (código, datos, carpetas) se lee en GitHub
        objetivo = (carpeta_origen / camino).as_posix().replace("/./", "/")
        return f"[{etiqueta}]({REPOSITORIO}/{objetivo})"

    return PATRON_ENLACE.sub(sustituir, texto)


def copiar_hojas_de_estilo() -> None:
    """Copia sitio/stylesheets/ a docs/, que es donde MkDocs busca extra_css."""
    origen = RAIZ / "sitio" / "stylesheets"
    if origen.is_dir():
        shutil.copytree(origen, DOCS / "stylesheets")


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    copiar_hojas_de_estilo()

    for origen, destino in PAGINAS.items():
        ruta_origen = RAIZ / origen
        ruta_destino = DOCS / destino
        ruta_destino.parent.mkdir(parents=True, exist_ok=True)
        ruta_destino.write_text(
            reescribir(ruta_origen.read_text(encoding="utf-8"), origen, destino),
            encoding="utf-8",
        )
        print(f"{origen}  ->  docs/{destino}")

    print(f"\n{len(PAGINAS)} páginas preparadas en {DOCS}")


if __name__ == "__main__":
    main()
