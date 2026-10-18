"""Punto de entrada del paquete: python -m ojeador"""

from . import leer_edicion, mas_caros, media_por_pais

EDICION = 2020


def main() -> None:
    jugadores = leer_edicion(EDICION)
    print(f"FIFA {EDICION}: {len(jugadores):,} jugadores\n")

    print("Los cinco más caros:")
    for jugador in mas_caros(jugadores):
        print(f"  {jugador['short_name']:<20} {jugador['club']:<22} "
              f"{jugador['value_eur'] / 1_000_000:>6.1f} M€")

    medias = media_por_pais(jugadores)
    mejores = sorted(medias.items(), key=lambda par: par[1], reverse=True)[:5]
    print(f"\nMedia más alta, entre los {len(medias)} países con 100 jugadores o más:")
    for pais, media in mejores:
        print(f"  {pais:<16} {media}")


if __name__ == "__main__":
    main()
