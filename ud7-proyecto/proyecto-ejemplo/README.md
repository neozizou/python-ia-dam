# Ventas IA · Proyecto integrador (ejemplo)

Predicción de las unidades que se venderán en un pedido, a partir del producto, el canal, la ciudad, el mes, el descuento y el precio.

**Aplicación publicada:** *(aquí va el enlace de Streamlit Community Cloud)*

## Puesta en marcha

```bash
git clone <url-del-repositorio>
cd proyecto-ejemplo
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1   ·   macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .

python scripts/entrenar.py      # entrena y guarda modelos/modelo.joblib
python -m pytest -q             # 4 pruebas
streamlit run app/app.py
```

## Estructura

```text
proyecto-ejemplo/
├── datos/ventas_ml.csv       datos de partida
├── modelos/                  modelo entrenado y sus métricas (no se sube a Git)
├── notebooks/                exploración de la UD3
├── src/ventas_ia/
│   ├── datos.py              cargar_limpio(): toda la limpieza, en un sitio
│   ├── modelo.py             construir_pipeline(), entrenar(), guardar(), cargar_modelo()
│   └── evaluacion.py         metricas() y metricas_por_grupo()
├── scripts/entrenar.py       entrenamiento reproducible desde la terminal
├── tests/test_proyecto.py    pruebas de datos y de modelo
├── app/app.py                aplicación Streamlit: panel, predicción y ficha
├── requirements.txt          dependencias con versiones fijadas
└── pyproject.toml
```

## Datos

- **Origen:** fichero de ventas del módulo, 8.000 registros de 2026.
- **Limpieza:** duplicados eliminados, ciudad normalizada, canal nulo como `desconocido`, filas sin unidades o sin precio descartadas.
- **Columna derivada:** `importe = unidades × precio`, que **no** se usa como característica, porque contiene la respuesta.

## Hallazgos del análisis

1. El precio y el mes explican la mayor parte de la variación de las unidades.
2. El canal online vende más unidades por pedido que la tienda y el teléfono.
3. Las devoluciones (16,1 % del total) se concentran en pedidos grandes del canal online.
4. Los productos baratos tienen cantidades mucho más variables que los caros.
5. El descuento aumenta las unidades, pero su efecto es menor que el del propio producto.

## Ficha del modelo

| Campo | Valor |
| --- | --- |
| Problema | Regresión: unidades de un pedido |
| Modelo | `RandomForestRegressor` (300 árboles, profundidad 10, mínimo 5 por hoja) dentro de un `Pipeline` con `OneHotEncoder` |
| Datos de entrenamiento | 6.400 filas; prueba: 1.600 (partición 80/20, semilla 42) |
| Métricas en prueba | MAE 1,54 unidades · RMSE 2,18 · R² 0,801 |
| Referencia ingenua | Predecir siempre la media: MAE 3,72 unidades |
| Dónde falla | MAE 2,56 en ratón y 2,36 en teclado, frente a 0,76 en portátil |
| Sesgo | Error medio próximo a 0 en todos los grupos: no sobreestima sistemáticamente |
| Límites de uso | No extrapola a precios, productos o canales no vistos. No explica causas: no sirve para fijar precios |
| Versión | scikit-learn 1.8.0 · modelo entrenado el 28/09/2026 |

## Reproducibilidad

Semilla fija (42) en la partición y en el bosque, versiones fijadas en `requirements.txt` y entrenamiento en un script, no en un notebook. Con el mismo fichero de datos, `scripts/entrenar.py` produce siempre las mismas métricas.
