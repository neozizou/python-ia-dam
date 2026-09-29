"""Convierte las alertas de GitHub en avisos de MkDocs Material.

En GitHub se escribe:

    > [!TIP]
    > **Buena práctica.** ...

y MkDocs Material espera:

    !!! tip
        **Buena práctica.** ...

Este hook hace la traducción al construir el sitio, para que los apuntes se
vean bien en los dos sitios sin escribirlos dos veces.
"""

import re

TIPOS = {
    "NOTE": "note",
    "TIP": "tip",
    "IMPORTANT": "info",
    "WARNING": "warning",
    "CAUTION": "danger",
}

PATRON = re.compile(
    r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*\n((?:^>.*\n?)*)",
    re.MULTILINE,
)


def _convertir(coincidencia: re.Match) -> str:
    tipo = TIPOS[coincidencia.group(1)]
    cuerpo = coincidencia.group(2)
    lineas = [linea[2:] if linea.startswith("> ") else linea.lstrip(">")
              for linea in cuerpo.splitlines()]
    sangrado = "\n".join(f"    {linea}".rstrip() for linea in lineas)
    return f'!!! {tipo}\n{sangrado}\n'


def on_page_markdown(markdown: str, **kwargs) -> str:
    """MkDocs llama a esta función con el Markdown de cada página."""
    return PATRON.sub(_convertir, markdown)
