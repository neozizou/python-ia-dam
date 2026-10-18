"""Agrupar, agregar, ordenar y buscar el máximo, solo con Python.

Son las cuatro operaciones que hace cualquier análisis de datos. En la UD3 cada
una será una línea de pandas; hacerlas ahora a mano es lo que te permitirá
entender después qué está haciendo pandas por dentro, y detectar cuándo hace
algo distinto de lo que creías.
"""

JUGADORES = [
    {"nombre": "L. Messi", "pais": "Argentina", "media": 94, "valor": 95_500_000},
    {"nombre": "Cristiano Ronaldo", "pais": "Portugal", "media": 93, "valor": 58_500_000},
    {"nombre": "J. Oblak", "pais": "Slovenia", "media": 91, "valor": 77_500_000},
    {"nombre": "K. De Bruyne", "pais": "Belgium", "media": 91, "valor": 90_000_000},
    {"nombre": "E. Hazard", "pais": "Belgium", "media": 91, "valor": 90_000_000},
    {"nombre": "Sergio Ramos", "pais": "Spain", "media": 89, "valor": 34_500_000},
    {"nombre": "De Gea", "pais": "Spain", "media": 89, "valor": 45_000_000},
    {"nombre": "Sergio Busquets", "pais": "Spain", "media": 87, "valor": 29_500_000},
]

# 1. AGRUPAR Y AGREGAR: sumar el valor de cada país.
valor_por_pais: dict[str, int] = {}
for jugador in JUGADORES:
    pais = jugador["pais"]
    valor_por_pais[pais] = valor_por_pais.get(pais, 0) + jugador["valor"]

# 2. ORDENAR: de mayor a menor, por el valor acumulado.
print("Valor total de la selección, por país:")
for pais, total in sorted(valor_por_pais.items(), key=lambda par: par[1], reverse=True):
    print(f"  {pais:<10} {total / 1_000_000:>6.1f} M€")

# 3. AGREGAR OTRA COSA: la media de `media` por país necesita suma y recuento.
suma: dict[str, int] = {}
cuantos: dict[str, int] = {}
for jugador in JUGADORES:
    pais = jugador["pais"]
    suma[pais] = suma.get(pais, 0) + jugador["media"]
    cuantos[pais] = cuantos.get(pais, 0) + 1

print("\nMedia de valoración por país:")
for pais in sorted(suma):
    plural = "jugador" if cuantos[pais] == 1 else "jugadores"
    print(f"  {pais:<10} {suma[pais] / cuantos[pais]:.1f}  ({cuantos[pais]} {plural})")

# 4. BUSCAR EL MÁXIMO: `max` con `key` evita escribir el bucle.
mas_caro = max(JUGADORES, key=lambda j: j["valor"])
print(f"\nEl más caro: {mas_caro['nombre']} ({mas_caro['valor'] / 1_000_000:.1f} M€)")

# Y el más caro de cada país, en una sola comprensión de diccionario.
mejor_por_pais = {
    pais: max((j for j in JUGADORES if j["pais"] == pais), key=lambda j: j["valor"])["nombre"]
    for pais in valor_por_pais
}
print("El más caro de cada país:", mejor_por_pais)
