# UD4 · SQL y NoSQL desde Python

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [4.1 Python y SQL](#41-python-y-sql)
- [4.2 pandas y SQL: dos mundos que se hablan](#42-pandas-y-sql-dos-mundos-que-se-hablan)
- [4.3 NoSQL: el modelo documental](#43-nosql-el-modelo-documental)
- [4.4 SQL frente a NoSQL](#44-sql-frente-a-nosql)
- [Práctica de la unidad · Hito 3 del proyecto integrador](#práctica-de-la-unidad--hito-3-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD4](#bibliografía-de-la-ud4)

## Presentación de la unidad

Cuatro horas para cerrar el círculo del dato: hasta ahora tus datos venían de un fichero y morían en un fichero. Aquí aprenderás a guardarlos en una base de datos y a consultarlos desde Python, tanto en un sistema relacional como en uno documental.

Traes el SQL de Bases de Datos de 1.º. Lo que cambia es el lado de Python: cómo se conecta, cómo se pasan los parámetros sin abrir un agujero de seguridad, y cuándo conviene que calcule la base de datos en lugar de pandas.

### Resultados de aprendizaje y criterios de evaluación

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 2d | Realiza consultas a bases de datos desde Python para extraer información | 4.1, 4.2 |
| 4c | Aplica técnicas de consulta y manipulación de datos en SQL y NoSQL a gran escala | 4.3, 4.4 |

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Martes 17/11/2026 | 1 | 4.1 SQL desde Python: conexión, parámetros e inyección |
| 2 | Lunes 23/11/2026 | 2 | 4.1 Índices · 4.2 pandas y SQL · 4.3 NoSQL |
| 3 | Martes 24/11/2026 | 1 | 4.3 Agregaciones en MongoDB · 4.4 Comparativa y criterios |

### Antes de empezar

```bash
python -m pip install -r ud4-bd/requirements.txt
```

Usaremos **SQLite** para la parte relacional: viene en la biblioteca estándar, no hay servidor que instalar y la base de datos es un único fichero. Todo lo que aprendas sirve igual para MariaDB o PostgreSQL, porque Python habla con todos ellos a través de la misma interfaz (apartado 4.2).

Para la parte NoSQL usaremos **MongoDB**. Si tienes un clúster gratuito de MongoDB Atlas, exporta su URL antes de ejecutar los listados:

```bash
export MONGODB_URI="mongodb+srv://usuario:clave@clúster.mongodb.net/"   # macOS/Linux
$env:MONGODB_URI = "mongodb+srv://usuario:clave@clúster.mongodb.net/"   # PowerShell
```

Si no la defines, [`conexion_mongo.py`](listados/conexion_mongo.py) usa `mongomock`, una imitación local de MongoDB que responde a las mismas órdenes en memoria. El código de los listados es idéntico en los dos casos.

> [!WARNING]
> Una contraseña nunca se escribe en el código ni se sube a GitHub. Va en una variable de entorno, en un fichero `.env` que el `.gitignore` excluya, o en los *secrets* de Streamlit al desplegar ([Streamlit: Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management)).

### Cómo usar esta carpeta

| Carpeta | Contenido |
| --- | --- |
| [`listados/`](listados/) | Los 12 listados de la unidad. Ejecuta primero el 4.1: crea `datos/ventas.db`, que usan los demás |
| [`listados/datos/`](listados/datos/) | `ventas_2026.csv` y `ciudades.csv`, los mismos de la UD3 |

## 4.1 Python y SQL

Python define una interfaz común para todas las bases de datos relacionales, la **DB-API 2.0** ([PEP 249](https://peps.python.org/pep-0249/)). Por eso el código que escribas con `sqlite3` se parecerá muchísimo al que usarías con MariaDB: cambian el módulo y los datos de conexión, no la forma de trabajar.

El ciclo es siempre el mismo: conectar, obtener un cursor, ejecutar, recoger resultados, confirmar los cambios y cerrar.

### Crear la base de datos y cargar los datos

**Listado 4.1.** Crear una base de datos SQLite y cargarla · [ver fichero](listados/listado_4_01_crear_bd.py)

```python
import sqlite3
from pathlib import Path

from comun import cargar_ventas

RUTA_BD = Path("datos") / "ventas.db"
ventas = cargar_ventas()

with sqlite3.connect(RUTA_BD) as conexion:     # el with confirma o deshace la transacción
    conexion.execute("""
        CREATE TABLE venta (
            id_venta  INTEGER PRIMARY KEY,
            fecha     TEXT    NOT NULL,
            ciudad    TEXT    NOT NULL,
            producto  TEXT    NOT NULL,
            canal     TEXT,
            unidades  INTEGER NOT NULL CHECK (unidades >= 0),
            precio    REAL    NOT NULL,
            cliente   TEXT
        )
    """)

    filas = [(int(f.id_venta), f.fecha.date().isoformat(), f.ciudad, f.producto,
              f.canal, int(f.unidades), float(f.precio), f.cliente)
             for f in ventas.itertuples()]
    conexion.executemany("INSERT INTO venta VALUES (?, ?, ?, ?, ?, ?, ?, ?)", filas)
```

- `executemany` inserta toda la lista en una sola transacción. Insertar fila a fila con `execute` dentro de un bucle es órdenes de magnitud más lento.
- El `with` de `sqlite3` **no cierra** la conexión: confirma la transacción si todo fue bien y la deshace si hubo una excepción. Cerrar sigue siendo cosa tuya, con `conexion.close()`.
- Las restricciones (`PRIMARY KEY`, `NOT NULL`, `CHECK`) son la última línea de defensa contra los datos sucios de la UD3. Lo que la base de datos rechaza, no entra.

### Consultar con parámetros

**Listado 4.2.** Cursores, parámetros y filas con nombre · [ver fichero](listados/listado_4_02_consultas.py)

```python
conexion = sqlite3.connect(RUTA_BD)
conexion.row_factory = sqlite3.Row          # filas accesibles por nombre de columna
cursor = conexion.cursor()

cursor.execute("SELECT COUNT(*) AS total, SUM(unidades * precio) AS importe FROM venta")
fila = cursor.fetchone()
print(f"{fila['total']} ventas, {fila['importe']:,.2f} €")     # 1200 ventas, 2.366.772,83 €

cursor.execute(
    """
    SELECT producto, COUNT(*) AS ventas, ROUND(SUM(unidades * precio), 2) AS importe
    FROM venta
    WHERE ciudad = ?
    GROUP BY producto
    ORDER BY importe DESC
    """,
    (ciudad,),
)
for fila in cursor.fetchall():
    print(f"{fila['producto']:<10} {fila['ventas']:>4} {fila['importe']:>12,.2f} €")
```

| Método | Devuelve |
| --- | --- |
| `fetchone()` | La siguiente fila, o `None` |
| `fetchall()` | Todas las filas restantes, en una lista |
| `fetchmany(n)` | Como mucho `n` filas |
| Recorrer el cursor con `for` | Fila a fila, sin cargarlas todas en memoria |

`row_factory = sqlite3.Row` merece la pena siempre: sin él, las filas son tuplas y acabas escribiendo `fila[3]` sin saber qué es la posición 3 ([docs.python.org, sqlite3](https://docs.python.org/3/library/sqlite3.html)).

### Nunca construyas SQL concatenando texto

**Listado 4.3.** Inyección SQL · [ver fichero](listados/listado_4_03_inyeccion.py)

```python
entrada = "Granada' OR '1'='1"          # lo que escribiría un atacante

sql_peligroso = f"SELECT COUNT(*) FROM venta WHERE ciudad = '{entrada}'"
print(conexion.execute(sql_peligroso).fetchone()[0])      # 1200: ¡todas las filas!

seguro = conexion.execute(
    "SELECT COUNT(*) FROM venta WHERE ciudad = ?", (entrada,)
).fetchone()[0]
print(seguro)                                             # 0: no existe esa ciudad
```

El SQL generado por la primera versión es `... WHERE ciudad = 'Granada' OR '1'='1'`, que es cierto para todas las filas. Con `SELECT` se filtra un dato que no debería verse; con `DELETE`, se borra una tabla.

> [!IMPORTANT]
> **Regla sin excepciones.** Los valores viajan siempre como parámetros (`?` o `:nombre`), nunca dentro del texto de la consulta. Los parámetros no se interpretan como SQL: son datos. Esto vale también cuando el valor viene de un filtro de Streamlit, que es exactamente el caso de tu proyecto.

### Índices

**Listado 4.4.** El mismo `SELECT`, antes y después de crear el índice · [ver fichero](listados/listado_4_04_indices.py)

```python
consulta = "SELECT COUNT(*) FROM venta WHERE ciudad = ? AND producto = ?"

for fila in conexion.execute("EXPLAIN QUERY PLAN " + consulta, ("Granada", "monitor")):
    print(fila[-1])            # SCAN venta

conexion.execute("CREATE INDEX idx_ciudad_producto ON venta (ciudad, producto)")

for fila in conexion.execute("EXPLAIN QUERY PLAN " + consulta, ("Granada", "monitor")):
    print(fila[-1])            # SEARCH venta USING COVERING INDEX idx_ciudad_producto
```

Salida de la medición con 1.200 filas:

```text
2000 consultas sin índice: 0.140 s
2000 consultas con índice: 0.013 s
```

Un índice es una estructura ordenada que evita recorrer la tabla entera: el plan pasa de `SCAN` (leer todo) a `SEARCH` (ir directo). Con mil filas apenas se nota; con millones, es la diferencia entre milisegundos y minutos. A cambio, ocupa espacio y ralentiza las escrituras, así que se indexa lo que de verdad se consulta y filtra.

### Para practicar

1. Añade una restricción `UNIQUE` sobre `id_venta` y comprueba qué ocurre al insertar dos veces la misma venta.
2. Escribe una consulta parametrizada que devuelva las ventas de un mes y una ciudad dados, ordenadas por importe.
3. Crea un índice sobre `fecha` y comprueba con `EXPLAIN QUERY PLAN` si lo usa una consulta que filtra por rango de fechas.
4. (A) Reescribe el listado 4.3 con `DELETE` en un fichero de prueba y explica por escrito qué habría pasado con la entrada del atacante.

## 4.2 pandas y SQL: dos mundos que se hablan

**Listado 4.5.** `to_sql` y `read_sql` · [ver fichero](listados/listado_4_05_pandas_sql.py)

```python
with sqlite3.connect(RUTA_BD) as conexion:
    ciudades.to_sql("ciudad", conexion, if_exists="replace", index=False)

    resumen = pd.read_sql(
        """
        SELECT c.provincia,
               COUNT(*)                             AS ventas,
               ROUND(SUM(v.unidades * v.precio), 2) AS importe,
               c.poblacion_miles
        FROM venta v
        JOIN ciudad c ON v.ciudad = c.ciudad
        GROUP BY c.provincia, c.poblacion_miles
        ORDER BY importe DESC
        """,
        conexion,
    )
```

Un DataFrame se convierte en tabla con `to_sql` y una consulta se convierte en DataFrame con `read_sql`. Ese `JOIN` es el mismo `merge` del listado 3.11, pero ejecutado por la base de datos.

### ¿Quién debe hacer el cálculo?

**Listado 4.6.** La misma pregunta, en SQL y en pandas · [ver fichero](listados/listado_4_06_sql_o_pandas.py)

```python
# Opción A: que trabaje la base de datos y traiga solo el resultado
en_sql = pd.read_sql(
    "SELECT canal, ROUND(SUM(unidades * precio), 2) AS importe "
    "FROM venta WHERE ciudad = ? GROUP BY canal ORDER BY importe DESC",
    conexion, params=("Granada",),
)

# Opción B: traerlo todo y agrupar en memoria con pandas
en_pandas = (
    ventas[ventas["ciudad"] == "Granada"]
    .groupby("canal", as_index=False)["importe"].sum().round(2)
    .sort_values("importe", ascending=False)
)
```

Ambas dan lo mismo. La diferencia está en qué viaja por la red y qué cabe en memoria:

| Hazlo en SQL | Hazlo en pandas |
| --- | --- |
| Filtrar y agregar grandes volúmenes: que viajen 8 filas y no 8 millones | Transformaciones complejas y encadenadas |
| Uniones entre tablas que ya están en la base de datos | Gráficos, estadística y preparación para modelos |
| Cuando los datos no caben en memoria | Cuando ya tienes el subconjunto que te interesa |

La regla práctica: **filtra y agrega lo más cerca posible del dato**, y trae a Python solo lo que vas a analizar.

### Otras bases de datos: SQLAlchemy

**Listado 4.7.** El mismo código para SQLite y para MariaDB · [ver fichero](listados/listado_4_07_sqlalchemy.py)

```python
from sqlalchemy import create_engine, text

URL_SQLITE = f"sqlite:///{Path('datos') / 'ventas.db'}"

# En un servidor real sería algo así (nunca con la contraseña escrita en el código):
#   URL_MARIADB = (
#       f"mariadb+mariadbconnector://{os.environ['BD_USUARIO']}:"
#       f"{os.environ['BD_CLAVE']}@servidor:3306/ventas"
#   )
motor = create_engine(os.environ.get("BD_URL", URL_SQLITE))

with motor.connect() as conexion:
    total = conexion.execute(
        text("SELECT COUNT(*) FROM venta WHERE ciudad = :ciudad"),
        {"ciudad": "Granada"},
    ).scalar()

top = pd.read_sql("SELECT ciudad, ROUND(SUM(unidades * precio), 2) AS importe "
                  "FROM venta GROUP BY ciudad ORDER BY importe DESC LIMIT 3", motor)
```

SQLAlchemy añade una capa sobre la DB-API: la conexión se describe con una **URL** y el resto del código no cambia al pasar de SQLite a MariaDB, PostgreSQL o SQL Server ([SQLAlchemy: Engine configuration](https://docs.sqlalchemy.org/en/20/core/engines.html)). Cada motor necesita su controlador instalado, por ejemplo `mariadb` o `psycopg`.

Con esto ya puedes leer directamente de la MariaDB del ciclo: cambia la URL y el resto del programa sigue igual.

### Para practicar

1. Carga la tabla `ciudad` y escribe una consulta que devuelva la facturación por provincia y canal.
2. Mide con el `Cronometro` de la UD2 cuánto tarda la opción A y la opción B del listado 4.6. ¿Se nota con 1.200 filas?
3. (A) Adapta el listado 4.7 para que lea la URL de un fichero `.env` (biblioteca `python-dotenv`) y añade ese fichero al `.gitignore`.

## 4.3 NoSQL: el modelo documental

«NoSQL» agrupa bases de datos que no siguen el modelo relacional. Hay cuatro familias principales:

| Familia | Guarda… | Ejemplos | Uso típico |
| --- | --- | --- | --- |
| Documental | Documentos tipo JSON, anidados | MongoDB, Firestore, CouchDB | Catálogos, perfiles, eventos con estructura variable |
| Clave-valor | Un valor por clave, sin estructura | Redis, DynamoDB | Cachés, sesiones, contadores |
| Columnar | Columnas por familia, muy distribuido | Cassandra, HBase | Series temporales y escrituras masivas |
| Grafos | Nodos y relaciones | Neo4j | Redes sociales, recomendaciones, fraude |

En este módulo trabajamos la documental, que es la más cercana a lo que ya sabes: un documento es, en la práctica, un diccionario de Python.

### El modelo documental sin instalar nada

**Listado 4.8.** TinyDB · [ver fichero](listados/listado_4_08_tinydb.py)

```python
from tinydb import Query, TinyDB

bd = TinyDB(RUTA, indent=2, ensure_ascii=False)
productos = bd.table("productos")

productos.insert({"nombre": "portátil", "precio": 899.90, "stock": 12,
                  "especificaciones": {"ram_gb": 16, "ssd_gb": 512}})
productos.insert({"nombre": "ratón", "precio": 12.50, "stock": 120,
                  "inalambrico": True})

P = Query()
print(productos.search(P.precio > 100))
print(productos.search(P.especificaciones.ram_gb == 16))     # busca dentro del documento
productos.update({"stock": 25}, P.nombre == "monitor")
```

Fíjate en lo que sería imposible en una tabla: el portátil tiene `especificaciones` anidadas y el ratón un campo `inalambrico` que los demás no tienen. En SQL harían falta columnas nuevas, o una tabla de atributos, o los dos.

### MongoDB desde Python

**Listado 4.9.** Insertar y consultar · [ver fichero](listados/listado_4_09_mongo_basico.py)

```python
cliente = obtener_cliente()
coleccion = cliente["tienda"]["ventas"]

documentos = ventas.assign(fecha=ventas["fecha"].dt.strftime("%Y-%m-%d")).to_dict("records")
coleccion.insert_many(documentos)                  # 1200 documentos insertados

filtro = {"ciudad": "Granada", "importe": {"$gt": 1000}}
proyeccion = {"_id": 0, "producto": 1, "canal": 1, "importe": 1}
print(coleccion.count_documents(filtro))           # 64 ventas grandes en Granada

for documento in coleccion.find(filtro, proyeccion).sort("importe", -1).limit(3):
    print(documento)

print(coleccion.count_documents({"producto": {"$in": ["portátil", "tablet"]}}))
```

El filtro es un diccionario, no una cadena de texto. Eso evita de raíz la inyección del listado 4.3, aunque no evita otros errores: si metes en el filtro un valor que llega del usuario sin validar, puedes seguir devolviendo datos que no tocaban.

| SQL | MongoDB |
| --- | --- |
| Tabla | Colección |
| Fila | Documento |
| Columna | Campo |
| `WHERE ciudad = 'Granada'` | `{"ciudad": "Granada"}` |
| `WHERE importe > 1000` | `{"importe": {"$gt": 1000}}` |
| `WHERE producto IN (...)` | `{"producto": {"$in": [...]}}` |
| `SELECT producto, importe` | `{"producto": 1, "importe": 1, "_id": 0}` |
| `ORDER BY importe DESC LIMIT 3` | `.sort("importe", -1).limit(3)` |

**Listado 4.10.** Agregaciones: el `GROUP BY` de MongoDB · [ver fichero](listados/listado_4_10_mongo_agregacion.py)

```python
tuberia = [
    {"$match": {"canal": {"$ne": "desconocido"}}},                  # WHERE
    {"$group": {"_id": "$ciudad",                                   # GROUP BY
                "ventas": {"$sum": 1},
                "importe": {"$sum": "$importe"},
                "ticket_medio": {"$avg": "$importe"}}},
    {"$sort": {"importe": -1}},                                     # ORDER BY
    {"$limit": 5},                                                  # LIMIT
]

for fila in coleccion.aggregate(tuberia):
    print(fila["_id"], fila["ventas"], round(fila["importe"], 2))
```

Una agregación es una **tubería**: cada etapa recibe los documentos que produjo la anterior, igual que encadenas operaciones en pandas ([MongoDB: Aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/)).

**Listado 4.11.** Esquema flexible e índices · [ver fichero](listados/listado_4_11_mongo_esquema.py)

```python
catalogo.insert_many([
    {"nombre": "portátil", "precio": 899.90,
     "especificaciones": {"ram_gb": 16, "ssd_gb": 512}},
    {"nombre": "ratón", "precio": 12.50, "inalambrico": True},
    {"nombre": "monitor", "precio": 180.00,
     "especificaciones": {"pulgadas": 27}, "etiquetas": ["oficina", "hogar"]},
])

print(list(catalogo.find({"especificaciones.ram_gb": {"$gte": 8}}, {"_id": 0, "nombre": 1})))
print(list(catalogo.find({"etiquetas": "oficina"}, {"_id": 0, "nombre": 1})))

catalogo.create_index("nombre")
catalogo.create_index([("precio", -1)])

# La flexibilidad tiene precio: nada impide guardar "precio": "25,00" como texto
catalogo.insert_one({"nombre": "teclado", "precio": "25,00"})
print(catalogo.count_documents({"precio": {"$type": "string"}}))     # 1
```

> [!WARNING]
> «Sin esquema» no significa «sin diseño». En una tabla, la columna `precio` es `REAL` y punto; en una colección, nada impide que un día alguien guarde `"25,00"` como texto y rompa todos los cálculos. La validación que no hace la base de datos la tienes que hacer tú, en Python.

**Listado 4.12.** De MongoDB a pandas · [ver fichero](listados/listado_4_12_mongo_pandas.py)

```python
cursor = coleccion.find({"importe": {"$gt": 2000}}, {"_id": 0})
grandes = pd.DataFrame(list(cursor))         # el cursor se consume una sola vez

print(grandes.groupby("producto")["importe"].sum().round(2).sort_values(ascending=False))
```

Excluir `_id` en la proyección evita arrastrar el identificador interno de MongoDB, que no se puede convertir a JSON sin más y suele estorbar en un DataFrame.

### Para practicar

1. Inserta en TinyDB tres documentos con campos distintos y escribe una búsqueda que use un campo anidado.
2. Escribe la agregación que devuelva el importe total por producto y canal, ordenado de mayor a menor.
3. Traduce a MongoDB esta consulta: `SELECT cliente, SUM(unidades*precio) FROM venta GROUP BY cliente HAVING SUM(unidades*precio) > 20000`. Pista: `$group` y después `$match`.
4. (A) Crea un clúster gratuito en MongoDB Atlas, exporta `MONGODB_URI` y ejecuta los listados 4.9 a 4.12 contra él. ¿Cambia alguna línea de código?

## 4.4 SQL frente a NoSQL

### Cómo crece cada uno

Una base de datos relacional crece sobre todo **en vertical**: máquina más grande, más memoria, discos más rápidos. Puede repartirse en varias máquinas con réplicas de lectura y con particionado, pero mantener transacciones que afecten a varias máquinas es caro y complejo.

Las bases NoSQL nacieron para crecer **en horizontal**: añadir máquinas al grupo y repartir los datos entre ellas (*sharding*), con copias de cada fragmento en varios nodos (*replicación*). A cambio renuncian a parte de las garantías del modelo relacional.

### El teorema CAP

Cuando los datos están repartidos entre varias máquinas, la red puede partirse. Ante una partición hay que elegir entre seguir respondiendo con datos posiblemente desactualizados o dejar de responder hasta recuperar la coherencia: no se pueden tener a la vez coherencia, disponibilidad y tolerancia a particiones (Gilbert y Lynch, 2002).

| Propiedad | Significa |
| --- | --- |
| **C**oherencia | Toda lectura ve la última escritura confirmada |
| **A**vailability (disponibilidad) | Toda petición recibe respuesta |
| **P**artition tolerance | El sistema sigue funcionando aunque se corte la comunicación entre nodos |

De ahí la diferencia de garantías: los sistemas relacionales priorizan las propiedades **ACID** (atomicidad, coherencia, aislamiento y durabilidad), mientras que muchos NoSQL adoptan la **coherencia eventual**: tras una escritura, las réplicas tardan un poco en ponerse de acuerdo, y durante ese rato una lectura puede devolver el valor anterior. Para el saldo de una cuenta bancaria es inaceptable; para el contador de «me gusta» de un vídeo, da igual.

### Cuándo elegir cada uno

| Elige relacional cuando… | Elige documental cuando… |
| --- | --- |
| Los datos tienen estructura estable y relaciones claras | La estructura varía entre registros o cambia a menudo |
| Necesitas transacciones y garantías fuertes | Necesitas escribir mucho y escalar en horizontal |
| Vas a hacer consultas analíticas con muchas uniones | Casi siempre lees el documento completo, sin unir nada |
| El equipo ya sabe SQL, y la consulta es la herramienta principal | Los datos son anidados por naturaleza: un pedido con sus líneas |

En la práctica conviven. Un proyecto real guarda los pedidos en PostgreSQL, las sesiones en Redis y el catálogo en MongoDB. Y los sistemas se han acercado: PostgreSQL y MariaDB almacenan y consultan JSON, y MongoDB admite transacciones y validación de esquema.

### Y para el proyecto de este módulo

| Opción | Cuándo te conviene |
| --- | --- |
| SQLite | Tu conjunto de datos es una tabla, cabe en un fichero y trabajas en local. Es la opción por defecto |
| MariaDB del ciclo | Quieres practicar contra un servidor real, con usuarios y permisos |
| MongoDB Atlas | Tu dataset tiene estructura variable o anidada, o quieres probar el modelo documental |

Sea cual sea, el panel de Streamlit de la UD3 puede leer de la base de datos en lugar del CSV: es lo que harás en la práctica.

### Para practicar

1. Clasifica estos casos y justifica: un sistema de reservas de vuelos, el historial de sensores de una fábrica, el catálogo de una tienda con fichas muy distintas, el carrito de la compra.
2. Explica con tus palabras qué garantía pierdes al usar coherencia eventual, con un ejemplo cotidiano.
3. (A) Busca cómo se llama el particionado en MongoDB y en MariaDB, y resume en cinco líneas en qué se diferencian.

## Práctica de la unidad · Hito 3 del proyecto integrador

Tu conjunto de datos deja de vivir en un fichero.

### 1. Llevarlo a una base de datos relacional

- Diseña el esquema con tipos, claves y restricciones (`NOT NULL`, `CHECK`, `UNIQUE`). Justifica los tipos elegidos.
- Escribe en tu paquete un módulo `bd.py` con dos funciones: una que cree la base de datos y cargue los datos limpios de la UD3, y otra que devuelva una conexión.
- Crea al menos un índice sobre la columna por la que más filtras y demuestra con `EXPLAIN QUERY PLAN` que se usa.

### 2. Seis consultas que respondan preguntas

Las mismas preguntas del hito 2, ahora resueltas en SQL. Al menos una debe incluir `GROUP BY` con `HAVING`, y otra un `JOIN` con una tabla auxiliar que tú añadas (categorías, provincias, fechas señaladas…). Todas parametrizadas.

### 3. Versión documental

Guarda una parte de tus datos como documentos en MongoDB o TinyDB, aprovechando la estructura anidada o los campos variables, y escribe:

- Dos consultas con filtros.
- Una agregación equivalente a un `GROUP BY`.
- Cinco líneas comparando ambas versiones: qué resultó más natural, qué te costó más y cuál usarías en producción.

### 4. Conectar el panel

Modifica `app/app.py` para que lea de la base de datos en lugar del CSV, con consultas parametrizadas construidas a partir de los filtros. Mantén `@st.cache_data` en la carga.

### 5. Entregables

- El módulo `bd.py`, el script de creación y las consultas, en el repositorio.
- Un apartado en el `README.md` con el esquema, las seis consultas y la comparación SQL/NoSQL.
- El panel actualizado y desplegado.
- Defensa oral breve (5 minutos): explicar una consulta y por qué decidiste calcularla en la base de datos o en pandas.

Fecha de entrega propuesta: antes del inicio de la UD6 (15/12/2026).

### 6. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 2d | Conexión desde Python, consultas parametrizadas, `JOIN`, agregaciones y uso correcto de `read_sql` |
| 4c | Versión documental funcionando, agregación equivalente y comparación razonada entre ambos modelos |

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 4.1 SQL desde Python | Conectar, cursor, ejecutar, confirmar. Los valores van como parámetros: nunca concatenes SQL |
| 4.1 Índices | `EXPLAIN QUERY PLAN` dice si se usan; convierten un `SCAN` en un `SEARCH` |
| 4.2 pandas y SQL | `to_sql` y `read_sql` unen los dos mundos. Filtra y agrega en la base de datos; analiza en pandas |
| 4.2 SQLAlchemy | Una URL describe la conexión: el mismo código sirve para SQLite y para MariaDB |
| 4.3 NoSQL | Un documento es un diccionario. Filtros y tuberías de agregación en lugar de `WHERE` y `GROUP BY` |
| 4.3 Esquema flexible | Sin esquema no es sin diseño: la validación que no hace la base de datos la haces tú |
| 4.4 Comparativa | Relacional escala en vertical y garantiza ACID; NoSQL escala en horizontal y suele ofrecer coherencia eventual |

## Bibliografía de la UD4

Todas las fuentes web se consultaron el 28 de septiembre de 2026.

### Documentación oficial

- Lemburg, M. A. (1999). *PEP 249 – Python Database API Specification v2.0*. <https://peps.python.org/pep-0249/>
- Python Software Foundation. (2026). *sqlite3 — DB-API 2.0 interface for SQLite databases*. <https://docs.python.org/3/library/sqlite3.html>
- SQLAlchemy developers. (2026). *Engine configuration*. <https://docs.sqlalchemy.org/en/20/core/engines.html>
- pandas development team. (2026). *pandas.read_sql* y *pandas.DataFrame.to_sql*. <https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html>
- MongoDB Inc. (2026). *Aggregation pipeline* y *Query documents*, MongoDB Manual. <https://www.mongodb.com/docs/manual/core/aggregation-pipeline/>
- MongoDB Inc. (2026). *PyMongo documentation*. <https://pymongo.readthedocs.io/>
- TinyDB developers. (2026). *TinyDB documentation*. <https://tinydb.readthedocs.io/>
- Snowflake Inc. (2026). *Streamlit: Secrets management*. <https://docs.streamlit.io/develop/concepts/connections/secrets-management>

### Artículos

- Gilbert, S. y Lynch, N. (2002). Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, 33(2), 51-59.
