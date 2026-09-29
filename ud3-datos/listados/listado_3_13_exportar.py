"""Listado 3.13. Guardar los resultados."""

from pathlib import Path

from comun import cargar_ventas

ventas = cargar_ventas()
resumen = (
    ventas.groupby("ciudad")
    .agg(ventas=("id_venta", "count"), importe=("importe", "sum"))
    .round(2)
    .sort_values("importe", ascending=False)
)

salida = Path("salida")
salida.mkdir(exist_ok=True)

resumen.to_csv(salida / "resumen_ciudades.csv", sep=";", decimal=",", encoding="utf-8")
resumen.to_excel(salida / "resumen_ciudades.xlsx")          # necesita openpyxl
resumen.to_json(salida / "resumen_ciudades.json", indent=2, force_ascii=False)
ventas.to_parquet(salida / "ventas_limpias.parquet")        # formato columnar comprimido

for fichero in sorted(salida.iterdir()):
    print(f"{fichero.name:28} {fichero.stat().st_size / 1024:8.1f} KB")
