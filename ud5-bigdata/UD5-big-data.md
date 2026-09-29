# UD5 · Big Data

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [5.1 Qué es Big Data](#51-qué-es-big-data)
- [5.2 Impacto social: privacidad, sesgos y sostenibilidad](#52-impacto-social-privacidad-sesgos-y-sostenibilidad)
- [5.3 Dónde se guardan los datos](#53-dónde-se-guardan-los-datos)
- [5.4 Preprocesar a escala sin clúster](#54-preprocesar-a-escala-sin-clúster)
- [5.5 Procesamiento distribuido y en flujo](#55-procesamiento-distribuido-y-en-flujo)
- [5.6 Casos de uso por sectores](#56-casos-de-uso-por-sectores)
- [Práctica de la unidad · Hito 4 del proyecto integrador](#práctica-de-la-unidad--hito-4-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD5](#bibliografía-de-la-ud5)

## Presentación de la unidad

Cinco horas para entender qué cambia cuando los datos dejan de caber en el portátil. Es la unidad más conceptual del módulo, pero no es teoría sin manos: vas a generar un millón de filas y a comprobar, con el reloj en la mano, por qué un formato importa más que un ordenador más caro.

La idea que la recorre: **antes de montar un clúster, aprende a no necesitarlo**. Ajustar tipos, leer por trozos, guardar en Parquet y consultar con herramientas perezosas resuelve el 90 % de los casos que verás en una empresa mediana.

### Resultado de aprendizaje y criterios de evaluación

**RA4.** Comprende los principios del Big Data y su aplicación práctica en el análisis de datos.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 4a | Comprende los fundamentos del Big Data y su impacto en la sociedad | 5.1, 5.2 |
| 4b | Identifica los sistemas de almacenamiento y procesamiento de grandes volúmenes de datos | 5.3, 5.5 |
| 4d | Aplica técnicas de preprocesamiento a grandes volúmenes de datos | 5.4 |
| 4e | Analiza casos de uso de Big Data en distintos sectores | 5.6 |

El criterio 4c, consultas SQL y NoSQL a gran escala, se trabajó en la UD4.

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Lunes 30/11/2026 | 2 | 5.1 Qué es Big Data · 5.2 Impacto social · 5.3 Almacenamiento |
| 2 | Martes 01/12/2026 | 1 | 5.4 Preprocesar a escala |
| 3 | Lunes 14/12/2026 | 2 | 5.5 Distribuido y en flujo · 5.6 Casos de uso |

Los días 7 y 8 de diciembre son festivos.

### Antes de empezar

```bash
python -m pip install -r ud5-bigdata/requirements.txt

cd ud5-bigdata/listados
python generar_datos_grandes.py            # 1.000.000 de filas, unos 48 MB
```

El fichero de datos **no está en el repositorio**: lo genera cada uno en su portátil, y así puedes probar también con cinco millones de filas pasando el número como argumento.

Para el listado de PySpark necesitas Java 17 o 21 instalado (`java -version`). Los demás listados no lo necesitan.

> [!NOTE]
> PySpark todavía avisa de que no soporta del todo pandas 3. Solo afecta a convertir resultados con `toPandas()`; las operaciones sobre DataFrames de Spark, que son las de este apartado, funcionan con normalidad.

## 5.1 Qué es Big Data

No hay un umbral oficial de gigabytes. Hay Big Data cuando el volumen, la velocidad o la variedad de los datos obligan a **cambiar de herramientas**: cuando lo que hacías en un portátil ya no cabe, no llega a tiempo o no encaja en una tabla.

La formulación clásica son las tres uves, propuestas por Doug Laney en 2001 (Laney, 2001), a las que la industria añadió después dos más:

| Uve | Significa | Ejemplo |
| --- | --- | --- |
| **Volumen** | Cantidad de datos que hay que guardar y procesar | Los registros de todos los TPV de una cadena durante cinco años |
| **Velocidad** | Ritmo al que llegan y con el que hay que responder | Lecturas de sensores cada segundo; detección de fraude en el momento del pago |
| **Variedad** | Formatos distintos: tablas, texto, imágenes, registros, audio | Un historial clínico con analíticas, informes escritos y radiografías |
| **Veracidad** | Calidad e incertidumbre del dato | Encuestas con respuestas incoherentes, sensores mal calibrados |
| **Valor** | Lo que se obtiene realmente del análisis | Un dato que no cambia ninguna decisión no vale lo que cuesta guardarlo |

### De dónde salen los datos

- **Sistemas operacionales**: ventas, facturación, logística. Son las bases de datos de la UD4.
- **Registros de actividad**: servidores web, aplicaciones, clics, partidas de un juego.
- **Sensores y dispositivos (IoT)**: temperatura, consumo eléctrico, GPS, pulseras de actividad.
- **Fuentes externas y abiertas**: datos.gob.es, INE, AEMET, redes sociales, APIs.

### Del dato al valor

El recorrido es siempre el mismo, y coincide con el del curso: **capturar → almacenar → limpiar → analizar → modelar → decidir**. Big Data solo cambia las herramientas de cada paso, no el orden ni el sentido. Y el cuello de botella rara vez es el algoritmo: es la limpieza y el gobierno del dato.

> [!TIP]
> La pregunta que hay que hacer antes de comprar tecnología: **¿qué decisión va a cambiar con este dato?** Si no hay respuesta, no hay proyecto de datos; hay un almacén caro.

### Para practicar

1. Clasifica según las uves: la telemetría de un equipo de Fórmula 1, el censo de población, los mensajes de una red social, los datos de un molino de viento.
2. Estima cuántos datos genera al día una cadena de 50 tiendas con 5 cajas cada una, 400 tickets por caja y 8 líneas por ticket. ¿Es Big Data?
3. (A) Busca en datos.gob.es un conjunto de datos de más de 100 MB y describe en cinco líneas qué contiene, quién lo publica y con qué licencia.

## 5.2 Impacto social: privacidad, sesgos y sostenibilidad

Procesar datos a gran escala tiene consecuencias que no son técnicas. Este apartado es tan evaluable como el resto.

### Protección de datos

El **RGPD**, Reglamento (UE) 2016/679, se aplica a cualquier tratamiento de datos personales y se apoya en principios que condicionan el diseño técnico: licitud, **minimización** (recoger solo lo necesario), limitación de la finalidad, limitación del plazo de conservación, exactitud, integridad y responsabilidad proactiva. En España lo desarrolla la LOPDGDD (Ley Orgánica 3/2018) y lo supervisa la AEPD.

Tres consecuencias prácticas para un proyecto de datos:

- **Anonimizar o seudonimizar** cuanto antes. Un identificador de cliente es mejor que un nombre y un DNI.
- Cuidado con la **reidentificación**: el cruce de varios conjuntos «anónimos» puede volver a identificar a una persona. Código postal, fecha de nacimiento y sexo bastan a menudo.
- El derecho de supresión implica poder **borrar de verdad**, también de las copias, los backups y los modelos entrenados con esos datos.

### El Reglamento Europeo de Inteligencia Artificial

El Reglamento (UE) 2024/1689, conocido como AI Act, es la primera norma integral del mundo sobre IA. Entró en vigor el 1 de agosto de 2024 y se aplica de forma escalonada: prácticas prohibidas y alfabetización en IA desde el 2 de febrero de 2025, modelos de propósito general desde el 2 de agosto de 2025 y aplicación general desde el 2 de agosto de 2026 ([Gobierno de España, one.gob.es](https://one.gob.es/es/contenidos/el-reglamento-europeo-de-inteligencia-artificial-avanza-nuevas-obligaciones-para)).

En julio de 2026, el Reglamento (UE) 2026/1744, el «Ómnibus Digital sobre IA», reajustó el calendario: las obligaciones de los sistemas de alto riesgo del anexo III se trasladan al 2 de diciembre de 2027, y los integrados en productos ya regulados, a 2028; los sistemas generativos puestos en el mercado antes del 2 de agosto de 2026 tienen hasta el 2 de diciembre de 2026 para cumplir el marcado del contenido sintético ([Cuatrecasas](https://www.cuatrecasas.com/es/spain/propiedad-intelectual/art/se-publica-reglamento-omnibus-digital-ia)).

Lo que más te afecta como desarrollador:

- **Enfoque por niveles de riesgo**: prohibido, alto riesgo, riesgo limitado (transparencia) y riesgo mínimo. La obligación depende del uso, no de la tecnología.
- **Transparencia**: desde agosto de 2026, una persona tiene derecho a saber que está interactuando con un sistema de IA, y el contenido generado debe poder identificarse como tal.
- En España, la autoridad de supervisión es la **AESIA**.

### Sesgos

Un modelo aprende de los datos que le das, incluidos sus desequilibrios históricos. Si un conjunto de datos de contrataciones refleja que históricamente se contrató a menos mujeres para cierto puesto, el modelo aprenderá esa pauta y la aplicará al futuro con apariencia de objetividad. Los sesgos aparecen en el muestreo (a quién se midió), en las etiquetas (quién decidió qué era «bueno») y en el uso (a quién se aplica el resultado). Volveremos sobre esto en la UD6, al evaluar modelos por grupos.

### Sostenibilidad

Entrenar modelos grandes y mantener centros de datos consume electricidad y agua de refrigeración, y el crecimiento de la IA ha convertido ese consumo en un factor de planificación energética. A tu escala, la decisión sostenible y la eficiente coinciden: guardar en Parquet en vez de CSV, leer solo las columnas necesarias y no reentrenar un modelo sin motivo ahorra tiempo, dinero y energía.

### Para practicar

1. Tu proyecto integrador: ¿contiene datos personales? Si los tuviera, ¿qué harías antes de publicarlo en Streamlit?
2. Busca un caso real de algoritmo con sesgo documentado y resume en cinco líneas qué falló y en qué fase.
3. (A) Clasifica según el AI Act: un filtro de spam, un sistema de admisión universitaria, un chatbot de atención al cliente y un sistema de puntuación social. Justifica el nivel de riesgo.

## 5.3 Dónde se guardan los datos

### Sistemas de almacenamiento

| Sistema | Idea | Ejemplos |
| --- | --- | --- |
| Ficheros distribuidos | El fichero se parte en bloques repartidos y replicados en muchas máquinas | HDFS |
| Almacenamiento de objetos | Cada fichero es un objeto con su clave, accesible por red, barato y casi ilimitado | Amazon S3, Google Cloud Storage, Azure Blob |
| Bases de datos distribuidas | Datos repartidos entre nodos con consultas propias | Cassandra, MongoDB (UD4) |

Hoy, la mayoría de los proyectos nuevos se apoyan en almacenamiento de objetos: es barato, escala solo y cualquier herramienta lee de él.

### Arquitecturas: almacén, lago y lakehouse

| Arquitectura | Qué guarda | Cuándo se estructura | Para qué |
| --- | --- | --- | --- |
| **Data warehouse** | Datos ya limpios y modelados, en tablas | Al escribir | Informes y cuadros de mando fiables |
| **Data lake** | Todo tal cual llega: ficheros, registros, imágenes | Al leer | Explorar, ciencia de datos, datos que aún no sabes si usarás |
| **Lakehouse** | Ficheros del lago con capa de tablas, esquema y transacciones | Mixto | Unir ambos mundos: Delta Lake, Apache Iceberg |

El riesgo conocido del lago es convertirse en un pantano: datos sin catálogo, sin propietario y sin calidad, que nadie se atreve a usar. La diferencia entre lago y pantano es el **gobierno del dato**: catálogo, esquema, linaje y responsables.

### El formato importa más de lo que parece

**Listado 5.3.** CSV frente a Parquet · [ver fichero](listados/listado_5_03_parquet.py)

```python
ventas = pd.read_csv(CSV, sep=";", decimal=",", parse_dates=["fecha"])
ventas.to_parquet(PARQUET, compression="snappy")        # conserva los tipos

pd.read_parquet(PARQUET)                       # leer todo
pd.read_parquet(PARQUET, columns=["ciudad", "precio"])  # leer solo dos columnas
```

Resultado con un millón de filas:

```text
CSV:       47.9 MB
Parquet:    7.2 MB
Leer el CSV completo:        0.98 s
Leer el Parquet completo:    0.24 s
Leer 2 columnas del Parquet: 0.03 s
```

Siete veces menos espacio y treinta veces menos tiempo si solo necesitas dos columnas. La razón es que Parquet es **columnar**: guarda juntos todos los valores de una misma columna, lo que permite comprimir mucho mejor y leer solo lo que pides. Además conserva los tipos, así que no hay que volver a decirle que `fecha` es una fecha ([Apache Parquet](https://parquet.apache.org/docs/)).

| Formato | Úsalo para |
| --- | --- |
| CSV | Intercambiar con personas y con Excel. Nunca como almacén de trabajo |
| JSON | APIs y documentos anidados (UD4) |
| Parquet | Todo lo demás: es el formato por defecto de un proyecto de datos |

### Para practicar

1. Convierte tu conjunto de datos del proyecto a Parquet y compara tamaños y tiempos de lectura.
2. Guarda el mismo DataFrame en Parquet con `compression="snappy"` y con `compression="gzip"`. ¿Qué cambia?
3. (A) Busca qué es el *particionado* en Parquet (`partition_cols`) y explica cómo acelera una consulta que filtra por año.

## 5.4 Preprocesar a escala sin clúster

Aquí está el criterio 4d y la parte más útil de la unidad: técnicas para trabajar con ficheros grandes en un portátil normal.

### 1. Ajustar los tipos

**Listado 5.1.** Cuánta memoria ocupa un millón de filas · [ver fichero](listados/listado_5_01_memoria.py)

```python
tipos = {
    "id_venta": "int32",
    "ciudad": "category",      # texto con pocos valores distintos
    "producto": "category",
    "canal": "category",
    "unidades": "int8",
    "precio": "float32",
}

ligeras = pd.read_csv(RUTA, sep=";", decimal=",", parse_dates=["fecha"], dtype=tipos)
```

```text
Memoria con los tipos por defecto: 73.5 MB
Memoria con los tipos ajustados:   19.1 MB
```

Cuatro veces menos memoria sin perder un solo dato. El tipo `category` guarda cada texto distinto una vez y, en su lugar, un número por fila: ideal para columnas como ciudad, provincia o canal. Los enteros pequeños caben en `int8` o `int16`, y muchos decimales no necesitan la precisión de `float64`.

### 2. Leer por trozos

**Listado 5.2.** Procesar más datos de los que caben en memoria · [ver fichero](listados/listado_5_02_chunks.py)

```python
acumulado = pd.Series(dtype="float64")

for trozo in pd.read_csv(RUTA, sep=";", decimal=",", chunksize=200_000,
                         usecols=["ciudad", "unidades", "precio"]):
    trozo["importe"] = trozo["unidades"] * trozo["precio"]
    parcial = trozo.groupby("ciudad")["importe"].sum()
    acumulado = acumulado.add(parcial, fill_value=0)     # agregación incremental
```

`chunksize` convierte `read_csv` en un iterador: en cada vuelta hay en memoria 200.000 filas, no un millón. El patrón es el mismo que el de los generadores de la UD2, y es el que permite que este bucle funcione igual con un fichero de 50 GB. Combínalo con `usecols`: las columnas que no lees no ocupan nada.

> [!IMPORTANT]
> No todas las operaciones se pueden hacer por trozos. Sumas, recuentos, máximos y mínimos sí, porque son **agregables**. La mediana exacta o un `sort` global, no: hay que recurrir a herramientas que gestionen el desbordamiento a disco, como las de los dos apartados siguientes.

### 3. Herramientas perezosas: Polars

**Listado 5.4.** Evaluación perezosa · [ver fichero](listados/listado_5_04_polars.py)

```python
import polars as pl

consulta = (
    pl.scan_csv(CSV, separator=";", decimal_comma=True)      # scan_ = perezoso
    .with_columns((pl.col("unidades") * pl.col("precio")).alias("importe"))
    .group_by("ciudad")
    .agg(pl.col("importe").sum())
    .sort("importe", descending=True)
)
resultado = consulta.collect()        # aquí, y solo aquí, se ejecuta
```

```text
pandas: 0.86 s
polars: 0.18 s
```

`scan_csv` no lee nada: construye un **plan**. Al llamar a `collect()`, Polars optimiza ese plan y lo ejecuta en paralelo. El propio plan lo dice:

```text
Csv SCAN [datos/ventas_grandes.csv]
PROJECT 3/7 COLUMNS
```

Ha deducido que solo necesita 3 de las 7 columnas y ni siquiera lee las demás. Esa optimización se llama *projection pushdown*, y es la misma idea que aplica un motor SQL ([Polars user guide](https://docs.pola.rs/)).

### 4. SQL sobre ficheros: DuckDB

**Listado 5.5.** Consultar sin cargar · [ver fichero](listados/listado_5_05_duckdb.py)

```python
import duckdb

resumen = duckdb.sql(f"""
    SELECT ciudad,
           COUNT(*)                         AS ventas,
           ROUND(SUM(unidades * precio), 2) AS importe
    FROM '{PARQUET}'
    GROUP BY ciudad
    ORDER BY importe DESC
""").df()
```

DuckDB ejecuta SQL directamente sobre ficheros CSV o Parquet, sin servidor y sin importar nada: es «la SQLite del análisis». Acepta comodines (`'datos/*.parquet'` une todos los ficheros de una carpeta) y devuelve el resultado como DataFrame con `.df()` ([DuckDB documentation](https://duckdb.org/docs/)).

Si ya sabes SQL de la UD4, esta es la vía más rápida para explorar ficheros grandes.

### Resumen de decisiones

| Situación | Herramienta |
| --- | --- |
| Cabe en memoria con los tipos ajustados | pandas |
| No cabe, pero la operación es agregable | `chunksize` |
| No cabe y quieres rapidez sin complicarte | Polars perezoso o DuckDB |
| Ya sabes SQL y el dato está en ficheros | DuckDB |
| No cabe en **una** máquina | Spark (apartado 5.5) |

### Para practicar

1. Genera el fichero con cinco millones de filas y repite los listados 5.1, 5.2 y 5.4. ¿Cuál aguanta mejor?
2. Calcula con `chunksize` el importe medio por producto. ¿Puedes hacerlo sumando medias parciales? ¿Qué necesitas acumular realmente?
3. Escribe en DuckDB la consulta del listado 5.2 y compara los tiempos.
4. (A) Lee la guía *Scaling to large datasets* de pandas y resume tres técnicas que no hayamos visto aquí.

## 5.5 Procesamiento distribuido y en flujo

### Por lotes o en flujo

| | Por lotes (*batch*) | En flujo (*streaming*) |
| --- | --- | --- |
| Cuándo procesa | Cada cierto tiempo, sobre un conjunto cerrado | Según llegan los datos |
| Latencia | Minutos u horas | Segundos o menos |
| Ejemplo | Informe nocturno de ventas del día | Detección de fraude en el momento del pago |
| Herramientas | Spark, consultas programadas | Kafka, Spark Structured Streaming, Flink |

### La idea de MapReduce

El modelo que hizo posible el Big Data moderno lo publicaron Dean y Ghemawat en 2004: repartir el trabajo en dos fases, **map** (transformar cada dato de forma independiente en pares clave-valor) y **reduce** (combinar los valores de cada clave), de modo que el sistema pueda ejecutar el *map* en cientos de máquinas a la vez y tolerar que alguna falle.

Ese `groupby("ciudad")["importe"].sum()` que escribes en pandas es exactamente un map (calcular el importe de cada venta) seguido de un reduce (sumar por ciudad). La diferencia es dónde se ejecuta.

### Spark

Apache Spark es el sucesor práctico de MapReduce: mantiene los datos en memoria entre etapas y ofrece una API de DataFrames muy parecida a la de pandas. Es **perezoso**, como Polars: las transformaciones construyen un plan y solo una acción (`show`, `count`, `collect`) lo ejecuta.

**Listado 5.6.** PySpark en local · [ver fichero](listados/listado_5_06_pyspark.py)

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (SparkSession.builder.appName("ventas-ud5")
         .master("local[*]")          # todos los núcleos del portátil, como un clúster
         .getOrCreate())

ventas = spark.read.parquet("datos/ventas_grandes.parquet")

resumen = (
    ventas
    .withColumn("importe", F.col("unidades") * F.col("precio"))
    .groupBy("ciudad")
    .agg(F.count("*").alias("ventas"),
         F.round(F.sum("importe"), 2).alias("importe"))
    .orderBy(F.desc("importe"))
)
resumen.show()                       # nada se calcula hasta esta acción

ventas.createOrReplaceTempView("venta")      # y también acepta SQL
spark.sql("SELECT producto, SUM(unidades * precio) FROM venta GROUP BY producto").show()
```

Con un millón de filas, Spark tarda más que pandas: repartir el trabajo, serializar y coordinar cuesta tiempo. La ventaja aparece cuando el fichero no cabe en una máquina, porque el mismo código se ejecuta en un clúster cambiando solo `master`. Esa es la lección del listado: **Spark no es «pandas rápido», es «pandas repartido»**, y a pequeña escala sale perdiendo.

### Flujo con lo que ya sabes

**Listado 5.7.** Una pasada, memoria constante · [ver fichero](listados/listado_5_07_streaming.py)

```python
def flujo_de_ventas(ruta: Path) -> Iterator[dict]:
    """Simula un flujo de eventos: entrega una venta cada vez."""
    with ruta.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            fila["importe"] = int(fila["unidades"]) * float(fila["precio"].replace(",", "."))
            yield fila


ultimas = deque(maxlen=1000)          # ventana deslizante de los 1000 últimos eventos

for venta in flujo_de_ventas(RUTA):
    eventos += 1
    total += venta["importe"]
    ultimas.append(venta["importe"])
    if venta["importe"] > 10_000:
        alertas += 1
```

```text
  250,000 eventos | total    438.7 M€ | media últimos 1000:  1703.89 €
  500,000 eventos | total    876.7 M€ | media últimos 1000:  1852.96 €
  ...
Fin del flujo: 1,000,000 eventos, 13,894 ventas por encima de 10.000 €
```

Un millón de eventos procesados con unos pocos contadores y una cola de mil elementos en memoria. Esa es la esencia del procesamiento en flujo: **una sola pasada, estado acotado, ventanas deslizantes**. Un sistema real cambia el `for` por un consumidor de Kafka, pero el esquema mental es este.

### Para practicar

1. Añade al listado 5.7 una alerta cuando la media de la ventana suba un 20 % respecto a la ventana anterior.
2. Ejecuta el listado 5.6 con `.master("local[1]")` y con `local[*]`. ¿Cuánto cambia el tiempo?
3. (A) Explica por qué la mediana no se puede calcular en una pasada con memoria constante y busca qué es un algoritmo aproximado como t-digest.

## 5.6 Casos de uso por sectores

| Sector | Datos | Qué se hace | Cuidado con |
| --- | --- | --- | --- |
| Comercio | Tickets, web, fidelización | Recomendaciones, previsión de demanda, precios dinámicos | Discriminación de precios y rastreo del comportamiento |
| Salud | Historia clínica, imagen médica, sensores | Apoyo al diagnóstico, gestión de listas de espera, epidemiología | Datos de categoría especial: consentimiento y seguridad |
| Banca y seguros | Movimientos, contratos, scoring | Detección de fraude en tiempo real, riesgo crediticio | Sesgos que deniegan crédito a colectivos concretos |
| Industria | Sensores de máquinas, calidad | Mantenimiento predictivo, control de calidad por visión | Datos que no llegan o sensores descalibrados |
| Administración pública | Padrón, tráfico, tributos | Planificación de servicios, transparencia, datos abiertos | Reidentificación al publicar microdatos |
| Deporte | GPS, vídeo, eventos de partido | Rendimiento, prevención de lesiones, análisis táctico | Datos de salud de los deportistas |
| Ciudades inteligentes | Tráfico, consumo, calidad del aire | Semáforos adaptativos, gestión de residuos, contaminación | Videovigilancia y proporcionalidad |

Un patrón se repite en todos: el proyecto que funciona resuelve **una** pregunta concreta con datos que ya existen, y el que fracasa empieza comprando una plataforma para «tenerlo todo».

### Para practicar

1. Elige un sector y describe un caso: qué dato, qué pregunta, qué decisión y qué riesgo ético.
2. Busca un caso real publicado por una empresa española y resume su arquitectura en cinco líneas.
3. (A) Relaciona tu conjunto de datos del proyecto con uno de estos sectores y plantea qué otro dato te haría falta para pasar de describir a decidir.

## Práctica de la unidad · Hito 4 del proyecto integrador

Toca someter tu conjunto de datos a un «reto de escala».

### 1. Multiplicar tus datos

Escribe un script `escalar.py` que genere una versión ampliada de tu conjunto de datos, de al menos **dos millones de filas**, repitiendo y perturbando los datos reales (con `numpy`, como en [`generar_datos_grandes.py`](listados/generar_datos_grandes.py)). No lo subas al repositorio: sube el script y añade el fichero al `.gitignore`.

### 2. Medir y optimizar

Una tabla en tu `README.md` con mediciones reales de tu equipo:

| Prueba | Tiempo | Memoria o tamaño |
| --- | --- | --- |
| Lectura CSV con tipos por defecto | | |
| Lectura CSV con tipos ajustados | | |
| Tamaño en CSV frente a Parquet | | |
| Lectura Parquet completo y de 2 columnas | | |
| Agregación en pandas, por trozos, en Polars y en DuckDB | | |

### 3. Procesar en flujo

Un script que recorra tu conjunto ampliado como un flujo de eventos, con generadores, y mantenga al menos tres métricas en vivo y una alerta, con memoria acotada.

### 4. Escribir las conclusiones

Entre 10 y 15 líneas en el `README.md`:

- Qué técnica te dio mejor resultado y por qué.
- A partir de qué tamaño dejaría de servirte tu portátil.
- Qué arquitectura de almacenamiento elegirías si estos datos crecieran a 500 GB, y por qué.
- Un párrafo sobre el impacto social de tus datos: privacidad, sesgos o sostenibilidad, según corresponda.

### 5. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 4a | El párrafo de impacto identifica riesgos reales del conjunto de datos, no generalidades |
| 4b | La elección de almacenamiento y de herramienta está justificada con las mediciones |
| 4d | Tipos ajustados, lectura por trozos, Parquet y una herramienta perezosa, aplicados y medidos |
| 4e | El caso propio se relaciona con un sector y con una decisión concreta |

Fecha de entrega propuesta: antes del final de la UD6 (19/01/2027).

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 5.1 Qué es Big Data | No es un umbral de gigabytes: es cuando volumen, velocidad o variedad obligan a cambiar de herramientas |
| 5.2 Impacto | RGPD: minimizar y anonimizar. AI Act: obligaciones por nivel de riesgo, con transparencia desde agosto de 2026 |
| 5.3 Almacenamiento | Objetos en la nube, lago frente a almacén, y Parquet como formato por defecto: 7 veces menos espacio |
| 5.4 Preprocesar | Tipos ajustados (4 veces menos memoria), `chunksize`, Polars perezoso y DuckDB antes de pensar en un clúster |
| 5.5 Procesar | Map y reduce siguen siendo la idea. Spark no es pandas rápido, es pandas repartido. En flujo: una pasada y estado acotado |
| 5.6 Casos de uso | El proyecto que funciona responde una pregunta concreta con datos que ya existen |

## Bibliografía de la UD5

Todas las fuentes web se consultaron el 28 de septiembre de 2026.

### Artículos y documentos de referencia

- Laney, D. (2001). *3D Data Management: Controlling Data Volume, Velocity and Variety*. META Group Research Note.
- Dean, J. y Ghemawat, S. (2004). MapReduce: Simplified Data Processing on Large Clusters. *OSDI'04*.
- Zaharia, M. et al. (2012). Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing. *NSDI'12*.

### Normativa

- Reglamento (UE) 2016/679, General de Protección de Datos (RGPD). <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- Reglamento (UE) 2024/1689, de Inteligencia Artificial. <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- Gobierno de España. (2026). *El Reglamento europeo de Inteligencia Artificial avanza: nuevas obligaciones para empresas y proveedores*. <https://one.gob.es/es/contenidos/el-reglamento-europeo-de-inteligencia-artificial-avanza-nuevas-obligaciones-para>
- Cuatrecasas. (2026). *Se publica el Reglamento Ómnibus Digital sobre IA* [Reglamento (UE) 2026/1744]. <https://www.cuatrecasas.com/es/spain/propiedad-intelectual/art/se-publica-reglamento-omnibus-digital-ia>

### Documentación técnica

- Apache Parquet. *Documentation*. <https://parquet.apache.org/docs/>
- Apache Spark. *PySpark documentation*. <https://spark.apache.org/docs/latest/api/python/>
- Polars. *User guide*. <https://docs.pola.rs/>
- DuckDB. *Documentation*. <https://duckdb.org/docs/>
- pandas development team. *Scaling to large datasets*. <https://pandas.pydata.org/docs/user_guide/scale.html>
