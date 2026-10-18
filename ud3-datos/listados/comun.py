"""Carga y limpieza del fichero de jugadores, compartidas por los listados.

Reúne lo que se decide a lo largo del apartado 3.4. Cada decisión está
justificada en los apuntes; aquí quedan escritas una sola vez para que todos
los listados partan exactamente de los mismos datos.
"""

from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[2]
JUGADORES = RAIZ / "datos-comunes" / "jugadores.csv"
POSICIONES = RAIZ / "datos-comunes" / "posiciones.csv"

# FIFA 15 trae el valor y el salario a cero en sus 15.465 filas: el dato no
# existe en esa edición. Se descarta entera (apartado 3.4).
PRIMERA_EDICION = 2016

# Columnas que se quedan. El fichero original trae 37; para analizar el
# catálogo no hacen falta las seis de portero ni los identificadores largos.
COLUMNAS = [
    "fifa", "sofifa_id", "short_name", "age", "nationality", "club",
    "player_positions", "preferred_foot", "work_rate", "body_type",
    "height_cm", "weight_kg", "overall", "potential",
    "value_eur", "wage_eur", "contract_valid_until", "joined",
    "pace", "shooting", "passing", "dribbling", "defending", "physic",
]


def cargar_limpio(ruta: Path = JUGADORES, edicion: int | None = None) -> pd.DataFrame:
    """Devuelve el DataFrame de jugadores limpio y con columnas derivadas.

    Si se indica `edicion`, devuelve solo esa; si no, de 2016 en adelante.
    """
    jugadores = pd.read_csv(ruta, usecols=COLUMNAS, low_memory=False)

    # 1. La edición sin datos de dinero fuera, y el filtro opcional por año.
    jugadores = jugadores[jugadores["fifa"] >= PRIMERA_EDICION]
    if edicion is not None:
        jugadores = jugadores[jugadores["fifa"] == edicion]

    # 2. Los ceros de los agentes libres son ausencias, no importes. El tipo
    #    "Int64" (con mayúscula) es el entero de pandas que admite nulos; el
    #    "int64" normal no, y la columna acabaría convertida en texto.
    for columna in ("value_eur", "wage_eur"):
        jugadores[columna] = jugadores[columna].replace(0, pd.NA).astype("Int64")

    # 3. Texto: body_type solo admite tres valores; el resto es ruido.
    validos = ["Lean", "Normal", "Stocky"]
    jugadores["body_type"] = jugadores["body_type"].where(
        jugadores["body_type"].isin(validos), "Normal")

    # 4. work_rate guarda dos datos en una columna: se parte en dos.
    esfuerzo = jugadores["work_rate"].str.split("/", expand=True)
    jugadores["esfuerzo_ataque"] = esfuerzo[0]
    jugadores["esfuerzo_defensa"] = esfuerzo[1]

    # 5. Columnas derivadas útiles para el resto de la unidad.
    jugadores["posicion"] = (jugadores["player_positions"]
                             .str.split(",").str[0].str.strip())
    jugadores["margen"] = jugadores["potential"] - jugadores["overall"]
    jugadores["es_portero"] = jugadores["posicion"] == "GK"

    return jugadores.reset_index(drop=True)


def cargar_posiciones(ruta: Path = POSICIONES) -> pd.DataFrame:
    """Tabla de búsqueda: código de posición, nombre en español y línea."""
    return pd.read_csv(ruta)
