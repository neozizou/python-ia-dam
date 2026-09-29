# UD3 · Análisis de datos con Python

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [3.1 NumPy: el motor que hay debajo](#31-numpy-el-motor-que-hay-debajo)
- [3.2 pandas: cargar e inspeccionar](#32-pandas-cargar-e-inspeccionar)
- [3.3 Seleccionar y filtrar](#33-seleccionar-y-filtrar)
- [3.4 Limpiar los datos](#34-limpiar-los-datos)
- [3.5 Transformar: columnas, grupos y uniones](#35-transformar-columnas-grupos-y-uniones)
- [3.6 Visualizar: matplotlib y seaborn](#36-visualizar-matplotlib-y-seaborn)
- [3.7 Análisis exploratorio](#37-análisis-exploratorio)
- [3.8 De los datos a la decisión: Streamlit](#38-de-los-datos-a-la-decisión-streamlit)
- [Práctica de la unidad · Hito 2 del proyecto integrador](#práctica-de-la-unidad--hito-2-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD3](#bibliografía-de-la-ud3)

## Presentación de la unidad

Es la unidad más larga del módulo: 10 horas. En la UD1 agrupaste ventas por ciudad con un diccionario y veinte líneas de código; aquí lo harás con una línea de pandas sobre 1.200 filas, y el mismo código serviría para 1.200.000. Al final publicarás en internet tu primer panel interactivo.

El orden sigue el ciclo real del dato: cargar, mirar, limpiar, transformar, visualizar, interpretar y comunicar. La limpieza ocupa buena parte de la unidad porque es donde de verdad se va el tiempo en un proyecto de datos.

### Resultado de aprendizaje y criterios de evaluación

**RA2.** Utiliza herramientas de análisis y procesamiento de datos con Python.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 2a | Carga, limpia y estructura conjuntos de datos con bibliotecas de Python | 3.1, 3.2, 3.3, 3.4, 3.5 |
| 2b | Representa gráficamente los datos para facilitar su interpretación | 3.6 |
| 2c | Realiza análisis exploratorios para identificar patrones y tendencias | 3.7 |
| 2e | Interpreta los resultados del análisis para apoyar la toma de decisiones | 3.7, 3.8 |

El criterio 2d, consultas a bases de datos, se trabaja en la UD4.

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Martes 20/10/2026 | 1 | 3.1 NumPy |
| 2 | Lunes 26/10/2026 | 2 | 3.2 Cargar e inspeccionar · 3.3 Seleccionar y filtrar |
| 3 | Martes 27/10/2026 | 1 | 3.4 Nulos, duplicados y texto |
| 4 | Martes 03/11/2026 | 1 | 3.4 Atípicos · 3.5 Columnas derivadas |
| 5 | Lunes 09/11/2026 | 2 | 3.5 Agrupaciones, tablas dinámicas, uniones y series temporales |
| 6 | Martes 10/11/2026 | 1 | 3.6 Visualización |
| 7 | Lunes 16/11/2026 | 2 | 3.7 Análisis exploratorio · 3.8 Streamlit y despliegue |

El lunes 02/11 es festivo.

### Antes de empezar: instalar las dependencias

Con el entorno virtual del proyecto activado (apartado 1.1):

```bash
python -m pip install -r ud3-datos/requirements.txt
```

El fichero fija las versiones con las que están probados todos los listados:

```text
numpy==2.4.4
pandas==3.0.2
matplotlib==3.10.8
seaborn==0.13.2
streamlit==1.64.0
openpyxl==3.1.5
pyarrow==25.0.1
```

> [!NOTE]
> **pandas 3.** Desde la versión 3.0, las columnas de texto tienen el tipo `str` en lugar del antiguo `object`. Si consultas tutoriales anteriores a 2026 verás `object` en las salidas de `dtypes` e `info()`. Es el mismo contenido con un nombre mejor.

### Cómo usar esta carpeta

| Carpeta | Contenido |
| --- | --- |
| [`listados/`](listados/) | Los 20 listados de la unidad. `comun.py` reúne la carga y la limpieza que reutilizan los listados a partir del 3.11 |
| [`listados/datos/`](listados/datos/) | `ventas_2026.csv` (1.215 filas, con suciedad deliberada) y `ciudades.csv` |
| [`app/`](app/) | La aplicación Streamlit completa, lista para desplegar |

El fichero de datos lo genera [`generar_datos.py`](listados/generar_datos.py), por si quieres cambiar su tamaño o la cantidad de errores que contiene.

## 3.1 NumPy: el motor que hay debajo

pandas está construido sobre NumPy, así que conviene entender la idea básica: un **array** es una secuencia homogénea y de tamaño fijo sobre la que las operaciones se aplican a todos los elementos a la vez, sin bucles. Eso se llama **vectorización** ([NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)).

**Listado 3.1.** Vectorización frente a bucles · [ver fichero](listados/listado_3_01_numpy.py)

```python
import numpy as np

precios = np.array([899.90, 180.00, 25.00, 12.50])
unidades = np.array([3, 2, 10, 5])

importes = precios * unidades          # operación elemento a elemento, sin bucle
print(importes)                        # [2699.7  360.    250.     62.5]
print(importes.sum(), importes.mean(), importes.max())
print(importes[importes > 300])        # máscara booleana: filtra sin bucle
```

El listado completo compara el tiempo de multiplicar cinco millones de números con un bucle de Python y con NumPy. La diferencia es de un orden de magnitud, y crece con el tamaño: NumPy guarda los datos en un bloque contiguo de memoria y ejecuta el cálculo en código compilado.

> [!NOTE]
> **Desde C++.** Un array de NumPy es lo más parecido a un `std::vector<double>` con operaciones aritméticas ya definidas. La diferencia con una lista de Python es que la lista guarda punteros a objetos dispersos por la memoria; el array, los números en bruto y seguidos.

Dos detalles que reaparecerán todo el curso:

- **`NaN`** (*not a number*) representa un valor ausente en columnas numéricas. Cualquier operación con `NaN` da `NaN`, por eso existen `np.nansum`, y en pandas casi todas las funciones lo ignoran por defecto.
- Las **máscaras booleanas** (`array[array > 300]`) son la forma de filtrar en NumPy y en pandas.

### Para practicar

1. Crea un array con las notas `[6.5, 4.0, 9.1, 7.25, 5.0]` y calcula media, desviación típica (`std`) y cuántas superan la media.
2. Con `np.arange(1, 13)`, obtén el array de los meses y, con una máscara, quédate con los del segundo semestre.
3. (A) Repite la comparación de tiempos del listado 3.1 con 50 millones de elementos. ¿Crece la ventaja de NumPy?

## 3.2 pandas: cargar e inspeccionar

Un `DataFrame` es una tabla: filas con índice y columnas con nombre y tipo. Una columna suelta es una `Series`. Casi todo el trabajo consiste en encadenar operaciones que devuelven nuevos DataFrames ([pandas: 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)).

**Listado 3.2.** Cargar un CSV y mirarlo por primera vez · [ver fichero](listados/listado_3_02_leer_csv.py)

```python
from pathlib import Path

import pandas as pd

ruta = Path("datos") / "ventas_2026.csv"

ventas = pd.read_csv(
    ruta,
    sep=";",                    # separador español
    decimal=",",                # coma decimal: 809,91 -> 809.91
    parse_dates=["fecha"],      # convierte la columna a fechas
    encoding="utf-8",
)

print(ventas.shape)             # (1215, 8)
print(ventas.head(3))
print(ventas.dtypes)
```

En la UD1 escribiste una función para convertir `"809,91"` en `809.91`. Aquí es un parámetro. `read_csv` tiene decenas: `usecols`, `nrows`, `skiprows`, `na_values`, `dtype`, `thousands`, `chunksize`. Antes de programar una limpieza, comprueba si `read_csv` ya la hace.

| Función hermana | Formato |
| --- | --- |
| `pd.read_excel` | `.xlsx` (necesita `openpyxl`) |
| `pd.read_json` | JSON |
| `pd.read_parquet` | Parquet, columnar y comprimido (UD5) |
| `pd.read_sql` | Resultado de una consulta SQL (UD4) |

**Listado 3.3.** Series, DataFrame y primera inspección · [ver fichero](listados/listado_3_03_inspeccion.py)

```python
print(type(ventas["precio"]), type(ventas[["ciudad", "precio"]]))   # Series, DataFrame

print(ventas.info())                      # tipos, nulos y memoria
print(ventas.describe())                  # estadísticos de las columnas numéricas
print(ventas["producto"].value_counts())  # recuento por categoría
print(ventas["ciudad"].nunique(), "ciudades distintas")
```

Estos cuatro métodos son el primer contacto con cualquier conjunto de datos. `info()` ya te avisa de dos problemas en nuestro fichero: `canal` tiene 1.175 valores no nulos de 1.215, y `unidades` solo 1.154.

| Método | Responde a… |
| --- | --- |
| `shape`, `columns`, `dtypes` | ¿Qué tamaño y qué tipos tiene? |
| `head()`, `tail()`, `sample(5)` | ¿Qué pinta tienen las filas? |
| `info()` | ¿Cuántos nulos hay y cuánta memoria ocupa? |
| `describe()` | ¿Cómo se distribuyen las columnas numéricas? |
| `value_counts()`, `unique()`, `nunique()` | ¿Qué categorías hay y cuántas veces aparecen? |

### Para practicar

1. Carga `ventas_2026.csv` sin `decimal=","` y mira el tipo de la columna `precio`. Explica qué ha pasado.
2. Carga solo las columnas `fecha`, `ciudad` e `importe`… y comprueba que la última no existe. ¿Qué error da `usecols`?
3. (A) Usa `describe(include="all")` y explica qué significan `unique`, `top` y `freq` en las columnas de texto.

## 3.3 Seleccionar y filtrar

**Listado 3.4.** `loc`, `iloc` y máscaras booleanas · [ver fichero](listados/listado_3_04_seleccion.py)

```python
print(ventas.loc[0, "ciudad"])                 # por etiqueta: fila 0, columna ciudad
print(ventas.iloc[0, 2])                       # por posición: fila 0, columna 2
print(ventas.loc[:4, ["ciudad", "precio"]])    # rebanada de filas y columnas

caras = ventas["precio"] > 500                 # una Series de True/False
print(caras.sum(), "ventas de más de 500 €")   # 218
print(ventas[caras].head(3))

# Varias condiciones: & (y), | (o), ~ (no). Cada una entre paréntesis
granada_online = ventas[(ventas["ciudad"] == "Granada") & (ventas["canal"] == "online")]

andalucia_oriental = ventas[ventas["ciudad"].isin(["Granada", "Jaén", "Almería"])]
print(len(ventas[ventas["precio"].between(100, 200)]))
print(len(ventas.query("precio > 500 and canal == 'tienda'")))   # alternativa legible
```

> [!WARNING]
> Usa `&`, `|` y `~`, no `and`, `or` y `not`: estos últimos trabajan con un único valor de verdad y fallan sobre una Series. Y pon cada condición entre paréntesis, porque `&` tiene más prioridad que `==`.

| Quiero… | Escribo |
| --- | --- |
| Una columna | `df["ciudad"]` |
| Varias columnas | `df[["ciudad", "precio"]]` |
| Filas por etiqueta de índice | `df.loc[10:20]` |
| Filas por posición | `df.iloc[0:5]` |
| Filas que cumplen una condición | `df[df["precio"] > 500]` |
| Filas de una lista de valores | `df[df["ciudad"].isin([...])]` |
| Un rango de valores | `df[df["precio"].between(100, 200)]` |

### Para practicar

1. Obtén las ventas de diciembre con importe superior a 1.000 €. Pista: `ventas["fecha"].dt.month`.
2. Cuenta cuántas ventas hay de cada producto en el canal `online`.
3. (A) Escribe la misma consulta con máscaras y con `query()`. ¿Cuál te parece más legible? ¿Y más fácil de construir dinámicamente desde un filtro de Streamlit?

## 3.4 Limpiar los datos

Es la parte menos vistosa y la más importante: un análisis sobre datos sucios produce conclusiones falsas con una presentación impecable.

### Valores ausentes

**Listado 3.5.** Detectar y tratar nulos · [ver fichero](listados/listado_3_05_nulos.py)

```python
print(ventas.isna().sum())                       # nulos por columna
print((ventas.isna().mean() * 100).round(1))     # porcentaje

sin_unidades = ventas.dropna(subset=["unidades"])          # 1. descartar la fila
canal_relleno = ventas["canal"].fillna("desconocido")      # 2. valor de relleno
mediana = ventas["unidades"].median()                      # 3. imputar
unidades_imputadas = ventas["unidades"].fillna(mediana)
```

La decisión no es técnica, es de criterio ([pandas: Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)):

| Estrategia | Cuándo | Riesgo |
| --- | --- | --- |
| Descartar la fila | Pocos nulos y repartidos al azar | Perder información; sesgar si los nulos no son aleatorios |
| Rellenar con una categoría | El nulo **significa** algo, como «no consta» | Crear una categoría artificial |
| Imputar con media o mediana | La columna es numérica y hace falta completa | Reducir la variabilidad real de los datos |

Documenta siempre qué decidiste y por qué: forma parte del análisis.

### Duplicados, texto y tipos

**Listado 3.6.** Duplicados, texto y tipos · [ver fichero](listados/listado_3_06_limpieza.py)

```python
print(ventas.duplicated().sum(), "filas duplicadas")    # 15
ventas = ventas.drop_duplicates()

print(sorted(ventas["ciudad"].unique())[:6])    # '  GRANADA ' y 'Granada' conviven

ventas["ciudad"] = ventas["ciudad"].str.strip().str.title()   # métodos .str
ventas["canal"] = ventas["canal"].fillna("desconocido")
ventas["unidades"] = ventas["unidades"].fillna(0).astype("int64")

print(ventas["fecha"].dt.year.unique(), ventas["fecha"].dt.month.min())
```

Los accesores `.str` y `.dt` aplican a toda la columna los métodos de cadena y de fecha que ya conoces de la UD1: `str.strip`, `str.lower`, `str.replace`, `str.contains`, `dt.year`, `dt.month`, `dt.dayofweek`. Sin ellos acabarías escribiendo un bucle.

### Valores atípicos

**Listado 3.7.** Criterio del rango intercuartílico · [ver fichero](listados/listado_3_07_atipicos.py)

```python
q1 = ventas["unidades"].quantile(0.25)
q3 = ventas["unidades"].quantile(0.75)
iqr = q3 - q1
limite_superior = q3 + 1.5 * iqr

atipicos = ventas[ventas["unidades"] > limite_superior]
print(f"Q1={q1}  Q3={q3}  IQR={iqr}  límite={limite_superior}")   # límite=18.0
print(len(atipicos), "ventas atípicas")                            # 10
```

El criterio del rango intercuartílico marca como atípico lo que se aleja más de 1,5 veces el IQR de los cuartiles. En nuestro fichero encuentra diez ventas de entre 200 y 400 unidades.

> [!IMPORTANT]
> Un atípico no es necesariamente un error. Puede ser un pedido real de un cliente grande. Antes de eliminar nada, mira las filas, decide con criterio y **escribe la decisión** en el informe. Eliminar en silencio los datos que no encajan es la forma más rápida de mentir con estadística.

### Para practicar

1. ¿Qué porcentaje de filas perderías si aplicaras `dropna()` sin `subset`? ¿Te parece aceptable?
2. Detecta los atípicos de la columna `importe` con el mismo criterio. ¿Son los mismos que los de `unidades`?
3. Comprueba si hay duplicados por `id_venta` aunque el resto de la fila cambie: `ventas.duplicated(subset=["id_venta"])`.
4. (A) Escribe una función `limpiar(ventas: pd.DataFrame) -> pd.DataFrame` que reúna todos los pasos y devuelva el DataFrame limpio, con su docstring. Compárala con [`comun.py`](listados/comun.py).

## 3.5 Transformar: columnas, grupos y uniones

### Columnas derivadas

**Listado 3.8.** `assign`, operaciones vectorizadas y clasificación · [ver fichero](listados/listado_3_08_columnas.py)

```python
ventas = ventas.assign(
    importe=lambda df: (df["unidades"] * df["precio"]).round(2),
    mes=lambda df: df["fecha"].dt.month,
    trimestre=lambda df: df["fecha"].dt.quarter,
)

ventas["tamaño"] = np.where(ventas["importe"] > 1000, "grande", "normal")
ventas["rango_precio"] = pd.cut(
    ventas["precio"],
    bins=[0, 50, 200, 1000],
    labels=["bajo", "medio", "alto"],
)
```

`assign` devuelve una copia con las columnas nuevas, así que permite encadenar transformaciones sin modificar el original. Para clasificar, `np.where` resuelve los casos de dos ramas y `pd.cut` convierte una variable continua en intervalos. Evita `apply` fila a fila siempre que exista una operación vectorizada: es mucho más lento.

### Agrupar y agregar

**Listado 3.9.** El equivalente a `GROUP BY` · [ver fichero](listados/listado_3_09_groupby.py)

```python
print(ventas.groupby("ciudad")["importe"].sum().sort_values(ascending=False))

resumen = (
    ventas.groupby("ciudad")
    .agg(
        ventas=("id_venta", "count"),
        unidades=("unidades", "sum"),
        importe=("importe", "sum"),
        ticket_medio=("importe", "mean"),
    )
    .round(2)
    .sort_values("importe", ascending=False)
)
print(resumen)
```

Resultado:

```text
         ventas  unidades    importe  ticket_medio
ciudad
Málaga      168      1348  361772.14       2153.41
Huelva      163      1251  337589.59       2071.10
Sevilla     149      1576  280358.89       1881.60
...
```

Compáralo con el listado 1.30, que hacía esto mismo con un diccionario y doce líneas. La sintaxis `nombre=("columna", "función")` da nombres claros a las columnas resultantes ([pandas: Group by](https://pandas.pydata.org/docs/user_guide/groupby.html)).

**Listado 3.10.** Tablas dinámicas y de contingencia · [ver fichero](listados/listado_3_10_pivot.py)

```python
tabla = pd.pivot_table(
    ventas, index="ciudad", columns="canal", values="importe",
    aggfunc="sum", fill_value=0,
).round(0)

print(pd.crosstab(ventas["producto"], ventas["canal"]))   # recuento cruzado
```

### Unir tablas

**Listado 3.11.** `merge` y `concat` · [ver fichero](listados/listado_3_11_merge.py)

```python
ciudades = pd.read_csv(Path("datos") / "ciudades.csv", sep=";")

completo = ventas.merge(ciudades, on="ciudad", how="left")   # el JOIN de SQL
print(completo["provincia"].isna().sum(), "filas sin provincia")

por_ciudad = completo.groupby(["ciudad", "poblacion_miles"])["importe"].sum().reset_index()
por_ciudad["euros_por_habitante"] = (
    por_ciudad["importe"] / (por_ciudad["poblacion_miles"] * 1000)
).round(2)

semestre = pd.concat([primer_trimestre, segundo_trimestre], ignore_index=True)  # UNION
```

`how="left"` conserva todas las filas de la izquierda, igual que un `LEFT JOIN`. Contar los nulos que aparecen tras el `merge` es la forma rápida de detectar claves que no casan, casi siempre por diferencias de escritura ([pandas: Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)).

La métrica de euros por habitante cambia por completo el ranking: Málaga factura más en total, pero Jaén y Cádiz facturan mucho más por habitante. Un dato agregado casi nunca significa nada hasta que se normaliza.

### Series temporales

**Listado 3.12.** Remuestrear y suavizar · [ver fichero](listados/listado_3_12_temporal.py)

```python
serie = ventas.set_index("fecha")["importe"]

mensual = serie.resample("ME").sum().round(2)      # ME = fin de mes; W = semana
print(mensual.rolling(window=3).mean().round(2))   # media móvil de 3 meses
print((mensual.pct_change() * 100).round(1))       # variación mensual en %
```

Con la fecha como índice, `resample` agrupa por periodos, `rolling` calcula medias móviles que suavizan el ruido y `pct_change` da la variación respecto al periodo anterior ([pandas: Time series](https://pandas.pydata.org/docs/user_guide/timeseries.html)).

### Guardar los resultados

**Listado 3.13.** Exportar a CSV, Excel, JSON y Parquet · [ver fichero](listados/listado_3_13_exportar.py)

```python
resumen.to_csv(salida / "resumen_ciudades.csv", sep=";", decimal=",", encoding="utf-8")
resumen.to_excel(salida / "resumen_ciudades.xlsx")          # necesita openpyxl
resumen.to_json(salida / "resumen_ciudades.json", indent=2, force_ascii=False)
ventas.to_parquet(salida / "ventas_limpias.parquet")        # formato columnar comprimido
```

Guarda los datos limpios en **Parquet**, no en CSV: conserva los tipos, ocupa mucho menos y se lee más rápido. Volveremos sobre ello en la UD5. El CSV queda para lo que tenga que abrir una persona en Excel.

### Para practicar

1. Calcula la facturación por producto y canal, y muéstrala como tabla dinámica con los productos en filas.
2. Añade a `ciudades.csv` una columna `zona` (oriental u occidental) y calcula la facturación por zona.
3. Obtén la facturación semanal con `resample("W")` y su media móvil de 4 semanas.
4. (A) Reescribe el listado 1.30 de la UD1 usando pandas. Cuenta las líneas de una y otra versión y comenta la diferencia.

## 3.6 Visualizar: matplotlib y seaborn

**matplotlib** es la base: da control total sobre figuras y ejes. **seaborn** está construido encima y resuelve en una línea los gráficos estadísticos habituales, con un aspecto cuidado por defecto.

**Listado 3.14.** Figura con dos ejes en matplotlib · [ver fichero](listados/listado_3_14_matplotlib.py)

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

ax1.plot(mensual.index, mensual.values, marker="o", color="#1f77b4")
ax1.set_title("Facturación mensual 2026")
ax1.set_xlabel("Mes")
ax1.set_ylabel("Importe (€)")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)

ax2.barh(por_ciudad.index, por_ciudad.values, color="#2ca02c")
ax2.set_title("Facturación por ciudad")

fig.tight_layout()
fig.savefig("graficos/resumen.png", dpi=150)
plt.show()          # en un notebook el gráfico aparece bajo la celda
```

La estructura es siempre la misma: una **figura** que contiene uno o varios **ejes**, y sobre cada eje se dibuja y se etiqueta ([Matplotlib quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)).

**Listado 3.15.** Cuatro gráficos estadísticos con seaborn · [ver fichero](listados/listado_3_15_seaborn.py)

```python
import seaborn as sns

sns.set_theme(style="whitegrid")

sns.histplot(data=ventas, x="importe", bins=40, ax=ejes[0, 0])      # distribución
sns.boxplot(data=ventas, x="canal", y="importe", ax=ejes[0, 1])     # comparar grupos
sns.barplot(data=por_producto, x="importe", y="producto", ax=ejes[1, 0])
sns.scatterplot(data=ventas, x="unidades", y="importe", hue="canal", alpha=0.6,
                ax=ejes[1, 1])                                      # relación
```

Elegir el gráfico es elegir la pregunta ([seaborn tutorial](https://seaborn.pydata.org/tutorial.html)):

| Pregunta | Gráfico | Función |
| --- | --- | --- |
| ¿Cómo se distribuye una variable numérica? | Histograma | `sns.histplot` |
| ¿Cómo evoluciona en el tiempo? | Líneas | `sns.lineplot`, `ax.plot` |
| ¿Cómo se comparan las categorías? | Barras | `sns.barplot`, `ax.bar` |
| ¿Hay diferencias de distribución entre grupos? | Cajas o violín | `sns.boxplot`, `sns.violinplot` |
| ¿Se relacionan dos variables numéricas? | Dispersión | `sns.scatterplot` |
| ¿Cómo se relacionan todas con todas? | Mapa de calor | `sns.heatmap` |

> [!TIP]
> Un gráfico sin título ni unidades no vale nada, y uno con el eje Y cortado engaña aunque los datos sean correctos. Pon siempre título, nombres de ejes con unidades, y empieza las barras en cero.

### Para practicar

1. Dibuja la evolución mensual de las unidades vendidas y añade la media móvil de tres meses en la misma figura.
2. Haz un `boxplot` del importe por producto y explica qué producto tiene más variabilidad.
3. Cambia los colores del gráfico de barras con `palette` y guarda la figura a 300 dpi.
4. (A) Busca un gráfico publicado en un medio de comunicación con el eje Y cortado y explica cómo cambiaría la lectura si empezara en cero.

## 3.7 Análisis exploratorio

El análisis exploratorio es mirar los datos con método antes de sacar conclusiones: primero cada variable por separado, después las relaciones entre ellas.

**Listado 3.16.** Una variable cada vez · [ver fichero](listados/listado_3_16_univariante.py)

```python
print(ventas["importe"].describe().round(2))
print("mediana:", ventas["importe"].median().round(2))
print("asimetría:", ventas["importe"].skew().round(2))
print(ventas["importe"].quantile([0.1, 0.25, 0.5, 0.75, 0.9, 0.99]).round(2))

print(ventas["canal"].value_counts())
print((ventas["canal"].value_counts(normalize=True) * 100).round(1))
```

En nuestros datos, la media del importe es 1.972 € y la mediana 899 €. Esa distancia, junto con una asimetría de 7,8, dice que unas pocas ventas muy grandes tiran de la media hacia arriba. **Con distribuciones asimétricas, informa de la mediana**, no solo de la media.

**Listado 3.17.** Relaciones entre variables · [ver fichero](listados/listado_3_17_bivariante.py)

```python
print(ventas.groupby("canal")["importe"].agg(["count", "mean", "median"]).round(2))

numericas = ventas[["unidades", "precio", "importe", "mes"]]
correlacion = numericas.corr().round(2)

sns.heatmap(correlacion, annot=True, cmap="Blues", vmin=-1, vmax=1, ax=ax)
```

La matriz de correlación mide la relación **lineal** entre pares de variables, entre -1 y 1. Aquí `importe` correlaciona 0,63 con `unidades` y 0,48 con `precio`, lo cual es esperable porque es su producto; `mes` no correlaciona con nada, es decir, no hay tendencia creciente a lo largo del año.

> [!WARNING]
> Correlación no es causalidad, y una correlación cercana a cero no significa que no haya relación: solo que no es lineal. Mira siempre el gráfico de dispersión además del número.

**Listado 3.18.** De los datos a la decisión · [ver fichero](listados/listado_3_18_hallazgos.py)

```python
por_cliente = ventas.groupby("cliente")["importe"].sum().sort_values(ascending=False)
top20 = por_cliente.head(int(len(por_cliente) * 0.2))
print(f"{len(top20)} clientes ({len(top20) / len(por_cliente):.0%}) aportan "
      f"{top20.sum() / total:.0%} de la facturación")

mensual = ventas.groupby("mes")["importe"].sum()
print(f"Mejor mes: {mensual.idxmax()} ({mensual.max():,.0f} €)")
```

Salida:

```text
59 clientes (20%) aportan 51% de la facturación
Mejor mes: 5 (302,269 €)
Peor mes:  1 (79,863 €)
Más factura: portátil
Más unidades: impresora
```

Ahí está el criterio 2e: cada número apunta a una decisión posible. Que el 20 % de los clientes aporte la mitad de la facturación sugiere un plan de fidelización; que el producto que más unidades mueve no sea el que más factura sugiere revisar márgenes. **Un análisis termina en recomendaciones, no en una tabla.**

### Para practicar

1. Calcula la mediana y la media del importe por ciudad. ¿Cambia el ranking según cuál uses?
2. ¿Qué día de la semana se vende más? Pista: `dt.dayofweek` y `dt.day_name()`.
3. Comprueba si los clientes del canal `online` compran importes mayores que los de `tienda`, con datos y con un gráfico.
4. (A) Escribe cinco hallazgos de estos datos, cada uno con el número que lo respalda y la decisión que propondrías. Máximo dos líneas por hallazgo.

## 3.8 De los datos a la decisión: Streamlit

Un notebook sirve para analizar, pero no para que lo use otra persona. **Streamlit** convierte un script de Python en una aplicación web: no hay HTML, ni CSS, ni JavaScript. Cada vez que alguien mueve un filtro, Streamlit vuelve a ejecutar el script entero de arriba abajo y redibuja la página ([Streamlit: Get started](https://docs.streamlit.io/get-started)).

**Listado 3.19.** La aplicación más pequeña posible · [ver fichero](listados/listado_3_19_streamlit_minimo.py)

```python
import streamlit as st

from comun import cargar_ventas

st.title("Ventas 2026")

ventas = cargar_ventas()

st.metric("Facturación total", f"{ventas['importe'].sum():,.0f} €")
st.dataframe(ventas.head(20))
st.bar_chart(ventas.groupby("ciudad")["importe"].sum())
```

Se ejecuta desde la terminal, no con `python`:

```bash
streamlit run listado_3_19_streamlit_minimo.py
```

**Listado 3.20.** El panel completo · [ver fichero](app/app.py)

```python
@st.cache_data                      # se calcula una vez; no en cada interacción
def cargar_ventas(ruta: Path) -> pd.DataFrame:
    """Lee y limpia el fichero de ventas."""
    ventas = pd.read_csv(ruta, sep=";", decimal=",", parse_dates=["fecha"])
    ...


with st.sidebar:                    # los filtros, en la barra lateral
    ciudades = st.multiselect("Ciudades", options=..., default=...)
    minimo, maximo = st.slider("Importe por venta (€)", 0, tope, (0, tope), step=100)

filtradas = ventas[ventas["ciudad"].isin(ciudades) & ventas["importe"].between(minimo, maximo)]

col1, col2, col3 = st.columns(3)
col1.metric("Facturación", f"{filtradas['importe'].sum():,.0f} €")

st.line_chart(filtradas.set_index("fecha")["importe"].resample("ME").sum())
st.download_button("Descargar resumen en CSV", data=..., file_name="resumen_ventas.csv")
```

Los elementos que necesitas para casi cualquier panel:

| Familia | Funciones |
| --- | --- |
| Texto | `st.title`, `st.header`, `st.subheader`, `st.write`, `st.caption`, `st.markdown` |
| Datos | `st.dataframe`, `st.table`, `st.metric`, `st.json` |
| Gráficos | `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.pyplot(fig)` para matplotlib |
| Entradas | `st.selectbox`, `st.multiselect`, `st.slider`, `st.date_input`, `st.checkbox`, `st.text_input` |
| Estructura | `st.sidebar`, `st.columns`, `st.tabs`, `st.expander` |
| Otros | `st.download_button`, `st.warning`, `st.stop`, `st.set_page_config` |

> [!TIP]
> `@st.cache_data` es un decorador, como los de la UD2: guarda el resultado de la función y lo reutiliza mientras no cambien sus argumentos. Sin él, tu aplicación releería y limpiaría el CSV cada vez que alguien tocara un filtro.

### Publicar la aplicación

Streamlit Community Cloud publica aplicaciones desde un repositorio de GitHub de forma gratuita, y necesita dos cosas: el fichero de la aplicación y un `requirements.txt` con las dependencias, en la raíz del repositorio o junto a la aplicación ([Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud)).

1. Sube tu proyecto a GitHub con `app.py`, los datos y `requirements.txt`.
2. Entra en [share.streamlit.io](https://share.streamlit.io) con tu cuenta de GitHub.
3. Elige repositorio, rama y ruta del fichero principal, por ejemplo `ud3-datos/app/app.py`.
4. Espera a que instale las dependencias. Obtendrás una URL pública que puedes compartir.

> [!IMPORTANT]
> La aplicación es **pública** y se ejecuta en servidores de Estados Unidos: no subas datos personales ni información confidencial. Fija las versiones en `requirements.txt` (`pandas==3.0.2`), porque si dejas que instale la última versión, un día tu aplicación dejará de funcionar sola.

### Para practicar

1. Añade al panel un filtro por producto y un cuarto indicador con las unidades totales.
2. Sustituye `st.bar_chart` por un gráfico de seaborn mostrado con `st.pyplot(fig)`.
3. Añade una pestaña con `st.tabs` que muestre la tabla de datos sin agregar.
4. (A) Quita el decorador `@st.cache_data`, mide con el `Cronometro` de la UD2 cuánto tarda la carga y explica qué notas al mover los filtros.

## Práctica de la unidad · Hito 2 del proyecto integrador

Toca aplicar todo esto a **tu** conjunto de datos, el que elegiste en el hito 0.

### 1. Limpieza reproducible

En tu paquete `src/`, un módulo `limpieza.py` con la función `cargar_limpio(ruta) -> pd.DataFrame` que:

- Cargue el fichero con los parámetros correctos de `read_csv` o `read_json`.
- Trate nulos, duplicados, tipos, textos y atípicos, con una decisión justificada para cada caso.
- Añada al menos dos columnas derivadas útiles para tu pregunta.
- Guarde el resultado en `datos/procesado/<nombre>.parquet`.

### 2. Análisis exploratorio

Un notebook `notebooks/03_exploracion.ipynb` con:

- Inspección inicial: dimensiones, tipos, nulos y estadísticos.
- Análisis univariante de al menos tres variables, numéricas y categóricas.
- Análisis bivariante: dos comparaciones entre grupos y una matriz de correlación.
- Un mínimo de seis gráficos, todos con título y ejes etiquetados.
- Texto entre las celdas que explique qué se ve en cada gráfico. Un notebook sin texto es un montón de código, no un análisis.

### 3. Panel publicado

Una aplicación `app/app.py` desplegada en Streamlit Community Cloud con, al menos:

- Dos filtros en la barra lateral.
- Tres indicadores (`st.metric`).
- Dos gráficos que reaccionen a los filtros.
- Una tabla y un botón de descarga.
- `@st.cache_data` en la carga de datos.

### 4. Entregables

- El código en el repositorio, con `requirements.txt` actualizado y versiones fijadas.
- El enlace a la aplicación publicada, en el `README.md` del proyecto.
- **Cinco hallazgos** en el `README.md`: cada uno con el dato que lo respalda y la decisión que sugiere, en dos líneas.
- Defensa oral breve (5 minutos): explicar una decisión de limpieza y uno de los hallazgos.

Fecha de entrega propuesta: antes del inicio de la UD5 (30/11/2026).

### 5. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 2a | Carga con los parámetros adecuados, limpieza justificada y datos guardados en Parquet, reproducible con una función |
| 2b | Seis gráficos legibles, con el tipo adecuado a cada pregunta, con título y unidades |
| 2c | Análisis univariante y bivariante que identifica patrones, diferencias entre grupos y correlaciones |
| 2e | Cinco hallazgos redactados con su dato y su decisión, y un panel que permite a otra persona explorar los datos |

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 3.1 NumPy | Vectorizar en lugar de iterar: las operaciones se aplican al array entero y son mucho más rápidas |
| 3.2 Cargar | `read_csv` resuelve con parámetros (`sep`, `decimal`, `parse_dates`) lo que en la UD1 programaste a mano |
| 3.3 Filtrar | `loc` por etiqueta, `iloc` por posición y máscaras booleanas con `&`, `\|`, `~` |
| 3.4 Limpiar | Nulos, duplicados, textos, tipos y atípicos. Cada decisión se justifica y se documenta |
| 3.5 Transformar | `assign` para columnas nuevas, `groupby().agg()` para agrupar, `merge` para unir y `resample` para el tiempo |
| 3.6 Visualizar | La pregunta decide el gráfico. Título, ejes y unidades siempre; barras desde cero |
| 3.7 Explorar | Media frente a mediana en distribuciones asimétricas; correlación no es causalidad |
| 3.8 Comunicar | Streamlit convierte un script en una aplicación web; `@st.cache_data` evita recalcular; se publica desde GitHub |

## Bibliografía de la UD3

Todas las fuentes web se consultaron el 28 de septiembre de 2026.

### Documentación de las bibliotecas

- NumPy developers. (2026). *NumPy: the absolute basics for beginners*. <https://numpy.org/doc/stable/user/absolute_beginners.html>
- pandas development team. (2026). *10 minutes to pandas*. <https://pandas.pydata.org/docs/user_guide/10min.html>
- pandas development team. (2026). *User Guide*: [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html), [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html), [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html) y [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html).
- Matplotlib development team. (2026). *Quick start guide*. <https://matplotlib.org/stable/users/explain/quick_start.html>
- Waskom, M. (2026). *seaborn: user guide and tutorial*. <https://seaborn.pydata.org/tutorial.html>
- Snowflake Inc. (2026). *Streamlit documentation: Get started* y *API reference*. <https://docs.streamlit.io/get-started> · <https://docs.streamlit.io/develop/api-reference>
- Snowflake Inc. (2026). *Deploy on Streamlit Community Cloud*. <https://docs.streamlit.io/deploy/streamlit-community-cloud>

### Lectura complementaria

- McKinney, W. *Python for Data Analysis* (3.ª edición). Edición web gratuita del autor de pandas. <https://wesmckinney.com/book/>
