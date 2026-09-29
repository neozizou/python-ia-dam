"""Listado 3.18. De los datos a la decisión."""

from comun import cargar_ventas

ventas = cargar_ventas()
total = ventas["importe"].sum()

# 1. Concentración de clientes: ¿el 20 % aporta el 80 %?
por_cliente = ventas.groupby("cliente")["importe"].sum().sort_values(ascending=False)
top20 = por_cliente.head(int(len(por_cliente) * 0.2))
print(f"{len(top20)} clientes ({len(top20) / len(por_cliente):.0%}) aportan "
      f"{top20.sum() / total:.0%} de la facturación")

# 2. Mejor y peor mes
mensual = ventas.groupby("mes")["importe"].sum()
print(f"Mejor mes: {mensual.idxmax()} ({mensual.max():,.0f} €)")
print(f"Peor mes:  {mensual.idxmin()} ({mensual.min():,.0f} €)")

# 3. Producto que más factura frente al que más se vende
por_producto = ventas.groupby("producto").agg(
    importe=("importe", "sum"), unidades=("unidades", "sum")
)
print(f"Más factura: {por_producto['importe'].idxmax()}")
print(f"Más unidades: {por_producto['unidades'].idxmax()}")

# 4. Cuota de cada canal
cuota = (ventas.groupby("canal")["importe"].sum() / total * 100).round(1)
print("\nCuota por canal (%):")
print(cuota.sort_values(ascending=False))
