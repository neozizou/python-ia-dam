"""Genera datos/ventas_ml.csv, el conjunto de trabajo de la UD6.

A diferencia del de la UD3, este fichero tiene una señal real que un modelo
puede aprender: las unidades vendidas dependen del producto, del canal, del mes
y del descuento, con ruido; y la probabilidad de devolución depende del canal y
del tamaño del pedido. Eso permite obtener métricas creíbles, ni perfectas ni
aleatorias.
"""

from pathlib import Path

import numpy as np
import pandas as pd

FILAS = 8_000
generador = np.random.default_rng(2026)

productos = {           # demanda base de cada producto
    "portátil": 3.0, "monitor": 5.0, "teclado": 9.0,
    "ratón": 11.0, "tablet": 4.0, "impresora": 4.5,
}
precios = {"portátil": 899.90, "monitor": 180.0, "teclado": 25.0,
           "ratón": 12.5, "tablet": 349.0, "impresora": 149.9}
canales = {"tienda": 1.0, "online": 1.25, "teléfono": 0.8}
ciudades = ["Granada", "Málaga", "Sevilla", "Córdoba", "Almería", "Jaén", "Cádiz", "Huelva"]

producto = generador.choice(list(productos), FILAS)
canal = generador.choice(list(canales), FILAS, p=[0.4, 0.45, 0.15])
ciudad = generador.choice(ciudades, FILAS)
mes = generador.integers(1, 13, FILAS)
descuento = generador.choice([0.0, 0.05, 0.10, 0.20], FILAS, p=[0.55, 0.2, 0.15, 0.1])

demanda = np.array([productos[p] for p in producto])
factor_canal = np.array([canales[c] for c in canal])
estacionalidad = 1 + 0.35 * np.sin((mes - 3) * np.pi / 6)        # pico a mitad de año
efecto_descuento = 1 + 2.5 * descuento                            # rebajar vende más
ruido = generador.normal(1, 0.25, FILAS)

unidades = np.clip(
    np.round(demanda * factor_canal * estacionalidad * efecto_descuento * ruido), 1, None
).astype(int)

precio_base = np.array([precios[p] for p in producto])
precio = np.round(precio_base * (1 - descuento), 2)

# Devolución: más probable online y en pedidos grandes
logit = -2.6 + 0.9 * (canal == "online") + 0.06 * unidades + 1.2 * descuento
probabilidad = 1 / (1 + np.exp(-logit))
devuelta = generador.binomial(1, probabilidad)

datos = pd.DataFrame({
    "id_venta": np.arange(10_000, 10_000 + FILAS),
    "mes": mes,
    "ciudad": ciudad,
    "producto": producto,
    "canal": canal,
    "descuento": descuento,
    "precio": precio,
    "unidades": unidades,
    "devuelta": devuelta,
})

destino = Path("datos") / "ventas_ml.csv"
destino.parent.mkdir(exist_ok=True)
datos.to_csv(destino, index=False, sep=";", decimal=",")
print(f"{destino}: {len(datos):,} filas")
print(datos.head())
print("\nDevoluciones:", f"{datos['devuelta'].mean():.1%}")
print("Unidades: media", round(datos["unidades"].mean(), 2),
      "| rango", datos["unidades"].min(), "-", datos["unidades"].max())
