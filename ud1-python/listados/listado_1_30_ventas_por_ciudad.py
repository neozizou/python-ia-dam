"""Listado 1.30. Ventas por ciudad con Python puro."""

ventas = [
    {"ciudad": "Granada", "producto": "portátil", "unidades": 3, "precio": 899.90},
    {"ciudad": "Málaga", "producto": "ratón", "unidades": 10, "precio": 12.50},
    {"ciudad": "Granada", "producto": "monitor", "unidades": 2, "precio": 180.00},
    {"ciudad": "Sevilla", "producto": "portátil", "unidades": 1, "precio": 899.90},
    {"ciudad": "Málaga", "producto": "monitor", "unidades": 4, "precio": 180.00},
]

# Acumular el importe por ciudad
total_por_ciudad = {}
for v in ventas:
    importe = v["unidades"] * v["precio"]
    total_por_ciudad[v["ciudad"]] = total_por_ciudad.get(v["ciudad"], 0) + importe

# Mostrar de mayor a menor
for ciudad, total in sorted(total_por_ciudad.items(), key=lambda par: par[1], reverse=True):
    print(f"{ciudad:<8} {total:>9.2f} €")

# Granada    3059.70 €
# Sevilla     899.90 €
# Málaga      845.00 €

# La venta de mayor importe
mejor = max(ventas, key=lambda v: v["unidades"] * v["precio"])
print(mejor)
