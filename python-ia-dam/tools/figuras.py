"""Utilidades para dibujar las figuras SVG de los apuntes.

Todas las figuras comparten paleta, tipografía y fondo claro propio, para que
se lean igual en GitHub y en el sitio web, tanto en modo claro como oscuro.
"""

from html import escape

# Paleta
TINTA = "#1f2430"
SUAVE = "#5b6472"
BORDE = "#c7cedb"
FONDO = "#ffffff"
PANEL = "#f4f6fa"
AZUL = "#2f6fd0"
AZUL_CLARO = "#dbe8fb"
VERDE = "#1f9d6b"
VERDE_CLARO = "#d8f1e6"
NARANJA = "#d9822b"
NARANJA_CLARO = "#fbe9d4"
ROJO = "#c0392b"
ROJO_CLARO = "#fadbd8"
MORADO = "#7b55c0"
MORADO_CLARO = "#e8dffa"
GRIS = "#8b95a6"
GRIS_CLARO = "#e8ecf3"

FUENTE = "ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'SF Mono', 'Cascadia Mono', Consolas, 'Liberation Mono', monospace"


class Figura:
    """Lienzo SVG con operaciones de dibujo sencillas."""

    def __init__(self, ancho: int, alto: int, titulo: str):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.partes: list[str] = []

    # --- primitivas ---------------------------------------------------
    def caja(self, x, y, an, al, relleno=FONDO, borde=BORDE, radio=10, grosor=1.5,
             guiones=None):
        guion = f' stroke-dasharray="{guiones}"' if guiones else ""
        self.partes.append(
            f'<rect x="{x}" y="{y}" width="{an}" height="{al}" rx="{radio}" '
            f'fill="{relleno}" stroke="{borde}" stroke-width="{grosor}"{guion}/>'
        )

    def texto(self, x, y, contenido, tam=14, color=TINTA, anclaje="start", peso="400",
              mono=False, cursiva=False):
        familia = MONO if mono else FUENTE
        estilo = ' font-style="italic"' if cursiva else ""
        self.partes.append(
            f'<text x="{x}" y="{y}" font-family="{familia}" font-size="{tam}" '
            f'fill="{color}" text-anchor="{anclaje}" font-weight="{peso}"{estilo}>'
            f'{escape(contenido)}</text>'
        )

    def linea(self, x1, y1, x2, y2, color=BORDE, grosor=1.5, guiones=None):
        guion = f' stroke-dasharray="{guiones}"' if guiones else ""
        self.partes.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{grosor}"{guion}/>'
        )

    def flecha(self, x1, y1, x2, y2, color=SUAVE, grosor=2, guiones=None, curva=None):
        guion = f' stroke-dasharray="{guiones}"' if guiones else ""
        if curva is None:
            d = f"M {x1} {y1} L {x2} {y2}"
        else:
            d = f"M {x1} {y1} Q {curva[0]} {curva[1]} {x2} {y2}"
        self.partes.append(
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"'
            f'{guion} marker-end="url(#punta)"/>'
        )

    def circulo(self, cx, cy, r, relleno=FONDO, borde=BORDE, grosor=1.5, opacidad=1.0):
        self.partes.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{relleno}" stroke="{borde}" '
            f'stroke-width="{grosor}" fill-opacity="{opacidad}"/>'
        )

    def ruta(self, d, relleno="none", borde=SUAVE, grosor=2, guiones=None, punta=False):
        guion = f' stroke-dasharray="{guiones}"' if guiones else ""
        marca = ' marker-end="url(#punta)"' if punta else ""
        self.partes.append(
            f'<path d="{d}" fill="{relleno}" stroke="{borde}" stroke-width="{grosor}"'
            f'{guion}{marca}/>'
        )

    # --- compuestos ---------------------------------------------------
    def etiqueta(self, x, y, an, al, titulo, color_borde, color_relleno, tam=14,
                 mono=True, peso="500"):
        """Caja con una línea de texto centrada."""
        self.caja(x, y, an, al, relleno=color_relleno, borde=color_borde)
        self.texto(x + an / 2, y + al / 2 + tam / 3, titulo, tam=tam, anclaje="middle",
                   mono=mono, peso=peso)

    def encabezado(self, x, y, texto, tam=15):
        self.texto(x, y, texto, tam=tam, peso="700", color=TINTA)

    def nota(self, x, y, texto, tam=12.5, color=SUAVE, anclaje="start", mono=False):
        self.texto(x, y, texto, tam=tam, color=color, anclaje=anclaje, mono=mono)

    # --- salida -------------------------------------------------------
    def svg(self) -> str:
        cuerpo = "\n  ".join(self.partes)
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.ancho} {self.alto}" \
width="{self.ancho}" height="{self.alto}" role="img" aria-label="{escape(self.titulo)}">
  <title>{escape(self.titulo)}</title>
  <defs>
    <marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
            markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{SUAVE}"/>
    </marker>
  </defs>
  <rect width="{self.ancho}" height="{self.alto}" rx="14" fill="{FONDO}" stroke="{BORDE}"/>
  {cuerpo}
</svg>
"""

    def guardar(self, ruta) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(self.svg(), encoding="utf-8")
