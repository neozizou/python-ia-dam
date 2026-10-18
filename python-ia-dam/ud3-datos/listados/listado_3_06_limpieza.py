"""Duplicados, texto y tipos: la limpieza que sí hay que hacer.

Limpiar no es «dejarlo bonito». Es tomar decisiones sobre los datos y dejarlas
escritas, porque cada una cambia los resultados y alguien tendrá que poder
revisarlas. Este listado recorre las cuatro de este fichero.
"""

from pathlib import Path

import pandas as pd

RUTA = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"
jugadores = pd.read_csv(RUTA, low_memory=False)

# --- 1. La edición sin datos de dinero -----------------------------------
print("Valor mediano por edición, tal cual viene el fichero:")
print(jugadores.groupby("fifa")["value_eur"].median().astype(int).to_string())
print("\n  FIFA 15 no es que fuera barato: no trae el dato. Fuera.")
jugadores = jugadores[jugadores["fifa"] >= 2016]

# --- 2. Duplicados -------------------------------------------------------
print(f"\nFilas duplicadas enteras: {jugadores.duplicated().sum()}")
print("Duplicados de (edición, jugador):",
      jugadores.duplicated(subset=["fifa", "sofifa_id"]).sum())
print("  Ninguno. Que el mismo jugador salga seis veces es correcto:")
print("  son seis ediciones, no seis copias.")

# --- 3. Los ceros que son ausencias --------------------------------------
sol = jugadores[jugadores["fifa"] == 2020].copy()
print(f"\nJugadores con value_eur = 0: {(sol['value_eur'] == 0).sum()}")
print(f"  Valor medio contándolos:    {sol['value_eur'].mean():>12,.0f} €")
sol["value_eur"] = sol["value_eur"].replace(0, pd.NA)
print(f"  Valor medio sin contarlos:  {sol['value_eur'].mean():>12,.0f} €")

# --- 4. Texto con valores imposibles -------------------------------------
print("\nbody_type debería tener tres valores:")
print(sol["body_type"].value_counts().to_string())
VALIDOS = ["Lean", "Normal", "Stocky"]
raros = ~sol["body_type"].isin(VALIDOS)
print(f"\n  {raros.sum()} filas con algo que no es una complexión.")
sol["body_type"] = sol["body_type"].where(~raros, "Normal")
print("  Corregidas a 'Normal':", sol["body_type"].value_counts().to_dict())

# --- 5. Una columna con dos datos dentro ---------------------------------
print("\nwork_rate guarda esfuerzo en ataque y en defensa:", sol["work_rate"].iloc[0])
sol[["esfuerzo_ataque", "esfuerzo_defensa"]] = sol["work_rate"].str.split("/", expand=True)
print(sol[["work_rate", "esfuerzo_ataque", "esfuerzo_defensa"]].head(3).to_string(index=False))
