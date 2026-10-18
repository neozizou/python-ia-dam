"""Genera la figura 3.5 de la UD3 a partir de los datos reales.

Es la única figura del repositorio que no dibuja `tools/generar_figuras.py`:
las demás son esquemas y esta es un gráfico de verdad, hecho con matplotlib
sobre `datos-comunes/jugadores.csv`. Los puntos van rasterizados dentro del
SVG para que el fichero no pase de unos pocos cientos de kilobytes.

Uso:
    python tools/generar_dispersion.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "ud3-datos" / "listados"))

from comun import cargar_limpio  # noqa: E402

DESTINO = RAIZ / "ud3-datos" / "figuras" / "dispersion-ejemplo.svg"
TITULO = "Dos gráficos de dispersión: edad frente a valoración y valoración frente a valor de mercado"

TINTA = "#1f2430"
SUAVE = "#5b6472"
BORDE = "#c7cedb"
AZUL = "#2f6fd0"


def estilo() -> None:
    """Deja los gráficos con los mismos colores que el resto de figuras."""
    plt.rcParams.update(
        {
            "font.size": 9,
            "font.family": "DejaVu Sans",
            "text.color": TINTA,
            "axes.labelcolor": TINTA,
            "axes.edgecolor": BORDE,
            "xtick.color": SUAVE,
            "ytick.color": SUAVE,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "svg.fonttype": "none",
        }
    )


def anadir_titulo(ruta: Path, titulo: str) -> None:
    """Inserta un <title> en el SVG, que es su texto alternativo."""
    contenido = ruta.read_text(encoding="utf-8")
    cierre = contenido.index(">", contenido.index("<svg")) + 1
    marca = f"\n <title>{titulo}</title>"
    ruta.write_text(contenido[:cierre] + marca + contenido[cierre:], encoding="utf-8")


def main() -> None:
    estilo()
    sol = cargar_limpio(edicion=2020)
    con_valor = sol.dropna(subset=["value_eur"])

    figura, (izq, der) = plt.subplots(1, 2, figsize=(9.2, 3.6))

    izq.scatter(sol["age"], sol["overall"], s=4, alpha=0.15, color=AZUL, rasterized=True)
    izq.set_title("Edad y valoración", color=TINTA, fontsize=10.5)
    izq.set_xlabel("Edad (años)")
    izq.set_ylabel("Valoración media (overall)")

    der.scatter(
        con_valor["overall"], con_valor["value_eur"], s=4, alpha=0.15, color=AZUL, rasterized=True
    )
    der.set_yscale("log")
    der.set_title("Valoración y valor de mercado", color=TINTA, fontsize=10.5)
    der.set_xlabel("Valoración media (overall)")
    der.set_ylabel("Valor de mercado (€, escala log.)")

    for ejes in (izq, der):
        ejes.grid(alpha=0.25, color=BORDE)
        ejes.set_axisbelow(True)
        for lado in ("top", "right"):
            ejes.spines[lado].set_visible(False)

    figura.tight_layout()
    figura.savefig(DESTINO, dpi=150, format="svg")
    plt.close(figura)
    anadir_titulo(DESTINO, TITULO)

    print(f"{DESTINO.relative_to(RAIZ)}  ({DESTINO.stat().st_size / 1024:.1f} KB)")
    print(f"  {len(sol):,} jugadores · {len(con_valor):,} con valor de mercado")


if __name__ == "__main__":
    main()
