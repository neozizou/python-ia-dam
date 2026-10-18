"""Listado 1.14. Validar una entrada hasta que sea correcta."""

while True:
    texto = input("Edad (0-120): ")
    if texto.isdigit() and 0 <= int(texto) <= 120:
        break
    print("Valor no válido, inténtalo de nuevo.")

edad = int(texto)
print(f"Edad registrada: {edad}")
