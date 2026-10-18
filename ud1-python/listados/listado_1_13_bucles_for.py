"""Listado 1.13. Las tres formas de recorrer con for."""

jugadores = ["L. Messi", "J. Oblak", "K. De Bruyne"]
medias = [94, 91, 91]

for jugador in jugadores:                          # 1. elemento a elemento
    print(jugador)

print()
for i, jugador in enumerate(jugadores, start=1):   # 2. con su posición
    print(f"{i}. {jugador}")

print()
for jugador, media in zip(jugadores, medias):      # 3. dos secuencias en paralelo
    print(f"{jugador:<14} {media}")

print()
for numero in range(3):                            # 4. un número de veces
    print("Vuelta", numero)
