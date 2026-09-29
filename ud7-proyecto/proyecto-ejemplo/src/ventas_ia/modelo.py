"""Construcción, entrenamiento y persistencia del modelo (UD6)."""

import json
import logging
from pathlib import Path

import joblib
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

logger = logging.getLogger(__name__)

NUMERICAS = ["mes", "descuento", "precio"]
CATEGORICAS = ["ciudad", "producto", "canal"]
CARACTERISTICAS = NUMERICAS + CATEGORICAS
OBJETIVO = "unidades"
SEMILLA = 42

RUTA_MODELO = Path("modelos") / "modelo.joblib"
RUTA_METRICAS = Path("modelos") / "metricas.json"


def construir_pipeline(**parametros) -> Pipeline:
    """Devuelve el pipeline completo: preparación + modelo, sin entrenar."""
    preparacion = ColumnTransformer(
        [("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAS)],
        remainder="passthrough",
    )
    bosque = RandomForestRegressor(
        n_estimators=parametros.get("n_estimators", 300),
        max_depth=parametros.get("max_depth", 10),
        min_samples_leaf=parametros.get("min_samples_leaf", 5),
        random_state=SEMILLA,
        n_jobs=-1,
    )
    return Pipeline([("preparacion", preparacion), ("modelo", bosque)])


def entrenar(ventas: pd.DataFrame, **parametros) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    """Entrena el pipeline y devuelve el modelo y el conjunto de prueba."""
    X = ventas[CARACTERISTICAS]
    y = ventas[OBJETIVO]
    X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
        X, y, test_size=0.2, random_state=SEMILLA
    )
    modelo = construir_pipeline(**parametros).fit(X_entrena, y_entrena)
    logger.info("Modelo entrenado con %d filas", len(X_entrena))
    return modelo, X_prueba, y_prueba


def guardar(modelo: Pipeline, metricas: dict, ruta: Path = RUTA_MODELO) -> None:
    """Guarda el pipeline y su ficha de métricas."""
    ruta.parent.mkdir(exist_ok=True)
    joblib.dump(modelo, ruta, compress=3)
    ficha = dict(metricas)
    ficha["version_sklearn"] = sklearn.__version__
    ficha["caracteristicas"] = CARACTERISTICAS
    ficha["objetivo"] = OBJETIVO
    RUTA_METRICAS.write_text(json.dumps(ficha, indent=2, ensure_ascii=False), encoding="utf-8")


def cargar_modelo(ruta: Path = RUTA_MODELO) -> tuple[Pipeline, dict]:
    """Carga el pipeline entrenado y sus métricas."""
    if not ruta.exists():
        raise FileNotFoundError("No hay modelo entrenado. Ejecuta scripts/entrenar.py")
    metricas = json.loads(RUTA_METRICAS.read_text(encoding="utf-8"))
    return joblib.load(ruta), metricas
