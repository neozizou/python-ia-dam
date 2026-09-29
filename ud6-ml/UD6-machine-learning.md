# UD6 · Machine Learning con scikit-learn

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [6.1 Qué es el Machine Learning](#61-qué-es-el-machine-learning)
- [6.2 Preparar los datos](#62-preparar-los-datos)
- [6.3 Regresión: predecir un número](#63-regresión-predecir-un-número)
- [6.4 Clasificación: predecir una categoría](#64-clasificación-predecir-una-categoría)
- [6.5 Evaluar bien y ajustar](#65-evaluar-bien-y-ajustar)
- [6.6 Aprendizaje no supervisado](#66-aprendizaje-no-supervisado)
- [6.7 Interpretar, guardar y poner en marcha](#67-interpretar-guardar-y-poner-en-marcha)
- [Práctica de la unidad · Hito 5 del proyecto integrador](#práctica-de-la-unidad--hito-5-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD6](#bibliografía-de-la-ud6)

## Presentación de la unidad

Diez horas para entrenar tu primer modelo de verdad. Hasta ahora has descrito lo que pasó; a partir de aquí vas a estimar lo que pasará, con un número al lado que diga cuánto te puedes fiar.

Dos avisos desde el principio. El primero: el 80 % del trabajo de un proyecto de Machine Learning es lo que ya sabes hacer de las UD3 y UD4, preparar los datos; el algoritmo son tres líneas. El segundo: un modelo sin una evaluación honesta no vale nada, y es muy fácil engañarse a uno mismo. Por eso dedicamos un apartado entero a evaluar.

### Resultado de aprendizaje y criterios de evaluación

**RA3.** Aplica conceptos básicos de Machine Learning en problemas reales.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 3a | Comprende los conceptos básicos del aprendizaje automático y sus tipos | 6.1, 6.6 |
| 3b | Implementa modelos de regresión y clasificación con bibliotecas de Python | 6.2, 6.3, 6.4 |
| 3c | Evalúa el rendimiento de los modelos con métricas adecuadas | 6.3, 6.4, 6.5, 6.7 |
| 3d | Ajusta los parámetros de los modelos para mejorar su precisión con datos reales | 6.2, 6.5 |

El criterio 3e, el proyecto integrador, se cierra en la UD7.

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Martes 15/12/2026 | 1 | 6.1 Qué es el ML |
| 2 | Lunes 21/12/2026 | 2 | 6.2 Preparar los datos |
| 3 | Martes 22/12/2026 | 1 | 6.3 Regresión |
| 4 | Lunes 11/01/2027 | 2 | 6.3 Árboles y bosques · 6.4 Clasificación |
| 5 | Martes 12/01/2027 | 1 | 6.4 Desbalanceo y umbral |
| 6 | Lunes 18/01/2027 | 2 | 6.5 Evaluar y ajustar · 6.6 No supervisado |
| 7 | Martes 19/01/2027 | 1 | 6.7 Interpretar, guardar y poner en marcha |

Las vacaciones de Navidad van del 23/12 al 6/1.

### Antes de empezar

```bash
python -m pip install -r ud6-ml/requirements.txt
```

El conjunto de datos de la unidad, `listados/datos/ventas_ml.csv`, tiene 8.000 ventas con una **señal real**: las unidades dependen del producto, del canal, del mes y del descuento, con ruido; y la probabilidad de devolución depende del canal y del tamaño del pedido. Lo genera [`generar_datos_ml.py`](listados/generar_datos_ml.py), así que puedes leer cómo se construyó y comparar lo que el modelo descubre con lo que de verdad hay dentro. Eso es un lujo que no tendrás nunca con datos reales.

## 6.1 Qué es el Machine Learning

**Programar** es escribir las reglas: si el importe supera los 1.000 €, marca la venta como grande. **Aprender automáticamente** es lo contrario: le das al sistema ejemplos con la respuesta correcta y él deduce las reglas.

```text
Programación clásica:   datos + reglas    -> resultados
Machine Learning:       datos + resultados -> reglas (el modelo)
```

| Término | Qué es |
| --- | --- |
| Inteligencia artificial | El campo completo: que una máquina haga tareas que asociamos a la inteligencia |
| Machine Learning | La parte que aprende de datos en lugar de seguir reglas escritas a mano |
| Deep Learning | La parte del ML que usa redes neuronales profundas; brilla con imagen, audio y texto |

### Tipos de aprendizaje

| Tipo | Los datos traen… | Sirve para | Ejemplo en este módulo |
| --- | --- | --- | --- |
| **Supervisado** | La respuesta correcta (etiqueta) | Predecir un número (regresión) o una categoría (clasificación) | Unidades que se venderán; si un pedido se devolverá |
| **No supervisado** | Nada, solo las características | Agrupar, reducir dimensiones, detectar anomalías | Segmentar las ventas en grupos parecidos (6.6) |
| **Por refuerzo** | Recompensas tras cada acción | Aprender una estrategia por ensayo y error | Un robot que aprende a caminar; no lo veremos en el módulo |

### El vocabulario y la API

Una fila es una **muestra**; las columnas con las que el modelo decide son las **características** (`X`); lo que se quiere predecir es el **objetivo** (`y`). scikit-learn mantiene la misma interfaz para todos sus modelos, la que ya construiste a mano en el listado 2.18 ([scikit-learn: Getting started](https://scikit-learn.org/stable/getting_started.html)).

**Listado 6.1.** La API de scikit-learn · [ver fichero](listados/listado_6_01_api_sklearn.py)

```python
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]      # características: siempre una tabla 2D
y = [25, 50, 74, 101, 124]         # objetivo: un vector

modelo = LinearRegression()
modelo.fit(X, y)                   # 1. aprender de los datos
print(modelo.predict([[6], [10]])) # 2. predecir datos nuevos  -> [149.5 249.1]
print(modelo.score(X, y))          # 3. evaluar               -> 0.9996
```

Cambiar de modelo es cambiar esas dos primeras líneas: el resto del programa no se entera. Eso es el *duck typing* de la UD2 aplicado a una biblioteca entera.

### El flujo de un proyecto

1. **Plantear la pregunta** y decidir qué se predice.
2. **Preparar los datos**: limpieza (UD3), características, partición.
3. **Entrenar** un modelo sencillo que sirva de referencia.
4. **Evaluar** con métricas y datos que el modelo no ha visto.
5. **Ajustar**: características nuevas, otros modelos, hiperparámetros.
6. **Interpretar y comunicar**: qué usa el modelo, dónde falla y qué margen tiene.
7. **Poner en marcha** y vigilar: los datos cambian con el tiempo.

> [!IMPORTANT]
> El paso que más se salta y más caro sale es el 3. Antes de un bosque aleatorio, entrena el modelo más tonto posible: predecir siempre la media, o siempre la clase mayoritaria. Si tu modelo sofisticado no lo supera con claridad, el problema no está en el algoritmo.

### Para practicar

1. Clasifica como supervisado, no supervisado o por refuerzo: detectar spam, agrupar clientes por comportamiento, estimar el precio de un piso, un coche que aprende a aparcar.
2. Para tu conjunto de datos del proyecto: ¿qué predecirías? ¿Es regresión o clasificación? ¿Qué decisión cambiaría esa predicción?
3. (A) Busca un caso en el que un modelo se pusiera en producción y fallara al cambiar los datos. ¿Qué se podría haber vigilado?

## 6.2 Preparar los datos

### Características, objetivo y partición

**Listado 6.2.** Entrenamiento y prueba · [ver fichero](listados/listado_6_02_particion.py)

```python
from sklearn.model_selection import train_test_split

X = ventas[["mes", "ciudad", "producto", "canal", "descuento", "precio"]]
y = ventas["unidades"]

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42      # random_state fija el reparto
)
# Entrenamiento: 6.400 filas | Prueba: 1.600 filas
```

El conjunto de prueba **no se toca** hasta el final. Es la simulación de los datos futuros: si lo usas para decidir algo, deja de ser una medida honesta. `random_state` hace que el reparto sea reproducible, para que tus resultados y los del profesor coincidan.

### Escalar y codificar

Los modelos trabajan con números. Hay que convertir las categorías y, en muchos modelos, poner todas las variables en una escala comparable.

**Listado 6.3.** Escalado y codificación · [ver fichero](listados/listado_6_03_preparacion.py)

```python
from sklearn.preprocessing import OneHotEncoder, StandardScaler

escalador = StandardScaler()                     # media 0, desviación 1
numericas = escalador.fit_transform(ventas[["precio", "descuento"]])

codificador = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
categorias = codificador.fit_transform(ventas[["canal"]])
print(codificador.get_feature_names_out())   # ['canal_online' 'canal_teléfono' 'canal_tienda']
```

| Transformación | Para qué | Cuándo hace falta |
| --- | --- | --- |
| `StandardScaler` | Escalas comparables | Modelos con distancias o pesos: regresión lineal y logística, k-NN, k-means, redes |
| `OneHotEncoder` | Una columna 0/1 por categoría | Siempre que haya texto. `handle_unknown="ignore"` evita fallar con categorías nuevas |
| `SimpleImputer` | Rellenar valores ausentes | Cuando queden nulos tras la limpieza de la UD3 |

Los árboles y los bosques no necesitan escalado: parten por umbrales, y el umbral se adapta a la escala.

### El pipeline lo junta todo

**Listado 6.4.** `ColumnTransformer` y `Pipeline` · [ver fichero](listados/listado_6_04_pipeline.py)

```python
preparacion = ColumnTransformer([
    ("numericas", StandardScaler(), numericas),
    ("categoricas", OneHotEncoder(handle_unknown="ignore"), categoricas),
])

modelo = Pipeline([
    ("preparacion", preparacion),
    ("regresion", LinearRegression()),
])

modelo.fit(X_entrena, y_entrena)
print(modelo.score(X_prueba, y_prueba))      # 0.619
```

Un `Pipeline` es un objeto con `fit` y `predict` que por dentro encadena pasos: exactamente el patrón del listado 2.18. Sus ventajas no son estéticas:

- Se guarda entero con el modelo, así que en producción no hay que recordar qué transformaciones se aplicaron.
- La validación cruzada y la búsqueda de hiperparámetros lo tratan como un modelo más.
- Evita la fuga de datos, que es el error que viene ahora.

### Fuga de datos

**Listado 6.5.** Escalar antes de dividir es hacer trampa · [ver fichero](listados/listado_6_05_fuga_datos.py)

```python
# MAL: el escalador ve TODOS los datos, incluidos los de prueba
X_todo_escalado = StandardScaler().fit_transform(X)
_, X_prueba_mal, _, _ = train_test_split(X_todo_escalado, y, test_size=0.2)

# BIEN: el escalador aprende solo del entrenamiento
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(X, y, test_size=0.2)
escalador = StandardScaler().fit(X_entrena)
```

Hay **fuga de datos** cuando el modelo, al entrenarse, tiene acceso a información que en el momento real de predecir no existirá. Ocurre al escalar o imputar con todos los datos, al seleccionar variables mirando el conjunto de prueba, o al incluir una columna que en realidad contiene la respuesta.

> [!WARNING]
> El síntoma de la fuga es un resultado sospechosamente bueno. Si tu modelo acierta casi siempre, no celebres: busca la fuga. En estos datos, predecir `unidades` incluyendo `importe` daría un R² casi perfecto, porque el importe es unidades por precio. **Regla: cualquier paso que APRENDA algo va dentro del Pipeline.**

### Para practicar

1. Añade `SimpleImputer` al `ColumnTransformer` para que el pipeline aguante nulos.
2. Divide en tres: entrenamiento, validación y prueba. ¿Para qué sirve cada uno?
3. (A) Inventa un caso de fuga de datos en tu proyecto: una columna que no deberías usar porque no existiría en el momento de predecir.

## 6.3 Regresión: predecir un número

**Listado 6.6.** Regresión lineal y sus métricas · [ver fichero](listados/listado_6_06_regresion.py)

```python
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error

modelo.fit(X_entrena, y_entrena)
prediccion = modelo.predict(X_prueba)

print(mean_absolute_error(y_prueba, prediccion))       # 2.21 unidades
print(root_mean_squared_error(y_prueba, prediccion))   # 3.03 unidades
print(r2_score(y_prueba, prediccion))                  # 0.619

media = y_entrena.mean()                               # modelo ingenuo de referencia
print(mean_absolute_error(y_prueba, [media] * len(y_prueba)))   # 3.72 unidades
```

| Métrica | Qué mide | Cómo se lee |
| --- | --- | --- |
| **MAE** | Error absoluto medio | En las unidades del objetivo: «me equivoco en 2,2 unidades de media» |
| **RMSE** | Raíz del error cuadrático medio | Como el MAE, pero penaliza más los errores grandes |
| **R²** | Proporción de varianza explicada | 1 es perfecto, 0 equivale a predecir la media, negativo es peor que la media |

El modelo explica el 62 % de la variación y reduce el error del 3,72 ingenuo a 2,21: mejora real, pero lejos de ser magia. **Informa siempre del MAE junto al R²**: el primero se entiende sin saber estadística.

### Árboles y bosques

**Listado 6.7.** Cuatro modelos comparados · [ver fichero](listados/listado_6_07_arboles.py)

```text
Modelo                    MAE entrena  MAE prueba  R² prueba
Regresión lineal                 2.19        2.21      0.619
Árbol (profundidad 5)            1.76        1.85      0.715
Árbol sin podar                  0.78        1.97      0.647
Bosque aleatorio                 0.98        1.71      0.748
```

Esa tabla cuenta toda la historia del aprendizaje automático:

- La **regresión lineal** solo puede trazar una recta: se queda corta con la estacionalidad, que es una curva.
- El **árbol** parte los datos por umbrales sucesivos y captura relaciones no lineales. Con profundidad 5 mejora.
- El **árbol sin podar** memoriza el entrenamiento (MAE 0,78) y empeora en prueba: eso es **sobreajuste**.
- El **bosque aleatorio** entrena cientos de árboles distintos y promedia sus predicciones. Al promediar, los errores individuales se cancelan. Es el mejor de los cuatro y casi siempre un buen punto de partida.

> [!TIP]
> Compara siempre **MAE de entrenamiento y de prueba**. Si el primero es mucho menor, el modelo memoriza. Si ambos son malos, se queda corto: es **subajuste**.

### Para practicar

1. Añade `GradientBoostingRegressor` a la comparación del listado 6.7. ¿Mejora al bosque?
2. Entrena sin la columna `precio` y mira cuánto empeora el MAE. ¿Qué te dice eso?
3. Crea una característica nueva, `es_temporada_alta`, a partir del mes, y comprueba si ayuda al modelo lineal.
4. (A) Explica con tus palabras por qué un árbol sin podar acierta casi siempre en entrenamiento. ¿Qué está memorizando?

## 6.4 Clasificación: predecir una categoría

**Listado 6.8.** Regresión logística y matriz de confusión · [ver fichero](listados/listado_6_08_clasificacion.py)

```python
y = ventas["devuelta"]                      # 1 = el pedido se devolvió
# Reparto de clases: {0: 0.839, 1: 0.161}

X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y    # conserva la proporción
)
modelo = Pipeline([...("clasificacion", LogisticRegression(max_iter=1000))]).fit(...)
```

Resultado:

```text
Matriz de confusión (filas: real, columnas: predicho)
[[1340    3]
 [ 247   10]]

               precision    recall  f1-score   support
 no devuelta       0.84      1.00      0.91      1343
    devuelta       0.77      0.04      0.07       257
    accuracy                           0.84      1600
```

Un 84 % de acierto… y el modelo es **inútil**: de 257 devoluciones detecta 10. Como el 84 % de los pedidos no se devuelve, decir siempre «no se devuelve» acierta el 84 %. Esa es la trampa de la exactitud (*accuracy*) con clases desbalanceadas.

| Métrica | Fórmula intuitiva | Responde a |
| --- | --- | --- |
| Exactitud | Aciertos entre total | ¿Cuánto acierto en general? Engañosa si hay desbalanceo |
| **Precisión** | De lo que marqué como positivo, cuánto lo era | ¿Cuántas falsas alarmas doy? |
| **Recall** (sensibilidad) | De todos los positivos reales, cuántos encontré | ¿Cuántos casos se me escapan? |
| **F1** | Media armónica de precisión y recall | Un único número cuando ambas importan |
| **ROC-AUC** | Capacidad de ordenar positivos antes que negativos | ¿Separa bien las clases, sea cual sea el umbral? |

La matriz de confusión se lee así: filas, lo que ocurrió; columnas, lo que el modelo dijo. La diagonal son los aciertos; fuera están los falsos positivos (arriba a la derecha) y los falsos negativos (abajo a la izquierda).

### Desbalanceo y umbral

**Listado 6.9.** Dos formas de arreglarlo · [ver fichero](listados/listado_6_09_desbalanceo.py)

```text
sin ajuste                 recall=0.039  ROC-AUC=0.651
class_weight='balanced'    recall=0.650  ROC-AUC=0.650

Efecto del umbral en el modelo sin ajustar:
  umbral 0.50: detecta el  4% de las devoluciones con  13 avisos de 1600
  umbral 0.35: detecta el 12% de las devoluciones con  74 avisos de 1600
  umbral 0.25: detecta el 26% de las devoluciones con 247 avisos de 1600
  umbral 0.15: detecta el 69% de las devoluciones con 762 avisos de 1600
```

Dos lecciones:

- `class_weight="balanced"` hace que los errores sobre la clase minoritaria pesen más, y el recall pasa del 4 % al 65 %. El ROC-AUC apenas cambia: **el modelo era el mismo, lo que cambia es dónde corta**.
- El umbral 0,5 no es sagrado. `predict_proba` devuelve la probabilidad, y tú eliges el corte según el coste de cada error. ¿Cuánto cuesta revisar un pedido que no se iba a devolver, frente a no detectar uno que sí?

> [!IMPORTANT]
> Elegir umbral es una decisión de negocio, no técnica. El modelo da probabilidades; la organización decide qué error prefiere cometer. Si nadie lo decide, lo decide por omisión el 0,5, que casi nunca es el mejor.

### Para practicar

1. Sustituye la regresión logística por un `RandomForestClassifier` con `class_weight="balanced"`. ¿Mejora el recall?
2. Dibuja la curva ROC con `RocCurveDisplay.from_estimator`. ¿Qué forma tendría un modelo que acierta al azar?
3. Calcula, para cada umbral del listado 6.9, cuántas devoluciones se detectan y cuántos avisos falsos hay. Elige un umbral y **justifícalo por escrito**.
4. (A) Busca qué es la métrica *precision-recall AUC* y por qué se prefiere a ROC-AUC cuando la clase positiva es muy rara.

## 6.5 Evaluar bien y ajustar

### Validación cruzada

**Listado 6.10.** Una sola partición engaña · [ver fichero](listados/listado_6_10_validacion_cruzada.py)

```text
random_state=0: R² = 0.781
random_state=1: R² = 0.772
random_state=2: R² = 0.741

R² en 5 particiones: [0.748 0.773 0.762 0.766 0.746]
Media 0.759 ± 0.011
```

Cambiando solo la semilla del reparto, el R² se mueve cuatro centésimas. Por eso no se informa de un número suelto: la **validación cruzada** divide los datos en k partes, entrena k veces usando cada parte como prueba una vez, y da la media y la dispersión ([scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)).

Para clasificación se usa `StratifiedKFold`, que mantiene la proporción de clases en cada partición. Con datos temporales, ninguno de los dos: hay que entrenar con el pasado y validar con el futuro (`TimeSeriesSplit`).

### La curva del sobreajuste

**Listado 6.11.** Subajuste, punto óptimo y sobreajuste · [ver fichero](listados/listado_6_11_sobreajuste.py)

```text
profundidad  1: entrena 2.60 | prueba 2.58     <- subajuste
profundidad  5: entrena 1.76 | prueba 1.85
profundidad  8: entrena 1.42 | prueba 1.64     <- punto óptimo
profundidad 12: entrena 1.07 | prueba 1.80
profundidad 20: entrena 0.78 | prueba 1.97     <- sobreajuste
```

El listado genera además `graficos/sobreajuste.png` con las dos curvas. Es **la** imagen del Machine Learning: el error de entrenamiento baja siempre; el de prueba baja, toca fondo y vuelve a subir. El objetivo no es el error mínimo en entrenamiento, sino el mínimo en datos no vistos.

### Buscar los hiperparámetros

Los **parámetros** los aprende el modelo (los coeficientes de la recta); los **hiperparámetros** los eliges tú antes de entrenar (la profundidad del árbol, el número de árboles del bosque).

**Listado 6.12.** `GridSearchCV` · [ver fichero](listados/listado_6_12_gridsearch.py)

```python
rejilla = {
    "bosque__n_estimators": [100, 300],
    "bosque__max_depth": [6, 10, None],
    "bosque__min_samples_leaf": [1, 5],
}

busqueda = GridSearchCV(modelo, rejilla, cv=5, scoring="neg_mean_absolute_error", n_jobs=-1)
busqueda.fit(X_entrena, y_entrena)      # 12 combinaciones x 5 particiones = 60 ajustes
```

```text
Mejores parámetros: {'max_depth': 10, 'min_samples_leaf': 5, 'n_estimators': 300}
MAE en validación cruzada:    1.518
MAE en el conjunto de prueba: 1.544
```

Los nombres llevan el prefijo del paso del pipeline (`bosque__`), lo que permite ajustar también la preparación. Que el MAE de prueba (1,544) se parezca al de validación (1,518) es buena señal: no hemos sobreajustado la búsqueda.

Con muchas combinaciones, `RandomizedSearchCV` prueba un número fijo de candidatos al azar y suele llegar casi igual de lejos en mucho menos tiempo.

### Para practicar

1. Amplía la rejilla con `max_features` y compara el tiempo de ejecución.
2. Usa `RandomizedSearchCV` con 10 candidatos y compara el resultado con la búsqueda completa.
3. Ejecuta la validación cruzada con `cv=10`. ¿Cambia la media? ¿Y la dispersión?
4. (A) Explica por qué elegir los hiperparámetros mirando el conjunto de prueba es otra forma de fuga de datos.

## 6.6 Aprendizaje no supervisado

Sin etiquetas, la pregunta cambia: ya no es «¿cuánto venderé?», sino «¿qué grupos hay aquí dentro?».

**Listado 6.15.** k-means · [ver fichero](listados/listado_6_15_kmeans.py)

```python
modelo = Pipeline([("escalado", StandardScaler()),          # k-means usa distancias
                   ("kmeans", KMeans(n_clusters=3, n_init=10, random_state=42))])
ventas["grupo"] = modelo.fit_predict(X)     # fit_predict: no hay y que pasarle
```

```text
Perfil de cada grupo:
       precio  unidades  descuento          Producto dominante
0       68.23     13.43       0.11          ratón
1      160.99      6.11       0.02          impresora
2      860.09      3.60       0.04          portátil
```

k-means agrupa por cercanía: coloca k centros y reparte cada punto al más próximo, repitiendo hasta que se estabilizan. Aquí ha descubierto solo, sin ver la columna `producto`, la estructura de precio y volumen del catálogo.

Para elegir k hay dos guías: la **inercia** (distancia a los centros, que siempre baja al aumentar k; se busca el «codo») y el **coeficiente de silueta** (entre -1 y 1, mide lo compactos y separados que quedan los grupos). Ninguna decide sola: la pregunta final es si los grupos **significan algo** para quien va a usarlos.

### Para practicar

1. Prueba k de 2 a 8 en tu conjunto y decide con el codo y la silueta. ¿Coinciden?
2. Ponle nombre a cada grupo del listado 6.15 según su perfil, como lo haría el departamento comercial.
3. (A) Lee qué es DBSCAN y explica en qué se diferencia de k-means con datos que tienen ruido.

## 6.7 Interpretar, guardar y poner en marcha

### Qué mira el modelo

**Listado 6.13.** Importancia de variables · [ver fichero](listados/listado_6_13_importancia.py)

```text
Importancia por permutación (empeoramiento del MAE):
precio       2.708
mes          1.133
canal        0.467
descuento    0.129
producto     0.011
ciudad      -0.003
```

La **importancia por permutación** baraja una columna y mide cuánto empeora el modelo: si empeora mucho, esa columna era clave. Aquí el modelo se apoya en el precio, el mes y el canal, y la ciudad no aporta nada, justo lo que pusimos al generar los datos. Coincidir con la verdad conocida es la mejor comprobación de que todo el proceso está bien montado.

> [!WARNING]
> La importancia dice qué **usa** el modelo, no qué **causa** el resultado. Que el precio sea importante no significa que subir el precio cause ventas: significa que el precio identifica el producto. Para hablar de causas hacen falta experimentos, no modelos predictivos.

### Dónde falla el modelo

**Listado 6.14.** Métricas por grupo · [ver fichero](listados/listado_6_14_por_grupos.py)

```text
MAE global: 1.54

           casos   MAE  error_medio
ratón      253.0  2.55         0.17
teclado    299.0  2.37        -0.11
...
portátil   261.0  0.77         0.12
```

El error global esconde que el modelo falla tres veces más con ratones que con portátiles, algo razonable porque los productos baratos se venden en cantidades más variables. **Evaluar por grupos es obligatorio** cuando los grupos son personas: un modelo con buena media puede ser mucho peor para un colectivo concreto, y eso es exactamente el sesgo del que hablamos en la UD5.

### Guardar el modelo

**Listado 6.16.** Entrenar el modelo definitivo y guardarlo · [ver fichero](listados/listado_6_16_guardar_modelo.py)

```python
import joblib

joblib.dump(modelo, "modelos/modelo_unidades.joblib", compress=3)

metricas = {"mae": 1.544, "r2": 0.801, "version_sklearn": sklearn.__version__,
            "columnas": columnas}
```

Se guarda **el pipeline entero**, no solo el algoritmo: así la aplicación no tiene que repetir la preparación. Junto al modelo se guarda un JSON con sus métricas, las columnas que espera y la versión de scikit-learn, porque un modelo serializado con una versión puede fallar al cargarse con otra. Ese fichero es el que copiarás en `requirements.txt` al desplegar.

### Ponerlo a funcionar

**Listado 6.17.** El modelo dentro de Streamlit · [ver fichero](app/app.py)

```python
@st.cache_resource            # cache_resource, no cache_data: el modelo es un objeto vivo
def cargar_modelo(ruta: Path):
    """Carga el pipeline entrenado una sola vez."""
    return joblib.load(ruta)


caso = pd.DataFrame([{ "mes": mes, "descuento": descuento, "precio": precio,
                       "ciudad": ciudad, "producto": producto, "canal": canal }])
prediccion = modelo.predict(caso)[0]

st.metric("Unidades estimadas", f"{prediccion:.1f}")
st.caption(f"Error medio del modelo en datos no vistos (MAE): ±{metricas['mae']} unidades")
```

Para ejecutarlo:

```bash
cd ud6-ml/listados && python listado_6_16_guardar_modelo.py
cd ../.. && streamlit run ud6-ml/app/app.py
```

Fíjate en el `st.caption`: la aplicación muestra **la predicción y su margen de error**. Una cifra suelta invita a creérsela; acompañada de su MAE, invita a usarla con criterio. En la UD7 desplegaremos esto y le añadiremos la documentación del modelo.

### Para practicar

1. Guarda tu mejor modelo de clasificación y escribe una aplicación que estime la probabilidad de devolución.
2. Añade a la aplicación un aviso cuando el caso introducido quede fuera del rango de los datos de entrenamiento.
3. (A) Carga el modelo guardado en un entorno con otra versión de scikit-learn y describe qué ocurre.

## Práctica de la unidad · Hito 5 del proyecto integrador

Entrena, evalúa y ajusta un modelo sobre **tu** conjunto de datos.

### 1. Plantear el problema

En el `README.md`: qué predices, si es regresión o clasificación, qué decisión cambiaría la predicción y **qué columnas no puedes usar** porque no existirían en el momento de predecir.

### 2. Entrenar y comparar

- Un `Pipeline` con `ColumnTransformer` que incluya toda la preparación.
- Un **modelo de referencia** ingenuo (la media o la clase mayoritaria).
- Al menos **tres modelos** comparados en una tabla, con métricas de entrenamiento y de prueba.
- Validación cruzada con 5 particiones: media y dispersión.

### 3. Ajustar

`GridSearchCV` o `RandomizedSearchCV` sobre el mejor modelo, con al menos dos hiperparámetros. Documenta la rejilla, los mejores parámetros y la mejora obtenida.

### 4. Evaluar de verdad

- Métricas adecuadas al problema, explicadas en las unidades del objetivo.
- Si es clasificación: matriz de confusión, y una justificación escrita del umbral elegido.
- Métricas **por grupos** de al menos una variable categórica, con un comentario sobre dónde falla el modelo.
- Importancia por permutación de las variables.
- La curva de sobreajuste de un hiperparámetro, en un gráfico.

### 5. Entregar

- El código en el repositorio y el modelo guardado con `joblib`, junto a su JSON de métricas.
- Una **ficha del modelo** en el `README.md`, de entre 15 y 20 líneas: problema, datos, características usadas, modelo elegido, métricas, dónde falla, limitaciones y riesgos de uso.
- Defensa oral breve (5 minutos): explicar por qué elegiste ese modelo y qué harías para mejorarlo.

Fecha de entrega propuesta: 19/01/2027, al terminar la unidad.

### 6. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 3a | El problema está bien planteado y el tipo de aprendizaje, justificado |
| 3b | Pipeline correcto, sin fuga de datos, con tres modelos entrenados y comparados |
| 3c | Métricas adecuadas, interpretadas en unidades reales, con evaluación por grupos y comparación con el modelo ingenuo |
| 3d | Búsqueda de hiperparámetros documentada, con validación cruzada y mejora demostrada |

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 6.1 Qué es el ML | Datos y resultados producen reglas. Empieza siempre por un modelo ingenuo de referencia |
| 6.2 Preparar | `ColumnTransformer` + `Pipeline`. Todo lo que aprende va dentro, o hay fuga de datos |
| 6.3 Regresión | MAE en unidades reales, R² como contexto. El bosque suele ganar; el árbol sin podar memoriza |
| 6.4 Clasificación | La exactitud engaña con clases desbalanceadas: mira recall, precisión y la matriz de confusión |
| 6.4 Umbral | El 0,5 no es sagrado: el corte depende del coste de cada error, y eso lo decide el negocio |
| 6.5 Evaluar | Una partición no basta: validación cruzada con media y dispersión. `GridSearchCV` para los hiperparámetros |
| 6.6 No supervisado | k-means agrupa por distancia y exige escalado; el número de grupos lo valida su utilidad |
| 6.7 Comunicar | Importancia por permutación, error por grupos, pipeline guardado con joblib y predicción siempre con su margen |

## Bibliografía de la UD6

Todas las fuentes web se consultaron el 28 de septiembre de 2026.

### Documentación de scikit-learn

- scikit-learn developers. (2026). *Getting started*. <https://scikit-learn.org/stable/getting_started.html>
- scikit-learn developers. (2026). *User guide*: [Pipelines and composite estimators](https://scikit-learn.org/stable/modules/compose.html), [Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html), [Tuning the hyper-parameters of an estimator](https://scikit-learn.org/stable/modules/grid_search.html), [Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) y [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html).
- scikit-learn developers. (2026). *Common pitfalls and recommended practices*. <https://scikit-learn.org/stable/common_pitfalls.html>
- scikit-learn developers. (2026). *Model persistence*. <https://scikit-learn.org/stable/model_persistence.html>

### Artículos y libros

- Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
- Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
- Géron, A. *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow* (3.ª edición). Referencia habitual para ampliar; los cuadernos del libro están en <https://github.com/ageron/handson-ml3>.
