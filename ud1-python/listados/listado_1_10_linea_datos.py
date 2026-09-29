"""Listado 1.10. Procesar y formatear una línea de datos."""

linea = "  Portátil;899.90;12 \n"

nombre, precio, stock = linea.strip().split(";")
precio = float(precio)
stock = int(stock)

print(f"{nombre:<10} {precio:>8.2f} € x {stock:>3} = {precio * stock:>9.2f} €")
# Portátil     899.90 € x  12 =  10798.80 €
