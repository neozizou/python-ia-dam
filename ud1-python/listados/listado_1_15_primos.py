"""Listado 1.15. Números primos con for … else (adaptado del tutorial oficial)."""

for n in range(2, 20):
    for divisor in range(2, n):
        if n % divisor == 0:
            break              # tiene un divisor: no es primo
    else:
        print(n, "es primo")   # el for interno terminó sin break
