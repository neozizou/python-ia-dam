"""Listado 1.10. Procesar y formatear una línea de datos."""

linea = "  L. Messi;FC Barcelona;94;95500000 \n"

nombre, club, media, valor = linea.strip().split(";")
media = int(media)                     # todo lo que llega como texto hay que convertirlo
valor = int(valor)

print(f"{nombre:<12} {club:<16} media {media:>3}  {valor / 1_000_000:>6.1f} M€")
# L. Messi     FC Barcelona     media  94    95.5 M€
