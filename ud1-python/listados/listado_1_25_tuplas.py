"""Listado 1.25. Empaquetado y desempaquetado."""

punto = (37.18, -3.60)          # latitud y longitud
lat, lon = punto                # desempaquetado
print(lat, lon)

primero, *resto = [10, 20, 30, 40]
print(primero, resto)           # 10 [20, 30, 40]
