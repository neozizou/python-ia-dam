"""Listado 1.13. Las cuatro formas habituales de for."""

ciudades = ["Granada", "Málaga", "Sevilla"]
temperaturas = [21.5, 24.0, 27.3]

for ciudad in ciudades:                          # 1. elemento a elemento
    print(ciudad)

for i, ciudad in enumerate(ciudades, start=1):   # 2. con su posición
    print(f"{i}. {ciudad}")

for ciudad, t in zip(ciudades, temperaturas):    # 3. dos secuencias en paralelo
    print(f"{ciudad}: {t} °C")

for n in range(10, 0, -2):                       # 4. una secuencia de enteros
    print(n, end=" ")                            # 10 8 6 4 2
print()
