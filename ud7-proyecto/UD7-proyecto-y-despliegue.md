# UD7 · Proyecto integrador, despliegue y evaluación

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [7.1 Cómo se organiza un proyecto de datos](#71-cómo-se-organiza-un-proyecto-de-datos)
- [7.2 Del notebook al paquete](#72-del-notebook-al-paquete)
- [7.3 La aplicación: panel y predictor](#73-la-aplicación-panel-y-predictor)
- [7.4 Desplegar en Streamlit Community Cloud](#74-desplegar-en-streamlit-community-cloud)
- [7.5 Documentar: README y ficha del modelo](#75-documentar-readme-y-ficha-del-modelo)
- [7.6 Día en la Oficina y defensa](#76-día-en-la-oficina-y-defensa)
- [Entrega final del proyecto integrador](#entrega-final-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD7](#bibliografía-de-la-ud7)

## Presentación de la unidad

Nueve horas para convertir lo que tienes en algo que otra persona pueda usar. No hay contenidos nuevos de biblioteca: hay oficio. Recoger seis meses de trabajo disperso en notebooks y dejarlo en un repositorio ordenado, con pruebas, documentación y una aplicación publicada con su enlace.

En esta carpeta tienes [`proyecto-ejemplo/`](proyecto-ejemplo/), un proyecto completo y funcionando que sirve de referencia: mira cómo está montado y monta el tuyo igual, con tus datos y tu modelo.

### Resultado de aprendizaje y criterio de evaluación

**RA3.** Aplica conceptos básicos de Machine Learning en problemas reales.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 3e | Desarrolla un proyecto integrador que combine análisis de datos, Machine Learning y programación en Python | Toda la unidad |

La unidad es además transversal: se evalúan aquí los CE de los RA1, RA2 y RA4 aplicados al proyecto completo.

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Lunes 25/01/2027 | 2 | 7.1 Organización · 7.2 Del notebook al paquete |
| 2 | Martes 26/01/2027 | 1 | 7.2 Pruebas y reproducibilidad |
| 3 | Lunes 01/02/2027 | 2 | 7.3 La aplicación |
| 4 | Martes 02/02/2027 | 1 | 7.4 Despliegue |
| 5 | Lunes 08/02/2027 | 2 | **Día en la Oficina** (sin IA) |
| 6 | Martes 09/02/2027 | 1 | 7.5 Documentación y ficha del modelo |

Los días 15 y 16 de febrero quedan de reserva: defensas orales y margen para lo que se haya desviado durante el curso.

### Lo que traes de las unidades anteriores

| Hito | Unidad | Lo que produjo |
| --- | --- | --- |
| 0 | UD1 | Conjunto de datos elegido y explorador en Python puro |
| 1 | UD2 | Explorador refactorizado a objetos |
| 2 | UD3 | Datos limpios, análisis exploratorio y primer panel publicado |
| 3 | UD4 | Datos en una base de datos y consultas |
| 4 | UD5 | Prueba de escala y conclusiones sobre el volumen |
| 5 | UD6 | Modelo entrenado, evaluado y ajustado |

En esta unidad todo eso se une en un único repositorio coherente.

## 7.1 Cómo se organiza un proyecto de datos

### El ciclo de trabajo

La metodología clásica del sector, CRISP-DM, describe seis fases que se recorren **en bucle**, no en línea recta:

| Fase | Pregunta | Dónde la trabajaste |
| --- | --- | --- |
| Comprensión del negocio | ¿Qué decisión hay que tomar? | Hito 0 |
| Comprensión de los datos | ¿Qué tengo y qué calidad tiene? | UD1, UD3 |
| Preparación de los datos | ¿Cómo lo dejo listo para modelar? | UD3, UD4 |
| Modelado | ¿Qué algoritmo y qué parámetros? | UD6 |
| Evaluación | ¿Sirve para la decisión inicial? | UD6 |
| Despliegue | ¿Cómo llega a quien lo usa? | UD7 |

Volver atrás no es un fracaso: evaluar suele revelar que faltan datos o que la pregunta estaba mal planteada, y eso devuelve a la primera fase.

### La estructura del repositorio

```text
proyecto/
├── datos/                    datos de partida y procesados
├── modelos/                  modelo entrenado y su ficha de métricas
├── notebooks/                exploración: se lee, no se ejecuta en producción
├── src/<paquete>/            el código que de verdad se reutiliza
├── scripts/                  entrada por terminal: entrenar, cargar datos
├── tests/                    pruebas automáticas
├── app/                      la aplicación Streamlit
├── requirements.txt
├── pyproject.toml
└── README.md
```

La regla que ordena todo esto: **los notebooks exploran, los módulos producen**. Un notebook es un cuaderno de laboratorio, perfecto para probar y para enseñar un análisis; pero el código del que dependen la aplicación y el entrenamiento vive en `src/`, donde se puede importar, probar y versionar.

### Reproducibilidad

Que otra persona, o tú dentro de seis meses, obtenga exactamente los mismos resultados:

- **Semillas fijas** en particiones y modelos (`random_state=42`).
- **Versiones fijadas** en `requirements.txt`.
- **Entrenamiento en un script**, no a mano en celdas de un notebook.
- **Datos versionados o reproducibles**: el fichero original intacto, y el procesado generado por código.
- **Nada de rutas absolutas**: siempre `Path(__file__)` o rutas relativas a la raíz del proyecto.

### Para practicar

1. Dibuja el ciclo CRISP-DM de tu proyecto marcando en qué fases has tenido que volver atrás.
2. Revisa tu repositorio actual: ¿qué ficheros no encajan en la estructura de arriba?
3. (A) Borra tu entorno virtual, recréalo desde `requirements.txt` y comprueba que todo sigue funcionando. Si algo falla, falta en el fichero.

## 7.2 Del notebook al paquete

### Una sola definición de cada cosa

El error más común al recoger el trabajo de varios meses es tener la limpieza repetida en tres sitios: el notebook, la aplicación y el script de entrenamiento. En cuanto cambia una decisión, dejan de coincidir.

**Listado 7.1.** `src/ventas_ia/datos.py`: toda la limpieza, en un sitio · [ver fichero](proyecto-ejemplo/src/ventas_ia/datos.py)

```python
def cargar_limpio(ruta: Path = RUTA_POR_DEFECTO) -> pd.DataFrame:
    """Devuelve el DataFrame de ventas limpio y listo para modelar."""
    if not ruta.exists():
        raise FileNotFoundError(f"No se encuentra el fichero de datos: {ruta}")

    ventas = pd.read_csv(ruta, sep=";", decimal=",")
    ventas = ventas.drop_duplicates()
    ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()
    ventas["canal"] = ventas["canal"].fillna("desconocido")
    ventas = ventas.dropna(subset=["unidades", "precio"])
    ventas["unidades"] = ventas["unidades"].astype("int64")
    ventas["importe"] = (ventas["unidades"] * ventas["precio"]).round(2)

    logger.info("Datos cargados: %d filas", len(ventas))
    return ventas
```

**Listado 7.2.** `src/ventas_ia/modelo.py`: construir, entrenar y guardar · [ver fichero](proyecto-ejemplo/src/ventas_ia/modelo.py)

```python
NUMERICAS = ["mes", "descuento", "precio"]
CATEGORICAS = ["ciudad", "producto", "canal"]
CARACTERISTICAS = NUMERICAS + CATEGORICAS
OBJETIVO = "unidades"
SEMILLA = 42


def construir_pipeline(**parametros) -> Pipeline:
    """Devuelve el pipeline completo: preparación + modelo, sin entrenar."""
    ...


def entrenar(ventas: pd.DataFrame, **parametros) -> tuple[Pipeline, pd.DataFrame, pd.Series]:
    """Entrena el pipeline y devuelve el modelo y el conjunto de prueba."""
    ...


def guardar(modelo: Pipeline, metricas: dict, ruta: Path = RUTA_MODELO) -> None:
    """Guarda el pipeline y su ficha de métricas."""
    ...
```

Las constantes en mayúsculas al principio del módulo evitan el peor error de producción: que la aplicación mande las columnas en otro orden o con otro nombre que el modelo espera. La aplicación importa `CARACTERISTICAS` y no puede equivocarse.

**Listado 7.3.** `scripts/entrenar.py`: el entrenamiento, reproducible · [ver fichero](proyecto-ejemplo/scripts/entrenar.py)

```python
def main() -> None:
    ventas = cargar_limpio()
    modelo, X_prueba, y_prueba = entrenar(ventas)
    prediccion = modelo.predict(X_prueba)

    resultados = metricas(y_prueba, prediccion)
    print("Métricas en el conjunto de prueba:", resultados)
    print(metricas_por_grupo(X_prueba, y_prueba, prediccion, "producto"))

    guardar(modelo, resultados)
```

Salida real del proyecto de ejemplo:

```text
Métricas en el conjunto de prueba: {'mae': 1.544, 'rmse': 2.184, 'r2': 0.801}

Error por producto:
           casos   mae  sesgo
ratón      253.0  2.56   0.17
teclado    299.0  2.36  -0.12
portátil   261.0  0.76   0.12
```

### Pruebas: que el proyecto se defienda solo

No hacen falta muchas. Con cuatro que comprueben lo esencial ya detectas el 90 % de los desastres.

**Listado 7.4.** `tests/test_proyecto.py` · [ver fichero](proyecto-ejemplo/tests/test_proyecto.py)

```python
def test_los_datos_no_tienen_nulos_en_las_caracteristicas(ventas):
    assert ventas[CARACTERISTICAS].isna().sum().sum() == 0


def test_el_modelo_supera_al_ingenuo(ventas):
    modelo, X_prueba, y_prueba = entrenar(ventas)
    resultado = metricas(y_prueba, modelo.predict(X_prueba))
    error_ingenuo = (y_prueba - ventas["unidades"].mean()).abs().mean()
    assert resultado["mae"] < error_ingenuo


def test_el_modelo_predice_un_caso_nuevo(ventas):
    modelo, _, _ = entrenar(ventas)
    caso = pd.DataFrame([{"mes": 6, "descuento": 0.1, "precio": 180.0,
                          "ciudad": "Granada", "producto": "monitor", "canal": "online"}])
    assert 0 < modelo.predict(caso)[0] < 100
```

```bash
python -m pytest -q      # 4 passed in 4.49s
```

Las dos primeras son **pruebas de datos**: si mañana el fichero llega con nulos o con unidades negativas, saltan antes de que el modelo aprenda basura. Las otras dos son **pruebas de humo**: el modelo entrena, predice y bate a la referencia ingenua.

> [!TIP]
> Cada vez que arregles un fallo, escribe antes la prueba que lo detecta. Así tienes la garantía de que no vuelve, y de paso documentas el problema.

### Para practicar

1. Mueve al paquete la limpieza que tengas repetida en notebooks y en la aplicación.
2. Escribe tres pruebas para tus datos: rangos válidos, columnas obligatorias y ausencia de duplicados.
3. (A) Añade una prueba que compruebe que el pipeline guardado y recargado con `joblib` predice lo mismo que el original.

## 7.3 La aplicación: panel y predictor

**Listado 7.5.** `app/app.py`, en tres pestañas · [ver fichero](proyecto-ejemplo/app/app.py)

```python
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "src"))      # así lo encuentra también Streamlit Cloud

from ventas_ia import cargar_limpio, cargar_modelo


@st.cache_data                      # datos: se copian y se cachean por valor
def datos() -> pd.DataFrame:
    return cargar_limpio(RAIZ / "datos" / "ventas_ml.csv")


@st.cache_resource                  # modelo: objeto vivo, una sola copia
def modelo_y_metricas():
    return cargar_modelo(RAIZ / "modelos" / "modelo.joblib")


panel, predictor, acerca_de = st.tabs(["Panel", "Predicción", "Sobre el modelo"])
```

La estructura en pestañas responde a tres preguntas distintas de quien la usa: **qué pasó** (panel de la UD3), **qué pasará** (predictor de la UD6) y **cuánto me puedo fiar** (ficha del modelo).

Tres detalles que separan una aplicación de un ejercicio:

```python
st.metric("Unidades estimadas", f"{prediccion:.1f}",
          help=f"Intervalo orientativo: {max(prediccion - margen, 0):.1f} – "
               f"{prediccion + margen:.1f}")
st.caption(f"Error medio del modelo en datos no vistos: ±{margen} unidades")

if precio > ventas["precio"].max():
    st.warning(f"El precio introducido supera el máximo visto al entrenar: "
               f"la predicción es poco fiable.")
```

1. **La predicción va con su margen.** Una cifra sola invita a creérsela.
2. **Avisa cuando le preguntas algo fuera de rango.** Un modelo no extrapola: inventa.
3. **Falla con elegancia.** Si no hay modelo entrenado, la aplicación lo dice y sigue funcionando el panel, en lugar de reventar con un *traceback* delante del usuario.

> [!IMPORTANT]
> `@st.cache_data` copia el resultado y sirve para DataFrames; `@st.cache_resource` devuelve siempre el mismo objeto y es lo que hay que usar para modelos y conexiones. Cachear un modelo con `cache_data` lo copiaría en cada sesión y consumiría memoria sin necesidad.

### Para practicar

1. Añade a tu aplicación la pestaña «Sobre el modelo» con su ficha leída del JSON de métricas.
2. Añade un aviso cuando alguna entrada quede fuera del rango de entrenamiento.
3. (A) Añade un botón que descargue en CSV las predicciones de un lote de casos subido por el usuario con `st.file_uploader`.

## 7.4 Desplegar en Streamlit Community Cloud

Repaso del apartado 3.8, ahora con el modelo dentro. El servicio es gratuito para aplicaciones públicas y se alimenta de un repositorio de GitHub; necesita el fichero de la aplicación y un `requirements.txt`, en la raíz o junto a la aplicación ([Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)).

### Pasos

1. Sube el repositorio a GitHub, incluido `modelos/modelo.joblib` si pesa poco (el del ejemplo ocupa 4,1 MB).
2. Entra en [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
3. Elige repositorio, rama y ruta del fichero principal (`app/app.py`).
4. Espera a la instalación y prueba la URL pública desde el móvil.
5. Pega el enlace en el `README.md`.

### Lo que suele salir mal

| Síntoma | Causa habitual | Solución |
| --- | --- | --- |
| `ModuleNotFoundError: ventas_ia` | El paquete no está instalado en la nube | La línea `sys.path.insert` del listado 7.5 |
| El modelo no carga y da error de versión | Entrenaste con otra versión de scikit-learn | Fija en `requirements.txt` la versión de la ficha del modelo |
| `FileNotFoundError` con los datos | Ruta relativa a tu carpeta de trabajo | `Path(__file__).parent` |
| La aplicación va muy lenta | Se recargan datos o modelo en cada interacción | `@st.cache_data` y `@st.cache_resource` |
| El modelo no está en el repositorio | Lo excluyó `.gitignore` | Súbelo si es pequeño, o entrénalo al arrancar si es grande |

Tienes la lista completa en [`plantillas/checklist-despliegue.md`](plantillas/checklist-despliegue.md).

> [!WARNING]
> La aplicación es pública y se ejecuta en servidores de Estados Unidos. Ningún dato personal, ninguna credencial en el código y ningún fichero interno del centro. Lo que se publica, se publica para todo el mundo.

### Para practicar

1. Despliega tu aplicación y ábrela en un dispositivo donde no hayas iniciado sesión.
2. Provoca a propósito el error de versión de scikit-learn y lee el mensaje completo.
3. (A) Consulta los límites de recursos de Community Cloud y estima si tu modelo cabe.

## 7.5 Documentar: README y ficha del modelo

El `README.md` es la portada del proyecto y lo único que muchos van a leer. Debe permitir a otra persona **ejecutar tu proyecto sin preguntarte nada**:

1. Qué hace y para qué, en dos líneas.
2. Enlace a la aplicación publicada.
3. Puesta en marcha: clonar, entorno, dependencias, entrenar, ejecutar.
4. Estructura de carpetas comentada.
5. Origen, licencia y limpieza de los datos.
6. Los cinco hallazgos del análisis.
7. La **ficha del modelo**.

Tienes el ejemplo completo en [`proyecto-ejemplo/README.md`](proyecto-ejemplo/README.md) y la plantilla en [`plantillas/ficha-modelo.md`](plantillas/ficha-modelo.md).

### Por qué una ficha del modelo

Porque un modelo sin documentación es una caja negra que alguien acabará usando para algo que no toca. La ficha contesta por adelantado: qué predice, con qué datos aprendió, cuánto se equivoca, **dónde se equivoca más** y para qué no debe usarse. La idea viene de las *model cards* (Mitchell et al., 2019) y hoy es práctica estándar, además de un requisito de transparencia en el marco europeo que vimos en la UD5.

Fíjate en las dos filas que más cuestan y más valen:

| Campo | Ejemplo real del proyecto |
| --- | --- |
| Dónde falla | MAE 2,56 en ratón y 2,36 en teclado, frente a 0,76 en portátil |
| Límites de uso | No extrapola a precios o productos no vistos. No explica causas: no sirve para fijar precios |

### Para practicar

1. Escribe tu ficha del modelo con la plantilla y enséñasela a un compañero: ¿entiende qué hace y qué no?
2. Revisa tu `README.md` con los siete puntos de arriba y marca lo que falta.
3. (A) Añade una sección «Trabajo futuro» con tres mejoras concretas y el porqué de cada una.

## 7.6 Día en la Oficina y defensa

### Día en la Oficina (2 horas, sin ayuda de IA)

Trabajo individual en el aula, sobre tu propio proyecto y con la documentación oficial abierta. El enunciado se entrega ese día e incluye tres tareas del estilo de estas:

1. **Análisis:** responder con código a una pregunta nueva sobre los datos y presentarla en un gráfico correcto.
2. **Modelo:** añadir una característica, reentrenar, comparar métricas con las anteriores y decidir si se queda.
3. **Aplicación:** añadir un control a la interfaz y hacer que afecte al resultado.

Se evalúa lo de siempre: que el código funcione, que esté ordenado y que sepas explicar **por qué** hiciste cada cosa.

### Defensa oral (10 minutos)

| Parte | Minutos | Contenido |
| --- | --- | --- |
| El problema | 2 | Qué datos, qué pregunta y qué decisión |
| Demostración | 3 | La aplicación publicada, en directo |
| El modelo | 3 | Qué elegiste, qué métricas tiene y dónde falla |
| Preguntas | 2 | Sobre cualquier línea de tu código |

Tres preguntas que caerán seguro: por qué elegiste ese modelo y no otro; qué harías si el error fuera el doble; y qué columna no podías usar, y por qué.

> [!TIP]
> Prepara la demostración con la aplicación ya abierta y un caso de ejemplo pensado. Y ensaya en voz alta la respuesta a «¿dónde falla tu modelo?»: reconocer los límites suma, no resta.

## Entrega final del proyecto integrador

### Qué se entrega

| Elemento | Requisitos |
| --- | --- |
| Repositorio | Estructura del apartado 7.1, `requirements.txt` con versiones, sin credenciales |
| Paquete `src/` | Limpieza, modelo y evaluación, sin código duplicado en notebooks |
| Notebook de exploración | El de la UD3, actualizado y con texto que explique cada gráfico |
| Base de datos | Script de creación y consultas de la UD4 |
| Prueba de escala | Script y mediciones de la UD5 |
| Modelo | Entrenado desde `scripts/entrenar.py`, guardado con su JSON de métricas |
| Pruebas | Al menos cuatro, que pasen con `pytest` |
| Aplicación | Publicada, con panel, predictor y ficha del modelo |
| `README.md` | Los siete puntos del apartado 7.5, con el enlace a la aplicación |

Fecha de entrega propuesta: **lunes 08/02/2027**, antes del Día en la Oficina. Defensas los días 9, 15 y 16 de febrero.

### Rúbrica orientativa

| Criterio | Qué se mira | Peso |
| --- | --- | --- |
| Datos y análisis (RA2) | Limpieza justificada, análisis exploratorio con conclusiones, consultas a la base de datos | 25 % |
| Modelo (RA3) | Pipeline sin fugas, modelos comparados, ajuste, métricas adecuadas y evaluación por grupos | 30 % |
| Código y proyecto (RA1) | Paquete organizado, funciones documentadas, pruebas, reproducibilidad | 20 % |
| Aplicación y despliegue (RA3.e) | Aplicación publicada, usable, con márgenes de error y avisos | 15 % |
| Documentación y defensa | `README.md`, ficha del modelo y claridad al explicarlo | 10 % |

El Día en la Oficina se evalúa aparte, con la rúbrica común del ciclo.

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 7.1 Organización | CRISP-DM se recorre en bucle. Los notebooks exploran, los módulos producen |
| 7.1 Reproducibilidad | Semillas fijas, versiones fijadas, entrenamiento en script y rutas relativas |
| 7.2 Paquete | Una sola definición de la limpieza y de las características, importada por todos |
| 7.2 Pruebas | Cuatro pruebas bien elegidas: datos válidos, modelo que entrena, predice y bate al ingenuo |
| 7.3 Aplicación | Panel, predictor y ficha. Predicción con margen, aviso fuera de rango y fallo elegante |
| 7.4 Despliegue | `requirements.txt` con versiones, misma versión de scikit-learn, rutas con `Path(__file__)` |
| 7.5 Documentación | El README permite ejecutar el proyecto sin preguntar. La ficha dice dónde falla el modelo |
| 7.6 Evaluación | Día en la Oficina sin IA y defensa de 10 minutos sobre tu propio código |

## Bibliografía de la UD7

Todas las fuentes web se consultaron el 28 de septiembre de 2026.

### Documentación

- Snowflake Inc. (2026). *Deploy on Streamlit Community Cloud*. <https://docs.streamlit.io/deploy/streamlit-community-cloud>
- Snowflake Inc. (2026). *Caching overview* (`st.cache_data` y `st.cache_resource`). <https://docs.streamlit.io/develop/concepts/architecture/caching>
- pytest developers. (2026). *pytest documentation*. <https://docs.pytest.org/>
- scikit-learn developers. (2026). *Model persistence*. <https://scikit-learn.org/stable/model_persistence.html>

### Artículos

- Mitchell, M. et al. (2019). Model Cards for Model Reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\* '19)*, 220-229.
- Wirth, R. y Hipp, J. (2000). CRISP-DM: Towards a Standard Process Model for Data Mining. *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining*.
