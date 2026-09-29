"""Pruebas mínimas: que los datos y el modelo sigan cumpliendo lo prometido."""

import pandas as pd
import pytest

from ventas_ia import CARACTERISTICAS, cargar_limpio, entrenar, metricas


@pytest.fixture(scope="module")
def ventas() -> pd.DataFrame:
    return cargar_limpio()


def test_los_datos_no_tienen_nulos_en_las_caracteristicas(ventas):
    assert ventas[CARACTERISTICAS].isna().sum().sum() == 0


def test_las_unidades_son_positivas(ventas):
    assert (ventas["unidades"] > 0).all()


def test_el_modelo_supera_al_ingenuo(ventas):
    modelo, X_prueba, y_prueba = entrenar(ventas)
    resultado = metricas(y_prueba, modelo.predict(X_prueba))
    error_ingenuo = (y_prueba - ventas["unidades"].mean()).abs().mean()
    assert resultado["mae"] < error_ingenuo


def test_el_modelo_predice_un_caso_nuevo(ventas):
    modelo, _, _ = entrenar(ventas)
    caso = pd.DataFrame([{"mes": 6, "descuento": 0.1, "precio": 180.0,
                          "ciudad": "Granada", "producto": "monitor", "canal": "online"}])
    prediccion = modelo.predict(caso)[0]
    assert 0 < prediccion < 100
