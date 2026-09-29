"""Listado 3.4. Seleccionar y filtrar: loc, iloc y máscaras booleanas."""

from pathlib import Path

import pandas as pd

ventas = pd.read_csv(Path("datos") / "ventas_2026.csv", sep=";", decimal=",",
                     parse_dates=["fecha"])

print(ventas.loc[0, "ciudad"])                 # por etiqueta: fila 0, columna ciudad
print(ventas.iloc[0, 2])                       # por posición: fila 0, columna 2
print(ventas.loc[:4, ["ciudad", "precio"]])    # rebanada de filas y columnas

caras = ventas["precio"] > 500                 # una Series de True/False
print(caras.sum(), "ventas de más de 500 €")
print(ventas[caras].head(3))

# Varias condiciones: & (y), | (o), ~ (no). Cada una entre paréntesis
granada_online = ventas[(ventas["ciudad"] == "Granada") & (ventas["canal"] == "online")]
print(len(granada_online))

andalucia_oriental = ventas[ventas["ciudad"].isin(["Granada", "Jaén", "Almería"])]
print(len(andalucia_oriental))

print(len(ventas[ventas["precio"].between(100, 200)]))
print(len(ventas.query("precio > 500 and canal == 'tienda'")))   # alternativa legible
