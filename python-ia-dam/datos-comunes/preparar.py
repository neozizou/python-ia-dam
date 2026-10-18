"""Construye `jugadores.csv` a partir del dataset original de Kaggle.

El fichero que usamos en el curso ya está en el repositorio, así que no hace
falta ejecutar esto para seguir las unidades. Está aquí por dos razones: para
que se pueda reproducir lo que hemos hecho con los datos, y para que veas cómo
se descarga un dataset de Kaggle desde Python.

    pip install kagglehub
    python datos-comunes/preparar.py

La primera vez pedirá credenciales de Kaggle. Hay que crear una cuenta, entrar
en «Settings», «API», «Create New Token» y guardar el fichero que descarga en
`~/.kaggle/kaggle.json`.
"""

import sys
from pathlib import Path

import pandas as pd

# La versión está fijada a propósito: así todo el mundo trabaja con los mismos
# datos aunque el autor publique otra versión más adelante.
DATASET = ("stefanoleone992/fifa-20-complete-player-dataset/versions/1")

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "jugadores.csv"
EDICIONES = range(15, 21)

# De las 104 columnas del original nos quedamos con estas 37. El resto son
# valoraciones por puesto («89+2») y atributos de detalle que no usamos.
COLUMNAS = [
    # Quién es
    "sofifa_id", "short_name", "long_name", "age", "dob", "nationality",
    "height_cm", "weight_kg",
    # Dónde juega
    "club", "team_position", "joined", "contract_valid_until",
    "player_positions", "preferred_foot", "work_rate", "body_type",
    # Cuánto vale
    "overall", "potential", "value_eur", "wage_eur", "release_clause_eur",
    "international_reputation", "weak_foot", "skill_moves",
    # Cómo juega (vacías en los porteros)
    "pace", "shooting", "passing", "dribbling", "defending", "physic",
    # Cómo para (vacías en los jugadores de campo)
    "gk_diving", "gk_handling", "gk_kicking", "gk_reflexes", "gk_speed",
    "gk_positioning",
]


def descargar() -> Path:
    """Descarga el dataset de Kaggle y devuelve la carpeta donde ha quedado."""
    import kagglehub

    destino = kagglehub.dataset_download(DATASET)
    return Path(destino)


def construir(origen: Path) -> pd.DataFrame:
    """Apila las seis ediciones, quedándose con las columnas elegidas."""
    ediciones = []
    for anio in EDICIONES:
        fichero = origen / f"players_{anio}.csv"
        edicion = pd.read_csv(fichero, low_memory=False)[COLUMNAS].copy()
        edicion.insert(0, "fifa", 2000 + anio)      # de qué edición viene la fila
        ediciones.append(edicion)
        print(f"  players_{anio}.csv: {len(edicion):>6,} jugadores")
    return pd.concat(ediciones, ignore_index=True)


def main() -> None:
    origen = Path(sys.argv[1]) if len(sys.argv) > 1 else descargar()
    print(f"Leyendo de {origen}")
    jugadores = construir(origen)
    jugadores.to_csv(SALIDA, index=False)

    print(f"\n{SALIDA.name}: {len(jugadores):,} filas × {jugadores.shape[1]} columnas "
          f"({SALIDA.stat().st_size / 1024 / 1024:.1f} MB)")
    print(f"Jugadores distintos: {jugadores['sofifa_id'].nunique():,}")
    print(f"Clubes: {jugadores['club'].nunique()} · "
          f"Nacionalidades: {jugadores['nationality'].nunique()}")


if __name__ == "__main__":
    main()
