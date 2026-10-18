"""Listado 1.29. Comprensiones de lista, diccionario y conjunto."""

cuadrados = [n ** 2 for n in range(1, 6)]            # [1, 4, 9, 16, 25]
pares = [n for n in range(20) if n % 2 == 0]         # con filtro
print(cuadrados, pares)

precios = {"teclado": 25.0, "ratón": 12.5, "monitor": 180.0}
con_iva = {p: round(v * 1.21, 2) for p, v in precios.items()}
caros = [p for p, v in precios.items() if v > 20]    # ['teclado', 'monitor']
print(con_iva, caros)

iniciales = {nombre[0] for nombre in ["Ana", "Alberto", "Eva"]}   # {'A', 'E'}
print(iniciales)
