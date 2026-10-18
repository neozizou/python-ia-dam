# El conjunto de datos del curso

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

Todo el módulo trabaja con el mismo fichero: `jugadores.csv`. Lo usarás en las siete unidades, desde leerlo a mano con Python puro en la UD1 hasta entrenar un modelo con él en la UD6 y publicar una aplicación en la UD7.

## Qué son estos datos

Son las valoraciones de los jugadores del videojuego **FIFA**, de EA Sports, en sus ediciones de 2015 a 2020. Cada año, un equipo de ojeadores y analistas puntúa a los jugadores de las ligas del mundo en una escala de 1 a 99: lo rápidos que son, cómo rematan, cómo pasan. De ahí sale la **media** (`overall`), que es el número que resume a un jugador, y una estimación de su **valor de mercado** y su **salario**.

> [!NOTE]
> Son datos reales, aunque vengan de un videojuego. Las valoraciones las produce un equipo humano a partir de observar partidos, y los valores de mercado se apoyan en los traspasos que de verdad ocurren. No son medidas físicas: son **opiniones expertas convertidas en números**, y eso tiene consecuencias que verás en la UD6.

| | |
| --- | --- |
| **Origen** | [FIFA 20 complete player dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-20-complete-player-dataset), de Stefano Leone, en Kaggle |
| **Datos originales** | [sofifa.com](https://sofifa.com), que recopila las valoraciones de cada edición del juego |
| **Licencia** | CC0 1.0 (dominio público): se puede usar, copiar y modificar sin restricciones |
| **Versión** | 1, publicada el 26/09/2019. Está fijada: no cambiará durante el curso |
| **Tamaño** | 100.995 filas × 37 columnas · 19,5 MB |

## Qué tiene dentro

| | |
| --- | --- |
| Filas | 100.995 |
| Jugadores distintos | 36.559 |
| Ediciones | 6 (FIFA 15 a FIFA 20) |
| Clubes | 918 |
| Nacionalidades | 179 |
| Filas duplicadas | ninguna |

Cada fila es **un jugador en una edición**. El mismo jugador aparece hasta seis veces, una por año, con su `sofifa_id` siempre igual. Eso permite seguirlo en el tiempo: cómo sube su media, cómo cambia de club, cómo se encarece.

```text
fifa  sofifa_id  short_name   age  club           overall  value_eur
2015  158023     L. Messi     27   FC Barcelona   93       0
2016  158023     L. Messi     28   FC Barcelona   94       111000000
2017  158023     L. Messi     29   FC Barcelona   93       104500000
```

## Las 37 columnas

### Quién es

| Columna | Qué es | Detalles |
| --- | --- | --- |
| `fifa` | Edición del juego: de 2015 a 2020 | La hemos añadido nosotros al juntar los seis ficheros |
| `sofifa_id` | Identificador del jugador | El mismo en todas las ediciones. Es la clave para seguirlo en el tiempo |
| `short_name` | Nombre corto | `L. Messi`. Se repite entre jugadores distintos: **no sirve de clave** |
| `long_name` | Nombre completo | `Lionel Andrés Messi Cuccittini` |
| `age` | Edad en años | De 16 a 47 |
| `dob` | Fecha de nacimiento | Formato `AAAA-MM-DD`. Al leer el CSV llega como texto |
| `nationality` | Selección a la que pertenece | 179 valores, en inglés |
| `height_cm` | Altura en centímetros | De 154 a 205 |
| `weight_kg` | Peso en kilos | De 49 a 110 |

### Dónde juega

| Columna | Qué es | Detalles |
| --- | --- | --- |
| `club` | Club en el que está esa temporada | 918 valores |
| `team_position` | Puesto que ocupa en su club | 1,3 % de nulos: suplentes y reservas |
| `joined` | Fecha en que fichó por el club | 8,0 % de nulos |
| `contract_valid_until` | Año en que termina su contrato | De 2014 a 2026. Llega como decimal (`2021.0`) |
| `player_positions` | Posiciones en las que puede jugar | **Una o varias, separadas por comas**: `RW, CF, ST`. 15 posiciones distintas; 2.481 jugadores tienen tres |
| `preferred_foot` | Pie bueno | `Left` o `Right` |
| `work_rate` | Esfuerzo en ataque y en defensa | **Dos valores en uno**: `Medium/Low` |
| `body_type` | Complexión | Debería ser `Lean`, `Normal` o `Stocky`, pero trae también nombres de jugadores (`Messi`, `C. Ronaldo`) y un código interno sin traducir (`PLAYER_BODY_TYPE_25`) |

### Cuánto vale

| Columna | Qué es | Detalles |
| --- | --- | --- |
| `overall` | Media del jugador, de 40 a 94 | El número que resume su nivel actual |
| `potential` | Media que se le estima a futuro | Nunca baja de `overall`. La diferencia es su margen de mejora |
| `value_eur` | Valor de mercado en euros | Hasta 123 millones. **Cero en FIFA 15 y en unos 250 agentes libres por edición** |
| `wage_eur` | Salario semanal en euros | Hasta 565.000. Mismo problema de ceros |
| `release_clause_eur` | Cláusula de rescisión | 51,1 % de nulos: **no existe en FIFA 15, 16 ni 17** |
| `international_reputation` | Fama internacional, de 1 a 5 | Muy desequilibrada: casi todos son 1 |
| `weak_foot` | Calidad del pie malo, de 1 a 5 | |
| `skill_moves` | Repertorio de filigranas, de 1 a 5 | |

### Cómo juega

Seis resúmenes de 1 a 99, **vacíos en los porteros** (11,1 % de las filas):

`pace` (velocidad) · `shooting` (remate) · `passing` (pase) · `dribbling` (regate) · `defending` (defensa) · `physic` (físico)

### Cómo para

Seis valoraciones de portero, **vacías en los jugadores de campo** (88,9 % de las filas):

`gk_diving` (estirada) · `gk_handling` (blocaje) · `gk_kicking` (saque) · `gk_reflexes` (reflejos) · `gk_speed` (velocidad) · `gk_positioning` (colocación)

> [!IMPORTANT]
> Estos dos bloques son **complementarios**: donde uno tiene datos, el otro está vacío, y al revés. Un portero no tiene `pace` porque la columna no se le aplica, no porque se haya perdido el dato. Rellenar esos huecos con la media de la columna sería un error grave: estarías inventando que los porteros corren como los delanteros. Volveremos a esto en la UD3.

## Las tres trampas que trae

Ningún conjunto de datos real viene limpio. Este tiene tres problemas, y conviene conocerlos antes de darse de bruces con ellos.

**1. FIFA 15 no tiene dinero.** Las 15.465 filas de 2015 traen `value_eur` y `wage_eur` a cero y `release_clause_eur` vacía. No es que esos jugadores no valieran nada: es que esa edición del dataset no recoge el dato. Si calculas el valor medio por año sin darte cuenta, te saldrá que en 2015 todos los jugadores del mundo valían cero euros.

**2. Hay ceros que son ausencias.** Además de FIFA 15, cada edición trae unos 250 jugadores con valor cero: son agentes libres, sin contrato. Un cero aquí no significa «vale cero euros», significa «no hay dato».

**3. `body_type` está sucia.** Diez valores donde debería haber tres, con nombres propios y un código interno del juego. Es lo que pasa cuando alguien mete un campo libre donde tenía que haber una lista cerrada.

> [!TIP]
> Las tres se arreglan, y arreglarlas es parte del trabajo. Lo que no se puede es ignorarlas: un análisis hecho sobre datos sucios da un resultado limpio y equivocado, que es lo peor de todo.

## Qué se puede preguntar a estos datos

Estas son las preguntas alrededor de las que gira el curso:

| Unidad | Pregunta |
| --- | --- |
| UD1 | ¿Qué hay aquí dentro? Cuántas filas, qué columnas, cuántos huecos |
| UD3 | ¿De qué depende que un jugador valga mucho? ¿Qué cambia de FIFA 16 a FIFA 20? |
| UD4 | ¿Qué club tiene la plantilla más cara? ¿Qué país produce más porteros? |
| UD5 | ¿Cómo se trabaja con esto cuando son cien mil filas y no cien? |
| UD6 | ¿Se puede predecir el salario de un jugador a partir de lo que sabemos de él? |
| UD7 | ¿Cómo se publica eso para que cualquiera lo use desde el navegador? |

## Cómo conseguirlo

El fichero ya está en el repositorio, en `datos-comunes/jugadores.csv`, así que no hace falta hacer nada para empezar.

Aun así, **descárgalo tú al menos una vez**: saber moverse por Kaggle y usar su API es parte del oficio, y el día que necesites datos para un proyecto propio vas a empezar ahí.

1. Crea una cuenta en [kaggle.com](https://www.kaggle.com).
2. Entra en **Settings → API → Create New Token**. Se descarga un `kaggle.json`.
3. Guárdalo en `~/.kaggle/kaggle.json` (en Windows, `C:\Users\<tu_usuario>\.kaggle\kaggle.json`).
4. Instala la biblioteca y ejecuta el script:

```bash
pip install kagglehub
python datos-comunes/preparar.py
```

[`preparar.py`](preparar.py) descarga la versión 1 del dataset original, apila las seis ediciones, se queda con las 37 columnas y vuelve a escribir `jugadores.csv`. Si lo ejecutas, debería salirte un fichero idéntico al que ya está en el repositorio.

> [!WARNING]
> Fíjate en que el script pide la **versión 1** del dataset, no «la última». Si pidiera la última y el autor publicara otra a mitad de curso, cada uno tendría datos distintos y dejaríamos de poder comparar resultados.

## Fuentes

- Leone, S. (2019). *FIFA 20 complete player dataset*. Licencia CC0 1.0. <https://www.kaggle.com/datasets/stefanoleone992/fifa-20-complete-player-dataset>
- SoFIFA. *Player database*. <https://sofifa.com>
- Kaggle. *kagglehub: download and share datasets from Python*. <https://github.com/Kaggle/kagglehub>
