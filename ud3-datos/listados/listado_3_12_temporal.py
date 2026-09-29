"""Listado 3.12. Series temporales: agrupar por periodos y medias móviles."""

from comun import cargar_ventas

ventas = cargar_ventas()

# Con la fecha como índice se puede remuestrear: ME = fin de mes, W = semana
serie = ventas.set_index("fecha")["importe"]

mensual = serie.resample("ME").sum().round(2)
print(mensual)

print("\nMedia móvil de 3 meses:")
print(mensual.rolling(window=3).mean().round(2).tail(6))

print("\nVariación respecto al mes anterior (%):")
print((mensual.pct_change() * 100).round(1).tail(6))
