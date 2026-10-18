"""Cargar el fichero y mirarlo por primera vez.

`read_csv` tiene más de cincuenta parámetros. En la práctica solo necesitas
unos pocos, pero elegirlos bien ahorra mucha limpieza después.
"""

from pathlib import Path

import pandas as pd

RUTA = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"

# La lectura mínima: pandas deduce el separador, los tipos y la cabecera.
jugadores = pd.read_csv(RUTA)
print("Filas y columnas:", jugadores.shape)
print("Memoria:", f"{jugadores.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

# Leer solo lo que hace falta: menos memoria y menos ruido.
columnas = ["fifa", "short_name", "age", "nationality", "club",
            "player_positions", "overall", "potential", "value_eur"]
ligero = pd.read_csv(RUTA, usecols=columnas)
print("\nCon usecols:", ligero.shape,
      f"· {ligero.memory_usage(deep=True).sum() / 1024**2:.1f} MB")

# Las fechas no se convierten solas: hay que pedirlo.
con_fechas = pd.read_csv(RUTA, usecols=["short_name", "dob", "joined"],
                         parse_dates=["dob", "joined"])
print("\nTipos de las fechas:")
print(con_fechas.dtypes.to_string())
print("\nNacimiento del primer jugador:", con_fechas["dob"].iloc[0].date())

# Las primeras filas, para ver qué pinta tiene.
print("\n", ligero.head(3).to_string(index=False), sep="")
