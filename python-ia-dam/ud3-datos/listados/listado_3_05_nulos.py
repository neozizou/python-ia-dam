"""Valores ausentes: contarlos, entenderlos y decidir.

Rellenar los huecos con la media es la respuesta automática, y casi siempre la
equivocada. Antes hay que preguntarse **por qué** falta el dato, porque de eso
depende qué se puede hacer con él.
"""

from pathlib import Path

import pandas as pd

RUTA = Path(__file__).resolve().parents[2] / "datos-comunes" / "jugadores.csv"
sol = pd.read_csv(RUTA, low_memory=False).query("fifa == 2020")

# 1. Cuántos huecos hay y dónde.
nulos = sol.isna().sum()
con_huecos = nulos[nulos > 0].sort_values(ascending=False)
print("Columnas con huecos, en porcentaje:")
print((con_huecos / len(sol) * 100).round(1).to_string())

# 2. Mirar quién los tiene: aquí está la explicación.
sin_pace = sol[sol["pace"].isna()]
print(f"\nJugadores sin 'pace': {len(sin_pace)}")
print("Sus posiciones:", sin_pace["player_positions"].value_counts().head(3).to_dict())

sin_portero = sol[sol["gk_diving"].isna()]
print(f"\nJugadores sin 'gk_diving': {len(sin_portero)}")
print("¿Alguno es portero?",
      sin_portero["player_positions"].str.contains("GK").any())

# 3. Los dos grupos son complementarios y no se solapan.
print(f"\n{len(sin_pace)} + {len(sin_portero)} = {len(sin_pace) + len(sin_portero)}"
      f" = {len(sol)} jugadores")

# 4. Qué NO hay que hacer.
media_pace = sol["pace"].mean()
print(f"\nSi rellenáramos 'pace' con la media ({media_pace:.1f}),")
print("estaríamos diciendo que los porteros corren como un jugador normal.")

# 5. Qué sí: dropna, fillna o dejarlo, según el caso.
print("\nTres respuestas posibles:")
print(f"  dropna(subset=['pace']) -> quedan {len(sol.dropna(subset=['pace'])):,} filas")
print(f"  fillna(0) en gk_* ------> correcto solo si 0 significa 'no aplica'")
print(f"  dejarlo como NaN -------> pandas ya lo ignora en mean(), sum() y groupby()")
print(f"\n  media de 'pace' ignorando los nulos: {sol['pace'].mean():.1f}")
print(f"  media tratando los nulos como cero: {sol['pace'].fillna(0).mean():.1f}  <- falsa")
