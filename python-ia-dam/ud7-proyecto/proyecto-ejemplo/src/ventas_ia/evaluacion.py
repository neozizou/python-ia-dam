"""Métricas globales y por grupos (UD6)."""

import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error


def metricas(y_real, y_predicho) -> dict:
    """Devuelve MAE, RMSE y R² redondeados."""
    return {
        "mae": round(mean_absolute_error(y_real, y_predicho), 3),
        "rmse": round(root_mean_squared_error(y_real, y_predicho), 3),
        "r2": round(r2_score(y_real, y_predicho), 3),
    }


def metricas_por_grupo(X: pd.DataFrame, y_real, y_predicho, columna: str) -> pd.DataFrame:
    """MAE y sesgo medio del modelo dentro de cada categoría de una columna."""
    evaluacion = X.copy()
    evaluacion["real"] = list(y_real)
    evaluacion["prediccion"] = list(y_predicho)
    return (
        evaluacion.groupby(columna)
        .apply(
            lambda g: pd.Series({
                "casos": len(g),
                "mae": mean_absolute_error(g["real"], g["prediccion"]),
                "sesgo": (g["prediccion"] - g["real"]).mean(),
            }),
            include_groups=False,
        )
        .round(2)
        .sort_values("mae", ascending=False)
    )
