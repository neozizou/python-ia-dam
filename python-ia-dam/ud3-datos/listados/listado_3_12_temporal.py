"""Series temporales: seguir a los mismos jugadores durante cinco ediciones.

Hasta aquí hemos mirado una foto. Ahora miramos la película: el mismo
`sofifa_id` aparece en varias ediciones, así que se puede ver cómo evoluciona
cada jugador y cómo cambia el conjunto.
"""

import pandas as pd

from comun import cargar_limpio

panel = cargar_limpio()            # todas las ediciones desde 2016
print(f"Panel: {len(panel):,} filas · ediciones {sorted(panel['fifa'].unique())}")

# ¿Cuántas ediciones tiene cada jugador?
ediciones = panel.groupby("sofifa_id")["fifa"].nunique()
print("\nJugadores según el número de ediciones en las que aparecen:")
print(ediciones.value_counts().sort_index().to_string())

# --- Un jugador concreto -------------------------------------------------
messi = panel[panel["sofifa_id"] == 158023]
print("\nMessi, edición a edición:")
print(messi[["fifa", "age", "overall", "value_eur", "wage_eur"]].to_string(index=False))

# --- El conjunto a lo largo del tiempo -----------------------------------
print("\nCómo evoluciona el conjunto:")
evolucion = panel.groupby("fifa").agg(
    jugadores=("sofifa_id", "size"),
    edad_media=("age", "mean"),
    media=("overall", "mean"),
    valor_mediano=("value_eur", "median"),
).round(1)
print(evolucion.to_string())

# Variación respecto al año anterior: pct_change.
evolucion["subida_valor_%"] = (evolucion["valor_mediano"].pct_change() * 100).round(1)
print("\nSubida del valor mediano, año a año:")
print(evolucion[["valor_mediano", "subida_valor_%"]].to_string())

# --- Fechas de verdad ----------------------------------------------------
# `joined` es texto hasta que se convierte. parse_dates lo hace al leer; aquí
# lo hacemos después para ver la diferencia.
con_fecha = panel[panel["fifa"] == 2020].copy()
con_fecha["joined"] = pd.to_datetime(con_fecha["joined"], errors="coerce")
con_fecha["anios_en_el_club"] = 2019 - con_fecha["joined"].dt.year

print("\nAños que lleva cada jugador en su club (FIFA 20):")
print(con_fecha["anios_en_el_club"].describe().round(1).to_string())
print("\nFichajes por mes del año (los cinco más frecuentes):")
print(con_fecha["joined"].dt.month.value_counts().head(5).to_string())
print("\n  Julio y enero: los dos mercados de fichajes. El dato lo confirma.")
