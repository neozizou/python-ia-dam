# UD1 · Python para quien ya programa

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [1.1 El ecosistema Python](#11-el-ecosistema-python)
- [1.2 Sintaxis y tipos básicos](#12-sintaxis-y-tipos-básicos)
- [1.3 Control de flujo](#13-control-de-flujo)
- [1.4 Funciones](#14-funciones)
- [1.5 Estructuras de datos](#15-estructuras-de-datos)
- [1.6 Ficheros: texto, CSV y JSON](#16-ficheros-texto-csv-y-json)
- [1.7 Errores, excepciones y depuración](#17-errores-excepciones-y-depuración)
- [1.8 Módulos y paquetes](#18-módulos-y-paquetes)
- [Práctica de la unidad · Hito 0 del proyecto integrador](#práctica-de-la-unidad--hito-0-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD1](#bibliografía-de-la-ud1)

## Presentación de la unidad

En esta unidad, de 7 horas, trasladas a Python lo que ya sabes hacer en C++ y terminas leyendo y procesando un conjunto de datos real con Python puro, sin bibliotecas externas. No empezamos de cero: el objetivo es aprender qué hace distinto Python y escribir código «pythónico», no traducir C++ línea a línea.

### Resultado de aprendizaje y criterios de evaluación

**RA1.** Implementa programas básicos en Python aplicados a la manipulación de datos.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 1a | Desarrolla programas en Python con variables, estructuras de control y funciones | 1.2, 1.3, 1.4 |
| 1b | Utiliza estructuras de datos (listas, diccionarios, tuplas) para organizar la información | 1.5 |
| 1c | Procesa archivos de texto con Python aplicando métodos de manipulación de datos | 1.6 |
| 1d | Detecta y gestiona errores en el código con técnicas de depuración y control de flujo | 1.7 |
| 1e | Diseña, estructura y utiliza módulos y paquetes para organizar y reutilizar el código | 1.1, 1.8 |

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Lunes 21/09/2026 | 2 | 1.1 Ecosistema e instalación · 1.2 Sintaxis y tipos |
| 2 | Martes 22/09/2026 | 1 | 1.3 Control de flujo |
| 3 | Lunes 28/09/2026 | 2 | 1.4 Funciones · 1.5 Estructuras de datos |
| 4 | Martes 29/09/2026 | 1 | 1.6 Ficheros |
| 5 | Lunes 05/10/2026 (1.ª hora) | 1 | 1.7 Errores y depuración · 1.8 Módulos y paquetes |

El ritmo es alto porque partes de saber programar. Las sesiones se dedican sobre todo a practicar; la lectura completa de cada apartado y los ejercicios marcados como autónomos se hacen fuera del aula.

### Requisitos previos

- Haber superado Programación de 1.º (C++): variables, control de flujo, funciones, vectores y clases.
- Nociones de SQL de Bases de Datos de 1.º (se retoman en la UD4).
- Portátil propio con permisos de administrador para instalar software.

### Cómo usar esta carpeta

| Carpeta | Contenido |
| --- | --- |
| [`listados/`](listados/) | Todos los listados de la unidad como ficheros `.py` listos para ejecutar, más los datos de ejemplo en `listados/datos/` |
| [`proyecto/`](proyecto/) | El proyecto completo del apartado 1.8: paquete `ventas`, `pyproject.toml` y datos |

Ejecuta los listados **desde la carpeta `listados/`**, con tu entorno virtual activado, para que las rutas relativas a `datos/` funcionen:

```bash
cd ud1-python/listados
python listado_1_33_resumen_ventas.py
```

Los fragmentos que empiezan por `>>>` son sesiones del intérprete interactivo y no tienen fichero: se escribe lo que sigue a `>>>` y la línea siguiente es la respuesta de Python.

### Convenciones de estos apuntes

- **Listado 1.x**: código completo que puedes copiar y ejecutar. El enlace «ver fichero» abre su versión en `listados/`.
- **Desde C++**: comparación directa con lo que ya conoces, para evitar los errores típicos de quien cambia de lenguaje.
- **Para practicar**: ejercicios cortos al final de cada apartado. Los marcados con (A) son de trabajo autónomo.
- Los nombres de ficheros, órdenes de terminal y fragmentos de código dentro del texto aparecen en `fuente monoespaciada`.

## 1.1 El ecosistema Python

En este módulo trabajaremos con **Python 3.14**, **VS Code** con las extensiones Python y Jupyter, y **un entorno virtual por proyecto**. Este apartado deja tu portátil listo para el resto del curso.

### Python frente a C++

| Aspecto | C++ | Python |
| --- | --- | --- |
| Ejecución | Se compila a código máquina antes de ejecutar | El intérprete (CPython) traduce el código a *bytecode* y lo ejecuta al momento |
| Tipado | Estático: el tipo se declara y se comprueba al compilar | Dinámico pero fuerte: el tipo lo tiene el valor, no la variable, y no hay conversiones implícitas entre tipos incompatibles |
| Bloques | Llaves `{ }` y punto y coma | Sangría obligatoria de 4 espacios y dos puntos `:` |
| Memoria | Manual o RAII (`new`/`delete`, punteros inteligentes) | Automática: el intérprete libera los objetos que ya no se usan |
| Bibliotecas | STL y bibliotecas externas que hay que compilar y enlazar | Biblioteca estándar muy amplia y miles de paquetes instalables con `pip` desde PyPI |

La consecuencia práctica: en Python escribes menos código y pruebas antes, pero muchos errores que C++ detectaba al compilar aparecen solo al ejecutar. Por eso en este módulo insistiremos en probar el código a menudo y en leer bien los mensajes de error (apartado 1.7).

### Qué versión usar

A fecha de hoy, las versiones 3.14 y 3.13 están en fase de mantenimiento activo, y la 3.15 tiene su publicación prevista para el 1 de octubre de 2026 ([Python Developer's Guide](https://devguide.python.org/versions/)). Usaremos **Python 3.14**: es estable y las bibliotecas del curso ya la soportan; por ejemplo, scikit-learn 1.8 funciona con Python 3.11 a 3.14 ([scikit-learn 1.8.0](https://zenodo.org/records/6968622/latest)). Evitaremos la 3.15 durante este curso, porque las bibliotecas científicas tardan unos meses en publicar versiones compatibles.

Python 2 dejó de tener soporte el 1 de enero de 2020 ([Python Developer's Guide](https://devguide.python.org/versions/)). Si consultas material antiguo, como el libro *Python para todos* de la bibliografía, verás `raw_input()` en lugar de `input()` y `print` sin paréntesis: es sintaxis de Python 2 y no funciona en Python 3.

### Instalación en tu portátil

**Windows.** La forma recomendada es el **Python install manager**, que se instala desde la Microsoft Store o con `winget install 9NQ7512CXL7T`. El instalador tradicional dejará de publicarse con Python 3.16 ([python.org](https://www.python.org/downloads/latest/pymanager)). Una vez instalado el gestor, usa la orden `py`:

**Listado 1.1.** Instalación y comprobación de Python en Windows (PowerShell)

```powershell
py install 3.14        # instala Python 3.14
py list                # muestra las versiones instaladas
py -3.14 --version     # comprueba la versión
```

**macOS.** Descarga el instalador oficial desde python.org/downloads. Tras instalarlo, la orden es `python3.14` (o `python3`).

**Linux.** Usa el Python de tu distribución (3.12 o superior sirve para esta unidad) e instala también el paquete de entornos virtuales; en Debian y Ubuntu es `python3-venv`.

### VS Code y las extensiones Python y Jupyter

Instala VS Code y, desde la vista de extensiones (`Ctrl+Mayús+X`), añade **Python** (Microsoft) y **Jupyter** (Microsoft). La extensión Jupyter permite usar cualquier entorno de Python como *kernel* de un notebook, siempre que ese entorno tenga instalado el paquete de Jupyter ([microsoft/vscode-jupyter](https://github.com/microsoft/vscode-jupyter)). Tres órdenes de la paleta (`Ctrl+Mayús+P`) que usarás a diario:

| Orden | Para qué sirve |
| --- | --- |
| `Python: Select Interpreter` | Elegir con qué Python se ejecutan los scripts del proyecto |
| `Jupyter: Create New Jupyter Notebook` | Crear un notebook nuevo |
| `Notebook: Select Notebook Kernel` | Elegir con qué entorno se ejecutan las celdas del notebook |

### Un entorno virtual por proyecto

Un entorno virtual es una carpeta con su propio intérprete y su propio conjunto de paquetes, aislados del resto del sistema. Por convenio se llama `.venv` y vive dentro de la carpeta del proyecto. La documentación oficial insiste en tres ideas: no se sube a Git, no se copia ni se mueve, y debe poder borrarse y recrearse en cualquier momento ([docs.python.org, venv](https://docs.python.org/3/library/venv.html)).

**Listado 1.2.** Crear el proyecto del curso y su entorno virtual en Windows (PowerShell)

```powershell
mkdir python-ia
cd python-ia
py -3.14 -m venv .venv                   # crea el entorno
.venv\Scripts\Activate.ps1               # lo activa
python -m pip install --upgrade pip
python -m pip install ipykernel          # necesario para los notebooks
```

Si PowerShell no deja ejecutar `Activate.ps1`, hay que permitir los scripts locales para tu usuario con la orden siguiente ([docs.python.org, venv](https://docs.python.org/3/library/venv.html)):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Listado 1.3.** Lo mismo en macOS y Linux (bash/zsh)

```bash
mkdir python-ia && cd python-ia
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install ipykernel
```

Con el entorno activado, el indicador de la terminal muestra `(.venv)`. Para salir, escribe `deactivate`. Desde Python 3.13, `venv` crea automáticamente un `.gitignore` dentro del entorno para que Git lo ignore ([docs.python.org, venv](https://docs.python.org/3/library/venv.html)).

> [!TIP]
> **Buena práctica.** Escribe siempre `python -m pip` en lugar de `pip` a secas. Así tienes la garantía de que el paquete se instala en el intérprete que estás usando y no en otro Python del sistema.

### Tres formas de ejecutar Python

**1. El intérprete interactivo.** Escribe `python` en la terminal y prueba expresiones sueltas. Es la calculadora del programador.

```python
>>> 2 ** 100
1267650600228229401496703205376
>>> "dam".upper()
'DAM'
```

**2. Un script.** Un fichero `.py` que se ejecuta de principio a fin con `python nombre.py`.

**Listado 1.4.** `hola.py`: primer script · [ver fichero](listados/listado_1_04_hola.py)

```python
import sys

nombre = input("¿Cómo te llamas? ")
version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"Hola, {nombre}. Estás usando Python {version}.")

# True si se está ejecutando dentro de un entorno virtual
print("¿Entorno virtual?", sys.prefix != sys.base_prefix)
```

La última línea usa la comprobación que recomienda la propia documentación: dentro de un entorno virtual, `sys.prefix` y `sys.base_prefix` son distintos ([docs.python.org, venv](https://docs.python.org/3/library/venv.html)).

**3. Un notebook.** Un fichero `.ipynb` con celdas de código y de texto que se ejecutan una a una y guardan sus resultados. Crea `exploracion.ipynb`, pulsa *Select Kernel* arriba a la derecha y elige el entorno `.venv` del proyecto.

| Usa… | Cuando… |
| --- | --- |
| Script o módulo `.py` | El código se va a reutilizar, probar o desplegar |
| Notebook `.ipynb` | Estás explorando datos o presentando un análisis con texto y gráficos |

### Estilo: PEP 8

PEP 8 es la guía de estilo oficial de Python; parte de la idea de que el código se lee muchas más veces de las que se escribe ([PEP 8](https://www.python.org/dev/peps/pep-0008/)). Las reglas que aplicaremos desde el primer día:

- Sangría de 4 espacios, nunca tabuladores.
- Líneas de 79 caracteres como máximo.
- `snake_case` para variables y funciones, `CamelCase` para clases y `MAYUSCULAS` para constantes.
- Los `import` van al principio del fichero, uno por línea.

Configura VS Code para formatear al guardar con un formateador automático, por ejemplo Ruff o Black. Así el estilo deja de ser una preocupación.

### Estructura del proyecto del curso

```text
python-ia/
├── .venv/              entorno virtual (no se sube a Git)
├── datos/              ficheros de datos originales
├── notebooks/          exploración y análisis
├── src/                código reutilizable (módulos y paquetes)
└── requirements.txt    dependencias del proyecto (apartado 1.8)
```

### Para practicar

1. Instala Python 3.14, VS Code y las extensiones Python y Jupyter. Crea el proyecto `python-ia` con su entorno virtual.
2. Ejecuta `hola.py` desde la terminal con el entorno activado y comprueba que la última línea muestra `True`. Desactiva el entorno y vuelve a ejecutarlo: ¿qué cambia?
3. Crea `notebooks/exploracion.ipynb`, selecciona el kernel `.venv` y ejecuta `import sys; sys.executable`. La ruta debe apuntar dentro de `.venv`.
4. (A) Ejecuta `import this` en el intérprete. Elige dos aforismos y explica cada uno con un ejemplo de código C++ que lo incumpla.

## 1.2 Sintaxis y tipos básicos

En Python no se declaran tipos: una variable es un **nombre que apunta a un objeto**, y es el objeto el que tiene tipo. Todo lo demás de este apartado se deriva de esa idea. El tutorial oficial, pensado precisamente para programadores que llegan desde otro lenguaje, cubre estos contenidos en su capítulo 3 ([The Python Tutorial](https://docs.python.org/3/tutorial/introduction.html)).

### Variables: etiquetas, no cajas

**Listado 1.5.** El tipo va con el valor, no con el nombre

```python
>>> edad = 20
>>> type(edad)
<class 'int'>
>>> edad = "veinte"        # el mismo nombre apunta ahora a un str
>>> type(edad)
<class 'str'>
```

> [!NOTE]
> **Desde C++.** En C++, `int edad;` reserva una caja de memoria que solo admite enteros. En Python, `edad` es una etiqueta que puedes despegar y pegar en cualquier objeto. Eso no significa que Python sea «débil» con los tipos: no mezcla tipos incompatibles por su cuenta.

**Listado 1.6.** Tipado dinámico pero fuerte

```python
>>> "20" + 1
TypeError: can only concatenate str (not "int") to str
>>> int("20") + 1          # la conversión siempre es explícita
21
```

Dos detalles de sintaxis que usarás constantemente:

- **Asignación múltiple.** `a, b = 1, 2` asigna a la vez, y `a, b = b, a` intercambia dos valores sin variable auxiliar.
- **Constantes por convenio.** No existe `const`. Un nombre en mayúsculas, como `IVA = 0.21`, indica a quien lee que no debe modificarse.

### Números

| Tipo | Ejemplo | Observaciones |
| --- | --- | --- |
| `int` | `42`, `1_000_000` | Precisión ilimitada: no hay desbordamiento. El guion bajo solo mejora la lectura |
| `float` | `3.14`, `2.5e-3` | Coma flotante de doble precisión, como `double` en C++ |
| `complex` | `3 + 4j` | Números complejos nativos |

**Listado 1.7.** Operadores aritméticos: las diferencias con C++ están en la división

```python
>>> 7 / 2          # división real, SIEMPRE devuelve float
3.5
>>> 7 // 2         # división entera (redondea hacia abajo)
3
>>> -7 // 2        # hacia abajo, no hacia cero: en C++ -7/2 da -3
-4
>>> 7 % 3          # resto
1
>>> 2 ** 0.5       # potencia
1.4142135623730951
```

**Listado 1.8.** La coma flotante no es exacta

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
>>> import math
>>> math.isclose(0.1 + 0.2, 0.3)     # así se comparan floats
True
>>> round(2.5), round(3.5)           # redondeo al par más cercano
(2, 4)
```

El problema de `0.1 + 0.2` no es de Python, sino de la representación binaria de los decimales; ocurre igual en C++. El tutorial le dedica el capítulo 15 ([The Python Tutorial](https://docs.python.org/3/tutorial/floatingpoint.html)).

### Booleanos y `None`

- Los valores son `True` y `False`, con mayúscula inicial. Los operadores lógicos son palabras: `and`, `or`, `not`, en lugar de `&&`, `||`, `!`.
- Las comparaciones se pueden encadenar como en matemáticas: `0 <= nota <= 10`.
- `None` representa la ausencia de valor, parecido a `nullptr`. Se compara con `is`: `if resultado is None:`.
- Cualquier objeto tiene un valor de verdad. Son **falsos** `0`, `0.0`, `""`, `[]`, `{}` y `None`; casi todo lo demás es verdadero. Por eso es idiomático escribir `if lista:` en lugar de `if len(lista) > 0:`.

### Cadenas de texto (`str`)

Las cadenas son secuencias **inmutables** de caracteres Unicode. Se escriben con comillas simples o dobles, y con comillas triples si ocupan varias líneas.

**Listado 1.9.** Índices y rebanadas (*slicing*)

```python
>>> s = "Python"
>>> s[0], s[-1]            # primer y último carácter
('P', 'n')
>>> s[1:4]                 # desde el índice 1 hasta el 4 (sin incluirlo)
'yth'
>>> s[:3], s[3:]
('Pyt', 'hon')
>>> s[::-1]                # paso -1: la cadena al revés
'nohtyP'
>>> s[0] = "J"
TypeError: 'str' object does not support item assignment
```

Los métodos de `str` que más usarás al procesar datos:

| Método | Ejemplo | Resultado |
| --- | --- | --- |
| `strip()` | `"  hola \n".strip()` | `'hola'` |
| `split(sep)` | `"a,b,,c".split(",")` | `['a', 'b', '', 'c']` |
| `join(iterable)` | `" ".join(["a", "b"])` | `'a b'` |
| `replace(a, b)` | `"Hola".replace("o", "0")` | `'H0la'` |
| `upper()`, `lower()`, `title()` | `"hola mundo".title()` | `'Hola Mundo'` |
| `startswith()`, `endswith()` | `"datos.csv".endswith(".csv")` | `True` |
| `find(sub)`, `count(sub)` | `"banana".count("a")` | `3` |

### f-strings: formatear la salida

Una f-string es una cadena precedida de `f` en la que las expresiones entre llaves se evalúan. Tras los dos puntos se indica el formato ([The Python Tutorial](https://docs.python.org/3/tutorial/inputoutput.html)).

**Listado 1.10.** Procesar y formatear una línea de datos · [ver fichero](listados/listado_1_10_linea_datos.py)

```python
linea = "  Portátil;899.90;12 \n"

nombre, precio, stock = linea.strip().split(";")
precio = float(precio)
stock = int(stock)

print(f"{nombre:<10} {precio:>8.2f} € x {stock:>3} = {precio * stock:>9.2f} €")
# Portátil     899.90 € x  12 =  10798.80 €
```

| Especificador | Significado | Ejemplo |
| --- | --- | --- |
| `:.2f` | 2 decimales | `f"{899.9:.2f}"` → `899.90` |
| `:>8` / `:<10` | Alinear a la derecha / izquierda en ese ancho | `f"{'DAM':>6}"` → `'   DAM'` |
| `:,` | Separador de miles | `f"{1234567:,}"` → `1,234,567` |
| `:.1%` | Porcentaje | `f"{0.2345:.1%}"` → `23.4%` |
| `=` | Muestra la expresión y su valor (depuración) | `f"{x=}"` → `x=42` |

### Entrada por teclado y conversiones

`input()` **siempre devuelve un `str`**, aunque el usuario escriba un número. Hay que convertirlo con `int()` o `float()`. Si el texto no es convertible, Python lanza un `ValueError`: por ejemplo, `int("3.5")` falla. Veremos cómo capturar ese error en el apartado 1.7.

> [!WARNING]
> Cuidado con `bool()`: `bool("False")` devuelve `True`, porque cualquier cadena no vacía es verdadera.

### Para practicar

1. Predice el resultado y compruébalo en el intérprete: `7 / 2`, `7 // 2`, `-7 // 2`, `-7 % 3`, `2 ** 0.5`, `round(2.5)`, `round(3.5)`.
2. Escribe `conversor.py`, que pida una temperatura en grados Celsius y muestre su equivalente en Fahrenheit con un decimal.
3. A partir de `"  garcía lópez, ana  "`, obtén y muestra `"Ana García López"` usando solo métodos de `str`.
4. (A) Lee el capítulo 15 del tutorial y explica con tus palabras por qué `0.1 + 0.2 != 0.3`. ¿Qué consecuencias tiene al comparar importes en euros?

## 1.3 Control de flujo

Las estructuras son las que ya conoces, con dos cambios de mentalidad: `for` recorre **elementos**, no índices, y `match` sustituye a `switch` con mucha más potencia. Los bloques se delimitan con dos puntos y sangría; no hay llaves.

### Condicionales: `if`, `elif`, `else`

**Listado 1.11.** Calificación a partir de una nota · [ver fichero](listados/listado_1_11_calificacion.py)

```python
nota = 7.5

if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elif nota < 5:
    calificacion = "Insuficiente"
elif nota < 6:
    calificacion = "Suficiente"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print(calificacion)      # Notable
```

Para asignaciones sencillas existe la **expresión condicional**, equivalente al operador ternario de C++:

```python
estado = "aprobado" if nota >= 5 else "suspenso"
```

### `match`: coincidencia de patrones

`match`, disponible desde Python 3.10, compara un valor con una serie de **patrones**. Además de valores literales, puede reconocer estructuras, capturar partes en variables y combinar alternativas con `|` ([The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#match-statements)).

**Listado 1.12.** Intérprete de órdenes con `match` · [ver fichero](listados/listado_1_12_ordenes_match.py)

```python
comando = input("Orden: ").strip().lower()

match comando.split():
    case ["salir"]:
        print("Hasta luego")
    case ["cargar", fichero]:                  # captura el 2.º elemento
        print(f"Cargando {fichero}...")
    case ["filtrar", columna, valor]:
        print(f"Filtrando {columna} = {valor}")
    case ["ayuda" | "?"]:                      # alternativas
        print("Órdenes: cargar, filtrar, salir")
    case _:                                    # comodín: cualquier otro caso
        print(f"Orden desconocida: {comando}")
```

Con la entrada `cargar ventas.csv`, el programa muestra `Cargando ventas.csv...`; con `borrar todo`, llega al comodín.

> [!NOTE]
> **Desde C++.** `match` no tiene *fallthrough*: se ejecuta solo el primer `case` que encaja y no hace falta `break`. Tampoco se limita a enteros o enumerados: compara listas, tuplas, diccionarios y objetos.

### Bucle `for`: recorrer elementos

El `for` de Python equivale al *range-based for* de C++ (`for (auto x : v)`). Nunca necesitas gestionar un índice a mano; si lo necesitas, `enumerate` te lo da.

**Listado 1.13.** Las cuatro formas habituales de `for` · [ver fichero](listados/listado_1_13_bucles_for.py)

```python
ciudades = ["Granada", "Málaga", "Sevilla"]
temperaturas = [21.5, 24.0, 27.3]

for ciudad in ciudades:                          # 1. elemento a elemento
    print(ciudad)

for i, ciudad in enumerate(ciudades, start=1):   # 2. con su posición
    print(f"{i}. {ciudad}")

for ciudad, t in zip(ciudades, temperaturas):    # 3. dos secuencias en paralelo
    print(f"{ciudad}: {t} °C")

for n in range(10, 0, -2):                       # 4. una secuencia de enteros
    print(n, end=" ")                            # 10 8 6 4 2
```

`range(inicio, fin, paso)` genera enteros desde `inicio` hasta `fin` **sin incluirlo**. Con un solo argumento empieza en 0: `range(5)` produce 0, 1, 2, 3 y 4.

### Bucle `while`, `break` y `continue`

Python no tiene `do … while`. El idioma equivalente es un `while True` que se rompe con `break` cuando se cumple la condición de salida.

**Listado 1.14.** Validar una entrada hasta que sea correcta · [ver fichero](listados/listado_1_14_validar_edad.py)

```python
while True:
    texto = input("Edad (0-120): ")
    if texto.isdigit() and 0 <= int(texto) <= 120:
        break
    print("Valor no válido, inténtalo de nuevo.")

edad = int(texto)
print(f"Edad registrada: {edad}")
```

`continue` salta a la siguiente iteración y `pass` es una instrucción vacía, útil cuando la sintaxis exige un bloque que aún no has escrito.

### La cláusula `else` de los bucles

Un bucle puede llevar `else`: ese bloque se ejecuta si el bucle termina **sin** pasar por `break`. Es la forma idiomática de expresar «busqué y no lo encontré».

**Listado 1.15.** Números primos con `for … else` (adaptado del tutorial oficial) · [ver fichero](listados/listado_1_15_primos.py)

```python
for n in range(2, 20):
    for divisor in range(2, n):
        if n % divisor == 0:
            break              # tiene un divisor: no es primo
    else:
        print(n, "es primo")   # el for interno terminó sin break
```

### Tabla de equivalencias C++ → Python

| C++ | Python |
| --- | --- |
| `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| `for (auto x : v)` | `for x in v:` |
| `switch (x) { case 1: …; break; }` | `match x:` / `case 1:` (sin `break`) |
| `do { … } while (c);` | `while True:` … `if not c: break` |
| `i++` | `i += 1` |
| `c ? a : b` | `a if c else b` |
| `&&`, `\|\|`, `!` | `and`, `or`, `not` |

### Para practicar

1. Escribe FizzBuzz del 1 al 30: múltiplos de 3 → `Fizz`, de 5 → `Buzz`, de ambos → `FizzBuzz`.
2. Crea una calculadora con un menú que se repita hasta que el usuario escriba `salir`. Usa `while True` y `match` para las órdenes `suma a b`, `resta a b` y `salir`.
3. Dadas `nombres = ["Ana", "Luis", "Eva"]` y `notas = [6.5, 4.0, 9.1]`, muestra cada alumno con su posición y su nota, y cuenta cuántos han aprobado.
4. (A) Reescribe este bucle de C++ de forma pythónica, sin manejar el índice a mano:

```cpp
for (int i = 0; i < v.size(); i++) {
    cout << i << ": " << v[i] << endl;
}
```

## 1.4 Funciones

Una función se define con `def`, puede devolver varios valores a la vez y admite parámetros por nombre y con valor por defecto. Las funciones son objetos: se pueden guardar en variables y pasar a otras funciones. El tutorial oficial trata todo esto en sus apartados 4.8 y 4.9 ([The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)).

### Definición, documentación y anotaciones de tipo

**Listado 1.16.** Una función bien escrita · [ver fichero](listados/listado_1_16_media.py)

```python
def media(valores: list[float]) -> float:
    """Devuelve la media aritmética de una lista no vacía de números."""
    return sum(valores) / len(valores)


print(media([4.5, 7.0, 9.25, 6.0]))    # 6.6875
```

- La cadena entre comillas triples tras la cabecera es el **docstring**: documenta la función y aparece al escribir `help(media)` o al pasar el ratón por encima en VS Code.
- `valores: list[float]` y `-> float` son **anotaciones de tipo**. Python **no las comprueba** al ejecutar: `media("hola")` falla dentro de `sum`, no al llamarla. Sirven para documentar y para que el editor detecte errores antes de ejecutar.
- Una función sin `return` devuelve `None`.

### Devolver varios valores

**Listado 1.17.** Retorno múltiple y desempaquetado · [ver fichero](listados/listado_1_17_estadisticas.py)

```python
def estadisticas(valores: list[float]) -> tuple[float, float, float]:
    """Devuelve el mínimo, el máximo y la media."""
    return min(valores), max(valores), sum(valores) / len(valores)


minimo, maximo, promedio = estadisticas([4.5, 7.0, 9.25, 6.0])
```

En realidad la función devuelve **una tupla** de tres elementos, que se desempaqueta en tres variables. En C++ necesitarías un `struct`, un `std::tuple` o parámetros por referencia.

### Tipos de parámetros

**Listado 1.18.** Valores por defecto y parámetros solo por nombre · [ver fichero](listados/listado_1_18_precio_final.py)

```python
def precio_final(base: float, iva: float = 0.21, *, descuento: float = 0.0) -> float:
    """Aplica el descuento y después el IVA.

    Los parámetros que siguen a * solo se pueden pasar por nombre.
    """
    return round(base * (1 - descuento) * (1 + iva), 2)


precio_final(100)                   # 121.0
precio_final(100, 0.10)             # 110.0
precio_final(100, descuento=0.2)    # 96.8
precio_final(iva=0.04, base=50)     # 52.0  (por nombre, en cualquier orden)
precio_final(100, 0.21, 0.2)        # TypeError: descuento debe ir por nombre
```

Obligar a pasar un parámetro por nombre evita errores de orden y hace legibles las llamadas. Es un patrón que verás constantemente en pandas y scikit-learn.

**Listado 1.19.** Número variable de argumentos: `*args` y `**kwargs` · [ver fichero](listados/listado_1_19_args_kwargs.py)

```python
def resumen(*valores, **opciones):
    """valores llega como tupla; opciones, como diccionario."""
    decimales = opciones.get("decimales", 2)
    total = sum(valores)
    return f"{len(valores)} valores, total {total:.{decimales}f}"


resumen(1.5, 2.25, 3)                # '3 valores, total 6.75'
resumen(1.5, 2.25, 3, decimales=0)   # '3 valores, total 7'
```

### Una trampa clásica: valores por defecto mutables

El valor por defecto se crea **una sola vez**, al definir la función, no en cada llamada. Si es una lista o un diccionario, todas las llamadas comparten el mismo objeto. El tutorial lo destaca como advertencia importante ([The Python Tutorial](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)).

**Listado 1.20.** El error y su corrección · [ver fichero](listados/listado_1_20_defecto_mutable.py)

```python
def anadir_mal(elemento, lista=[]):        # MAL
    lista.append(elemento)
    return lista

anadir_mal(1)    # [1]
anadir_mal(2)    # [1, 2]   ← la lista «por defecto» sobrevive entre llamadas


def anadir(elemento, lista=None):          # BIEN
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista
```

### Cómo se pasan los argumentos

Python no pasa «por valor» ni «por referencia» en el sentido de C++: la función recibe **una referencia al mismo objeto** que tiene quien la llama.

**Listado 1.21.** Modificar frente a reasignar · [ver fichero](listados/listado_1_21_paso_argumentos.py)

```python
def modificar(lista):
    lista.append(99)      # cambia el objeto recibido: quien llama lo ve

def reasignar(lista):
    lista = [0]           # solo mueve la etiqueta local: quien llama no lo ve

datos = [1, 2]
modificar(datos)
print(datos)              # [1, 2, 99]
reasignar(datos)
print(datos)              # [1, 2, 99]
```

> [!NOTE]
> **Desde C++.** Con objetos inmutables (`int`, `float`, `str`, `tuple`) el efecto es como el paso por valor, porque la función no puede modificarlos. Con objetos mutables (`list`, `dict`, `set`) es como pasar un puntero: cuidado con modificar datos que no son tuyos.

### Ámbito de las variables

Python busca un nombre en este orden: local, funciones que la contienen, global del módulo y predefinidos (regla **LEGB**). Una función puede **leer** variables globales, pero si les asigna un valor crea una variable local nueva. Existe la palabra `global` para evitarlo, pero en este módulo no la usaremos: una función debe recibir lo que necesita por parámetro y devolver su resultado.

### Funciones como valores y funciones lambda

Como las funciones son objetos, se pueden pasar como argumento. El caso más habitual es el parámetro `key` de `sorted`, `min` y `max`, que indica **por qué** ordenar o comparar. Para funciones de una sola expresión se usa `lambda`.

**Listado 1.22.** Ordenar con una función clave · [ver fichero](listados/listado_1_22_ordenar_lambda.py)

```python
alumnos = [("Ana", 6.5), ("Luis", 4.0), ("Eva", 9.1)]

ranking = sorted(alumnos, key=lambda a: a[1], reverse=True)
# [('Eva', 9.1), ('Ana', 6.5), ('Luis', 4.0)]

mejor = max(alumnos, key=lambda a: a[1])     # ('Eva', 9.1)
```

Las funciones que reciben o devuelven otras funciones, y los decoradores que se construyen con ellas, se estudian a fondo en la UD2.

### Para practicar

1. Escribe `es_primo(n: int) -> bool` con su docstring y úsala para listar los primos menores que 50.
2. Escribe `normalizar(texto: str, *, mayusculas: bool = False) -> str`, que quite espacios al principio y al final, reduzca los espacios repetidos a uno y, si se pide, pase a mayúsculas. Pista: `split()` sin argumentos y `join`.
3. Amplía `estadisticas` para que devuelva también la mediana. Pista: `sorted(valores)`.
4. (A) Sin ejecutarlo, explica qué imprime la versión incorrecta del listado 1.20 si llamamos `anadir_mal(3, [])` y después `anadir_mal(4)`. Compruébalo después.

## 1.5 Estructuras de datos

Python trae cuatro colecciones integradas que cubren casi todas las necesidades: **listas**, **tuplas**, **diccionarios** y **conjuntos**. Una lista de diccionarios ya es, en la práctica, una tabla de datos; en la UD3 pandas hará lo mismo a gran escala. Referencia: capítulo 5 del tutorial ([The Python Tutorial](https://docs.python.org/3/tutorial/datastructures.html)).

| Estructura | Sintaxis | Ordenada | Mutable | Duplicados | Equivalente en C++ |
| --- | --- | --- | --- | --- | --- |
| Lista `list` | `[1, 2, 2]` | Sí | Sí | Sí | `std::vector` |
| Tupla `tuple` | `(1, 2, 2)` | Sí | No | Sí | `std::tuple`, `std::pair`, un `struct` |
| Diccionario `dict` | `{"a": 1}` | Orden de inserción | Sí | Claves únicas | `std::unordered_map` |
| Conjunto `set` | `{1, 2}` | No | Sí | No | `std::unordered_set` |

A diferencia de C++, una misma colección puede contener objetos de tipos distintos, aunque en la práctica conviene que sean homogéneos.

### Listas

**Listado 1.23.** Operaciones habituales con listas · [ver fichero](listados/listado_1_23_listas.py)

```python
notas = [6.5, 4.0, 9.1]

notas.append(7.25)        # añade al final
notas.insert(0, 5.0)      # inserta en una posición
# [5.0, 6.5, 4.0, 9.1, 7.25]

ultima = notas.pop()      # extrae y devuelve el último: 7.25
notas.remove(4.0)         # elimina la primera aparición de un valor
# [5.0, 6.5, 9.1]

sorted(notas, reverse=True)   # devuelve una lista NUEVA ordenada
notas.sort(reverse=True)      # ordena la lista ORIGINAL y devuelve None

9.1 in notas              # True: pertenencia
len(notas)                # 3
```

Las rebanadas del apartado 1.2 funcionan igual con listas: `notas[:2]`, `notas[-1]`, `notas[::-1]`.

### Asignar no es copiar

Como las variables son etiquetas (apartado 1.2), `b = a` no copia la lista: crea un segundo nombre para el **mismo** objeto.

**Listado 1.24.** Alias, copia y el error de la matriz · [ver fichero](listados/listado_1_24_copias.py)

```python
a = [1, 2, 3]
b = a              # alias: a y b son la misma lista
b.append(4)
print(a)           # [1, 2, 3, 4]

c = a.copy()       # copia independiente (también vale a[:] o list(a))
c.append(5)
print(a)           # [1, 2, 3, 4]

matriz = [[0] * 3] * 2              # MAL: dos referencias a la misma fila
matriz[0][0] = 9                    # [[9, 0, 0], [9, 0, 0]]

matriz = [[0] * 3 for _ in range(2)]    # BIEN: dos filas distintas
matriz[0][0] = 9                        # [[9, 0, 0], [0, 0, 0]]
```

`copy()` hace una copia **superficial**: si la lista contiene otras listas, estas se siguen compartiendo. Para copiar estructuras anidadas completas está `copy.deepcopy()`.

### Tuplas

Una tupla es una secuencia **inmutable**. Se usa para agrupar datos heterogéneos que van juntos, como las coordenadas de un punto o una fila de datos, y como clave de un diccionario, cosa que una lista no puede ser.

**Listado 1.25.** Empaquetado y desempaquetado · [ver fichero](listados/listado_1_25_tuplas.py)

```python
punto = (37.18, -3.60)          # latitud y longitud
lat, lon = punto                # desempaquetado

primero, *resto = [10, 20, 30, 40]
# primero = 10, resto = [20, 30, 40]
```

### Diccionarios

Un diccionario asocia **claves** únicas con **valores**. El acceso por clave es muy rápido, y desde Python 3.7 se garantiza que se conserva el orden de inserción.

**Listado 1.26.** Crear, consultar, modificar y recorrer un diccionario · [ver fichero](listados/listado_1_26_diccionarios.py)

```python
alumno = {"nombre": "Ana", "nota": 6.5, "ciclo": "DAM"}

alumno["nombre"]                   # 'Ana'
alumno["telefono"]                 # KeyError: 'telefono'
alumno.get("email")                # None: no lanza error
alumno.get("email", "sin email")   # valor alternativo

alumno["nota"] = 7.0               # modificar
alumno["email"] = "ana@example.com"    # añadir
del alumno["email"]                # eliminar

"nota" in alumno                   # True: busca entre las CLAVES

for clave, valor in alumno.items():
    print(f"{clave}: {valor}")
```

Un patrón que usarás a menudo es **contar o acumular por clave**:

**Listado 1.27.** Frecuencia de palabras con `dict` y con `Counter` · [ver fichero](listados/listado_1_27_frecuencias.py)

```python
texto = "el perro y el gato y el raton"

frecuencias = {}
for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
# {'el': 3, 'perro': 1, 'y': 2, 'gato': 1, 'raton': 1}

from collections import Counter             # la versión de la biblioteca estándar
Counter(texto.split()).most_common(2)       # [('el', 3), ('y', 2)]
```

### Conjuntos

Un conjunto guarda elementos **sin repetir y sin orden**. Comprobar si un elemento pertenece a él es muy rápido, y admite las operaciones de la teoría de conjuntos.

**Listado 1.28.** Operaciones con conjuntos · [ver fichero](listados/listado_1_28_conjuntos.py)

```python
matriculados = {"Ana", "Luis", "Eva", "Juan"}
aprobados = {"Ana", "Eva", "Marta"}

matriculados & aprobados     # intersección: {'Ana', 'Eva'}
matriculados - aprobados     # diferencia: {'Luis', 'Juan'}
matriculados | aprobados     # unión
matriculados ^ aprobados     # diferencia simétrica: {'Luis', 'Juan', 'Marta'}

sorted(set([3, 1, 3, 2, 1]))   # quitar duplicados: [1, 2, 3]
```

Al imprimir un conjunto, el orden de los elementos puede variar entre ejecuciones.

### Comprensiones

Una **comprensión** construye una colección a partir de otra en una sola expresión: `[expresión for elemento in iterable if condición]`. Es más legible y, normalmente, más rápida que el bucle equivalente con `append`.

**Listado 1.29.** Comprensiones de lista, diccionario y conjunto · [ver fichero](listados/listado_1_29_comprensiones.py)

```python
cuadrados = [n ** 2 for n in range(1, 6)]            # [1, 4, 9, 16, 25]
pares = [n for n in range(20) if n % 2 == 0]         # con filtro

precios = {"teclado": 25.0, "ratón": 12.5, "monitor": 180.0}
con_iva = {p: round(v * 1.21, 2) for p, v in precios.items()}
caros = [p for p, v in precios.items() if v > 20]    # ['teclado', 'monitor']

iniciales = {nombre[0] for nombre in ["Ana", "Alberto", "Eva"]}   # {'A', 'E'}
```

Si una comprensión no cabe en una línea o necesita varias condiciones anidadas, vuelve al bucle `for`: la legibilidad manda.

### Todo junto: una tabla con listas y diccionarios

**Listado 1.30.** Ventas por ciudad con Python puro · [ver fichero](listados/listado_1_30_ventas_por_ciudad.py)

```python
ventas = [
    {"ciudad": "Granada", "producto": "portátil", "unidades": 3, "precio": 899.90},
    {"ciudad": "Málaga", "producto": "ratón", "unidades": 10, "precio": 12.50},
    {"ciudad": "Granada", "producto": "monitor", "unidades": 2, "precio": 180.00},
    {"ciudad": "Sevilla", "producto": "portátil", "unidades": 1, "precio": 899.90},
    {"ciudad": "Málaga", "producto": "monitor", "unidades": 4, "precio": 180.00},
]

# Acumular el importe por ciudad
total_por_ciudad = {}
for v in ventas:
    importe = v["unidades"] * v["precio"]
    total_por_ciudad[v["ciudad"]] = total_por_ciudad.get(v["ciudad"], 0) + importe

# Mostrar de mayor a menor
for ciudad, total in sorted(total_por_ciudad.items(), key=lambda par: par[1], reverse=True):
    print(f"{ciudad:<8} {total:>9.2f} €")

# Granada    3059.70 €
# Sevilla     899.90 €
# Málaga      845.00 €

# La venta de mayor importe
mejor = max(ventas, key=lambda v: v["unidades"] * v["precio"])
```

Fíjate en lo que hemos hecho: agrupar, agregar, ordenar y buscar el máximo. Son exactamente las operaciones que en la UD3 resolverás con una línea de pandas. Hacerlas antes a mano es la mejor forma de entender qué hace pandas por dentro.

### Para practicar

1. A partir de `ventas` (listado 1.30), calcula las unidades vendidas por producto y el importe medio por venta.
2. Con una comprensión, obtén la lista de ciudades distintas ordenada alfabéticamente. Hazlo después con un conjunto. ¿Qué diferencia hay?
3. Dada una lista de tuplas `(alumno, módulo, nota)`, construye un diccionario `{alumno: [notas]}` y, a partir de él, otro con la media de cada alumno.
4. (A) Explica por qué `[[0] * 3] * 2` crea filas compartidas. Dibuja las etiquetas y los objetos.

## 1.6 Ficheros: texto, CSV y JSON

Tres reglas resumen este apartado: abre los ficheros siempre con `with` e indicando `encoding="utf-8"`, construye las rutas con `pathlib`, y lee los CSV con el módulo `csv` en lugar de trocear líneas a mano. Referencia: apartado 7.2 del tutorial ([The Python Tutorial](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)).

### Rutas con `pathlib`

Un objeto `Path` representa una ruta y funciona igual en Windows, macOS y Linux. El operador `/` une partes de la ruta sin preocuparse de si el separador es `\` o `/`.

**Listado 1.31.** Operaciones básicas con `Path` · [ver fichero](listados/listado_1_31_pathlib.py)

```python
from pathlib import Path

ruta = Path("datos") / "ventas.csv"

ruta.name        # 'ventas.csv'
ruta.stem        # 'ventas'
ruta.suffix      # '.csv'
ruta.parent      # Path('datos')
ruta.exists()    # True o False

list(Path("datos").glob("*.csv"))    # todos los CSV de la carpeta
```

Las rutas relativas se resuelven desde la **carpeta de trabajo**, que no siempre es la del script. En VS Code, abre siempre la carpeta raíz del proyecto (`python-ia`) y ejecuta desde ella.

### Ficheros de texto

| Modo | Significado |
| --- | --- |
| `"r"` | Leer (por defecto). Error si el fichero no existe |
| `"w"` | Escribir. Crea el fichero o **borra** su contenido si ya existía |
| `"a"` | Añadir al final sin borrar lo anterior |
| `"x"` | Crear. Error si el fichero ya existe |
| `"b"` | Se combina con los anteriores para ficheros binarios: `"rb"`, `"wb"` |

**Listado 1.32.** Escribir y leer un fichero de texto · [ver fichero](listados/listado_1_32_fichero_texto.py)

```python
from pathlib import Path

ruta = Path("datos") / "registro.txt"

with ruta.open("w", encoding="utf-8") as f:
    f.write("inicio del proceso\n")
    f.write("ERROR: fichero no encontrado\n")
    f.write("fin del proceso\n")

with ruta.open(encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):    # línea a línea
        if linea.startswith("ERROR"):
            print(f"Línea {numero}: {linea.rstrip()}")

# Línea 2: ERROR: fichero no encontrado
```

- `with` cierra el fichero al salir del bloque, incluso si se produce un error. Es el equivalente de RAII en C++.
- Recorrer el fichero con `for` lee **una línea cada vez**, sin cargarlo entero en memoria. Es la forma correcta de procesar ficheros grandes.
- Para ficheros pequeños, `ruta.read_text(encoding="utf-8")` devuelve todo el contenido en una cadena.
- Indica siempre `encoding="utf-8"`. En Windows, la codificación por defecto puede no ser UTF-8 y los acentos se estropean.

### Ficheros CSV

CSV no es un formato con un estándar único: cada aplicación introduce pequeñas variaciones, como el separador o el entrecomillado. El módulo `csv` resuelve esas diferencias por ti. La documentación recomienda abrir el fichero con `newline=""` y advierte de que todos los valores se leen como texto, sin conversión automática de tipos ([docs.python.org, csv](https://docs.python.org/3/library/csv.html)).

> [!TIP]
> **CSV «a la española».** Excel y LibreOffice en español suelen guardar los CSV con `;` como separador y coma decimal (`899,90`). Además, la opción «CSV UTF-8» de Excel añade al principio una marca invisible (BOM). Si la primera columna aparece con un nombre raro como `'\ufefffecha'`, abre el fichero con `encoding="utf-8-sig"`.

Partimos de este fichero, [`datos/ventas.csv`](listados/datos/ventas.csv), que tiene una fila con un campo vacío:

```csv
fecha;ciudad;producto;unidades;precio
2026-09-01;Granada;portátil;3;899,90
2026-09-01;Málaga;ratón;10;12,50
2026-09-02;Granada;monitor;2;180,00
2026-09-02;Sevilla;portátil;;899,90
2026-09-03;Málaga;monitor;4;1.180,00
```

**Listado 1.33.** `resumen_ventas.py`: de CSV a JSON · [ver fichero](listados/listado_1_33_resumen_ventas.py)

```python
import csv
import json
from pathlib import Path

CARPETA_DATOS = Path("datos")
entrada = CARPETA_DATOS / "ventas.csv"
salida = CARPETA_DATOS / "resumen.json"


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


total_por_ciudad = {}
descartadas = 0

with entrada.open(encoding="utf-8", newline="") as f:
    lector = csv.DictReader(f, delimiter=";")
    for fila in lector:                      # cada fila es un dict
        if not fila["unidades"]:             # campo vacío: no se puede calcular
            descartadas += 1
            continue
        importe = int(fila["unidades"]) * a_float(fila["precio"])
        ciudad = fila["ciudad"]
        total_por_ciudad[ciudad] = total_por_ciudad.get(ciudad, 0) + importe

resumen = {
    "fichero": entrada.name,
    "filas_descartadas": descartadas,
    "total_por_ciudad": {c: round(t, 2) for c, t in total_por_ciudad.items()},
}

with salida.open("w", encoding="utf-8") as f:
    json.dump(resumen, f, ensure_ascii=False, indent=2)
```

`csv.DictReader` usa la primera fila como cabecera y devuelve cada fila como un diccionario, así que el código accede a los campos por nombre y no por posición. Si mañana alguien reordena las columnas del CSV, el programa sigue funcionando.

> [!WARNING]
> `a_float` solo sirve para números en formato español. Aplicada a `"1180.00"`, quitaría el punto y devolvería 118000. Saber en qué formato llegan los datos es parte del trabajo de limpieza que retomaremos en la UD3.

Para **escribir** un CSV, `csv.DictWriter` hace el camino inverso: recibe los nombres de columna en `fieldnames`, escribe la cabecera con `writeheader()` y cada fila con `writerow(diccionario)`.

### Ficheros JSON

JSON es el formato de intercambio de datos de la web y de casi todas las API. Su correspondencia con Python es directa: los objetos JSON son diccionarios, los arrays son listas, `true`/`false` son `True`/`False` y `null` es `None`.

El resultado del listado 1.33, `datos/resumen.json`:

```json
{
  "fichero": "ventas.csv",
  "filas_descartadas": 1,
  "total_por_ciudad": {
    "Granada": 3059.7,
    "Málaga": 4845.0
  }
}
```

**Listado 1.34.** Leer un JSON y trabajar con él · [ver fichero](listados/listado_1_34_leer_json.py)

```python
import json

with open("datos/resumen.json", encoding="utf-8") as f:
    resumen = json.load(f)                     # dict de Python

ciudad, total = max(resumen["total_por_ciudad"].items(), key=lambda par: par[1])
print(f"Ciudad con más ventas: {ciudad} ({total:.2f} €)")
```

| Función | Hace | Parámetros útiles |
| --- | --- | --- |
| `json.load(f)` | Lee de un fichero abierto | — |
| `json.loads(texto)` | Lee de una cadena | — |
| `json.dump(obj, f)` | Escribe en un fichero abierto | `indent=2` (legible), `ensure_ascii=False` (conserva acentos) |
| `json.dumps(obj)` | Devuelve una cadena JSON | Los mismos |

### Para practicar

1. Ejecuta el listado 1.33 desde la carpeta `listados/` y comprueba el JSON generado. ¿Por qué no aparece Sevilla?
2. Amplía el programa para que genere también `datos/informe.csv` con las columnas `ciudad` y `total`, ordenado de mayor a menor, usando `csv.DictWriter` con `;` como separador.
3. Escribe una función `contar_lineas(ruta: Path, texto: str) -> int` que devuelva cuántas líneas de un fichero contienen un texto dado, sin cargar el fichero entero en memoria.
4. (A) Abre `ventas.csv` con Excel o LibreOffice y guárdalo como «CSV UTF-8». Léelo con `encoding="utf-8"` y después con `"utf-8-sig"`, e imprime las claves de la primera fila. Explica la diferencia.

## 1.7 Errores, excepciones y depuración

Como Python no compila de antemano, la mayoría de los errores aparecen al ejecutar, en forma de **excepciones**. Saber leer un *traceback*, capturar solo las excepciones que puedes tratar y usar el depurador de VS Code es lo que separa perder diez minutos de perder una tarde. Referencia: capítulo 8 del tutorial ([The Python Tutorial](https://docs.python.org/3/tutorial/errors.html)).

### Tres tipos de error

| Tipo | Cuándo aparece | Ejemplo |
| --- | --- | --- |
| Error de sintaxis | Antes de ejecutar nada: Python no entiende el código | Un paréntesis sin cerrar, una sangría incorrecta |
| Excepción | Durante la ejecución, en la línea problemática | Dividir entre cero, una clave que no existe |
| Error lógico | Nunca: el programa termina, pero el resultado es incorrecto | Usar `<` donde iba `<=` |

Los errores lógicos son los más peligrosos, porque no avisan. Se combaten probando con datos cuyo resultado conoces y con el depurador.

### Leer un *traceback*

**Listado 1.35.** Un programa que falla… · [ver fichero](listados/listado_1_35_traceback.py)

```python
def media(valores):
    return sum(valores) / len(valores)

notas = []
print(media(notas))
```

…y el informe de error que produce:

```text
Traceback (most recent call last):
  File "notas.py", line 5, in <module>
    print(media(notas))
          ^^^^^^^^^^^^
  File "notas.py", line 2, in media
    return sum(valores) / len(valores)
           ~~~~~~~~~~~~~^~~~~~~~~~~~~~
ZeroDivisionError: division by zero
```

Se lee **de abajo arriba**. La última línea dice qué pasó (`ZeroDivisionError`) y por qué. Justo encima está la línea exacta, con marcas que señalan la operación culpable. Más arriba aparece la cadena de llamadas que llevó hasta allí.

### Las excepciones más frecuentes

| Excepción | Causa típica | Ejemplo |
| --- | --- | --- |
| `SyntaxError` | Código mal escrito | `print("hola"` → paréntesis sin cerrar |
| `IndentationError` | Sangría incorrecta | Un `if` sin bloque sangrado debajo |
| `NameError` | Nombre no definido o mal escrito | `print(nombre)` antes de asignarlo |
| `TypeError` | Operación con un tipo incompatible | `"20" + 1` |
| `ValueError` | Tipo correcto, valor inválido | `int("3.5")`, `int("")` |
| `KeyError` | Clave inexistente en un diccionario | `d["telefono"]` |
| `IndexError` | Índice fuera de rango | `lista[5]` en una lista de 2 elementos |
| `AttributeError` | El objeto no tiene ese método o atributo | `"abc".push(1)` |
| `ZeroDivisionError` | División entre cero | `media([])` |
| `FileNotFoundError` | El fichero no existe | `open("no_existe.txt")` |

### Capturar excepciones: `try`, `except`, `else`, `finally`

**Listado 1.36.** Lectura robusta de `ventas.csv` (mejora del listado 1.33) · [ver fichero](listados/listado_1_36_lectura_robusta.py)

```python
import csv
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


def leer_ventas(ruta: Path) -> list[dict]:
    """Devuelve las filas válidas del CSV de ventas con los tipos convertidos."""
    validas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        for num_linea, fila in enumerate(lector, start=2):   # la línea 1 es la cabecera
            try:
                fila["unidades"] = int(fila["unidades"])
                fila["precio"] = a_float(fila["precio"])
            except ValueError as e:
                logging.warning("Línea %d descartada: %s", num_linea, e)
                continue
            validas.append(fila)
    return validas


try:
    ventas = leer_ventas(Path("datos") / "ventas.csv")
except FileNotFoundError as e:
    logging.error("No se encuentra el fichero %s", e.filename)
else:
    logging.info("%d ventas válidas", len(ventas))
finally:
    logging.info("Proceso terminado")
```

Salida con el fichero del apartado 1.6:

```text
WARNING: Línea 5 descartada: invalid literal for int() with base 10: ''
INFO: 4 ventas válidas
INFO: Proceso terminado
```

| Bloque | Se ejecuta… |
| --- | --- |
| `try` | Siempre: contiene el código que puede fallar |
| `except Tipo as e` | Solo si se produce una excepción de ese tipo; `e` contiene los detalles |
| `else` | Solo si el `try` terminó **sin** excepciones |
| `finally` | Siempre, haya o no excepción. Se usa para tareas de limpieza |

> [!IMPORTANT]
> **Regla de oro.** Captura solo las excepciones que sabes tratar y hazlo lo más cerca posible de donde se producen. Un `except:` sin tipo, o un `except Exception:` que no hace nada, esconde errores reales. Es el equivalente de un `catch (...) {}` vacío en C++.

### Lanzar excepciones: `raise`

Cuando una función recibe datos con los que no puede trabajar, lo correcto es **lanzar** una excepción con un mensaje claro, no devolver un valor «raro» como `-1`.

**Listado 1.37.** Validar con `raise` · [ver fichero](listados/listado_1_37_validar_nota.py)

```python
def validar_nota(nota: float) -> float:
    """Devuelve la nota si está entre 0 y 10; si no, lanza ValueError."""
    if not 0 <= nota <= 10:
        raise ValueError(f"Nota fuera de rango: {nota}")
    return nota
```

### Pedir perdón en lugar de permiso

En C++ es habitual comprobarlo todo antes de actuar (*Look Before You Leap*, LBYL). En Python es idiomático intentarlo y tratar el fallo si ocurre (*Easier to Ask Forgiveness than Permission*, EAFP):

```python
# LBYL: comprobar antes de actuar
if texto.isdigit():
    edad = int(texto)
else:
    edad = None
```

```python
# EAFP: intentarlo y capturar el fallo
try:
    edad = int(texto)
except ValueError:
    edad = None
```

La versión EAFP es más robusta: `isdigit()` rechaza `"-5"`, y `int()` sí sabe interpretarlo.

### `assert` y `logging`

- `assert condición, "mensaje"` detiene el programa si la condición es falsa. Sirve para comprobar supuestos internos mientras desarrollas, como `assert len(ventas) > 0`. No lo uses para validar datos del usuario: las aserciones se pueden desactivar al ejecutar.
- `logging` sustituye a los `print` de depuración. Cada mensaje tiene un nivel (`DEBUG`, `INFO`, `WARNING`, `ERROR`) y se puede silenciar o redirigir a un fichero sin tocar el código ([The Python Tutorial](https://docs.python.org/3/tutorial/stdlib2.html#logging)).

### El depurador de VS Code

1. Haz clic a la izquierda del número de línea para poner un **punto de interrupción** (*breakpoint*). Aparece un punto rojo.
2. Pulsa `F5` y elige *Python Debugger: Current File*. El programa se detiene al llegar a esa línea.
3. Avanza con `F10` (paso a paso, sin entrar en funciones) o `F11` (entrando en ellas). `F5` continúa hasta el siguiente punto.
4. En el panel **Variables** ves el valor de todo en ese instante. En **Watch** puedes seguir expresiones, y la **consola de depuración** permite ejecutar código en ese contexto.
5. Un clic derecho sobre el punto rojo permite añadir una **condición**, por ejemplo `num_linea == 5`, para detenerte solo en el caso que falla.

En los notebooks, cada celda tiene una opción para ejecutarla línea a línea o depurarla con estas mismas herramientas.

### Para practicar

1. Provoca a propósito cada excepción de la tabla en el intérprete. Anota la última línea del *traceback* de cada una.
2. Reescribe el listado 1.14 con `try`/`except ValueError` en lugar de `isdigit()`.
3. Pon un punto de interrupción condicional dentro del bucle de `leer_ventas` que se detenga en la línea 5 del CSV. Inspecciona `fila` en el panel de variables.
4. (A) Amplía `leer_ventas` para que descarte también las filas con precio o unidades menores o iguales que cero. Usa `raise ValueError` dentro del `try` y registra el motivo en el aviso.

## 1.8 Módulos y paquetes

Un **módulo** es un fichero `.py`; un **paquete** es una carpeta de módulos. Organizar el código así permite reutilizarlo desde scripts, notebooks y, al final del curso, desde la aplicación Streamlit. Referencia: capítulo 6 del tutorial ([The Python Tutorial](https://docs.python.org/3/tutorial/modules.html)).

### Importar

**Listado 1.38.** Las tres formas de `import` · [ver fichero](listados/listado_1_38_imports.py)

```python
import statistics                      # 1. el módulo completo
statistics.mean([4.5, 7.0, 9.25])

from pathlib import Path               # 2. un nombre concreto
ruta = Path("datos")

import datetime as dt                  # 3. con un alias
hoy = dt.date.today()
```

Evita `from modulo import *`: llena tu espacio de nombres de nombres desconocidos y hace imposible saber de dónde viene cada función.

> [!NOTE]
> **Desde C++.** `import` se parece a `#include`, pero no copia texto: carga el módulo **una sola vez**, lo ejecuta y te da acceso a sus nombres a través de un espacio de nombres propio, como un `namespace`. No hay ficheros de cabecera ni enlazado.

### Tu primer módulo y `__name__`

Al importar un módulo, Python ejecuta todo su código. Para que un fichero funcione a la vez como módulo importable y como script, se usa la comprobación `if __name__ == "__main__":`. Ese bloque solo se ejecuta cuando el fichero se lanza directamente ([The Python Tutorial](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)).

**Listado 1.39.** `utilidades.py`: módulo con autoprueba · [ver fichero](listados/utilidades.py)

```python
"""Funciones de texto reutilizables."""


def normalizar(texto: str) -> str:
    """Quita espacios sobrantes y pasa a minúsculas."""
    return " ".join(texto.split()).lower()


if __name__ == "__main__":
    # Solo se ejecuta con: python utilidades.py
    assert normalizar("  Hola   MUNDO ") == "hola mundo"
    print("Pruebas superadas")
```

Desde otro fichero de la misma carpeta basta con `import utilidades` y `utilidades.normalizar("...")`; las pruebas no se ejecutan.

### Paquetes: el código del proyecto en `src/`

Vamos a convertir el código de los apartados 1.6 y 1.7 en un paquete llamado `ventas`, dentro de la carpeta `src/` que preparamos en el apartado 1.1. Tienes el proyecto completo en la carpeta [`proyecto/`](proyecto/).

```text
python-ia/
├── pyproject.toml
├── datos/
│   └── ventas.csv
├── notebooks/
└── src/
    └── ventas/
        ├── __init__.py      convierte la carpeta en paquete
        ├── __main__.py      se ejecuta con: python -m ventas
        ├── lectura.py       a_float, leer_ventas
        └── informes.py      total_por_ciudad, guardar_json
```

**Listado 1.40.** `src/ventas/lectura.py` · [ver fichero](proyecto/src/ventas/lectura.py)

```python
"""Lectura y conversión de los datos de ventas."""

import csv
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def a_float(texto: str) -> float:
    """Convierte un número en formato español ('1.234,56') en float."""
    return float(texto.replace(".", "").replace(",", "."))


def leer_ventas(ruta: Path) -> list[dict]:
    """Devuelve las filas válidas del CSV de ventas con los tipos convertidos."""
    validas = []
    with ruta.open(encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f, delimiter=";")
        for num_linea, fila in enumerate(lector, start=2):
            try:
                fila["unidades"] = int(fila["unidades"])
                fila["precio"] = a_float(fila["precio"])
            except ValueError as e:
                logger.warning("Línea %d descartada: %s", num_linea, e)
                continue
            validas.append(fila)
    return validas
```

Fíjate en un cambio respecto al listado 1.36: el módulo ya no llama a `logging.basicConfig`, sino que crea su propio `logger`. Una biblioteca informa de lo que pasa; decidir cómo se muestran los mensajes le corresponde al programa que la usa.

**Listado 1.41.** `src/ventas/informes.py` · [ver fichero](proyecto/src/ventas/informes.py)

```python
"""Cálculos y exportación de informes a partir de las ventas."""

import json
from pathlib import Path


def total_por_ciudad(ventas: list[dict]) -> dict[str, float]:
    """Importe total por ciudad, ordenado de mayor a menor."""
    totales = {}
    for v in ventas:
        totales[v["ciudad"]] = totales.get(v["ciudad"], 0) + v["unidades"] * v["precio"]
    ordenados = sorted(totales.items(), key=lambda par: par[1], reverse=True)
    return {ciudad: round(total, 2) for ciudad, total in ordenados}


def guardar_json(datos: dict, ruta: Path) -> None:
    """Guarda un diccionario en un fichero JSON legible."""
    with ruta.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
```

**Listado 1.42.** `src/ventas/__init__.py`: la interfaz pública del paquete · [ver fichero](proyecto/src/ventas/__init__.py)

```python
"""Utilidades para leer y resumir el fichero de ventas del curso."""

from .lectura import leer_ventas
from .informes import total_por_ciudad, guardar_json

__all__ = ["leer_ventas", "total_por_ciudad", "guardar_json"]
```

Los puntos de `.lectura` indican una **importación relativa**: el módulo `lectura` de este mismo paquete. Gracias a este fichero, quien use el paquete puede escribir `from ventas import leer_ventas` sin conocer su organización interna.

**Listado 1.43.** `src/ventas/__main__.py`: el programa principal · [ver fichero](proyecto/src/ventas/__main__.py)

```python
"""Punto de entrada: python -m ventas"""

import logging
from pathlib import Path

from ventas import guardar_json, leer_ventas, total_por_ciudad


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    ventas = leer_ventas(Path("datos") / "ventas.csv")
    totales = total_por_ciudad(ventas)
    guardar_json({"total_por_ciudad": totales}, Path("datos") / "resumen.json")
    for ciudad, total in totales.items():
        print(f"{ciudad:<8} {total:>9.2f} €")


if __name__ == "__main__":
    main()
```

### Hacer el paquete importable desde cualquier sitio

Para que `import ventas` funcione desde la raíz, desde `notebooks/` o desde cualquier otra carpeta, instalamos el propio proyecto en el entorno virtual en **modo editable**. Solo hace falta un `pyproject.toml` mínimo en la raíz:

**Listado 1.44.** `pyproject.toml` · [ver fichero](proyecto/pyproject.toml)

```toml
[project]
name = "python-ia"
version = "0.1.0"
requires-python = ">=3.12"

[build-system]
requires = ["setuptools>=64"]
build-backend = "setuptools.build_meta"
```

**Listado 1.45.** Instalar y ejecutar (con el entorno activado, desde la carpeta del proyecto)

```bash
python -m pip install -e .      # -e: editable; los cambios en src/ se ven al instante
python -m ventas                # ejecuta src/ventas/__main__.py
```

Salida:

```text
WARNING: Línea 5 descartada: invalid literal for int() with base 10: ''
Málaga     4845.00 €
Granada    3059.70 €
```

Y en cualquier notebook del proyecto:

```python
from pathlib import Path
from ventas import leer_ventas

ventas = leer_ventas(Path("../datos/ventas.csv"))
```

La instalación genera una carpeta `src/python_ia.egg-info`: añádela al `.gitignore` del proyecto.

### La biblioteca estándar: pilas incluidas

Antes de instalar nada, comprueba si la biblioteca estándar ya lo resuelve.

| Módulo | Para qué | Ejemplo |
| --- | --- | --- |
| `pathlib` | Rutas y ficheros | `Path("datos").glob("*.csv")` |
| `csv`, `json` | Formatos de datos | Apartado 1.6 |
| `datetime` | Fechas y horas | `dt.date.fromisoformat("2026-09-21")` |
| `math`, `statistics` | Cálculo y estadística básica | `statistics.median(notas)` |
| `random` | Números aleatorios | `random.choice(ciudades)` |
| `collections` | Colecciones especializadas | `Counter`, `defaultdict` |
| `logging` | Registro de mensajes | Apartado 1.7 |
| `re` | Expresiones regulares | Validar códigos postales |

### Paquetes externos y `requirements.txt`

Lo que no está en la biblioteca estándar se instala desde PyPI con `pip`. Para que otra persona, o tú mismo en otro ordenador, pueda reproducir el entorno, se guarda la lista de paquetes en `requirements.txt`. La documentación de `venv` recomienda precisamente esto: un entorno no se copia, se recrea a partir de ese fichero ([docs.python.org, venv](https://docs.python.org/3/library/venv.html)).

**Listado 1.46.** Guardar y restaurar las dependencias

```bash
# Guardar (excluyendo el propio proyecto, instalado en modo editable)
python -m pip freeze --exclude-editable > requirements.txt

# Recrear el entorno en otro equipo
python -m venv .venv
# (activar el entorno)
python -m pip install -r requirements.txt
python -m pip install -e .
```

`requirements.txt` sí se sube a Git; `.venv` no.

### Para practicar

1. Crea `utilidades.py` (listado 1.39), ejecútalo directamente y después impórtalo desde otro script. Comprueba que las pruebas solo se ejecutan en el primer caso.
2. Monta el paquete `ventas` en tu proyecto, instálalo en modo editable y ejecuta `python -m ventas`.
3. Añade al paquete un módulo `validacion.py` con `validar_nota` (listado 1.37) y exporta la función en `__init__.py`. Úsala desde un notebook.
4. (A) Genera tu `requirements.txt`, borra la carpeta `.venv` y reconstruye el entorno desde cero siguiendo el listado 1.46.

## Práctica de la unidad · Hito 0 del proyecto integrador

La práctica de la UD1 es el primer hito del proyecto integrador. Cada alumno o equipo elige el conjunto de datos con el que trabajará todo el curso y construye, **solo con la biblioteca estándar**, un explorador que lo describe. Ese mismo conjunto de datos se limpiará en la UD3, se guardará en una base de datos en la UD4, se modelará en la UD6 y se desplegará en la UD7.

### 1. Elegir el conjunto de datos

Requisitos:

- Datos reales y públicos, con licencia que permita su uso. Ningún dato personal: la aplicación final se publicará en internet.
- Formato CSV o JSON, con al menos 1.000 filas y 6 columnas.
- Columnas numéricas y categóricas, y al menos una que se pueda predecir: un número (regresión) o una categoría (clasificación).

Portales donde buscar: [datos.gob.es](https://datos.gob.es) (catálogo de datos abiertos de las administraciones españolas), [UCI Machine Learning Repository](https://archive.ics.uci.edu) y [Kaggle Datasets](https://www.kaggle.com/datasets).

Documenta la elección en `docs/ficha_dataset.md` con: fuente y enlace, licencia, fecha de descarga, descripción de cada columna, la pregunta que quieres responder y la variable que intentarás predecir.

### 2. Construir el explorador

Crea un paquete `src/explorador/` que, ejecutado con `python -m explorador`, lea tu fichero de `datos/` y genere `datos/informe_inicial.json` con:

- Número de filas y de columnas.
- Para cada columna: número y porcentaje de valores vacíos y tipo inferido (entero, decimal o texto).
- Para las columnas numéricas: mínimo, máximo y media.
- Para las columnas de texto: número de valores distintos y los 5 más frecuentes.
- Número de filas que no se han podido procesar y el motivo, registrado con `logging`.

Estructura mínima sugerida:

```text
src/explorador/
├── __init__.py
├── __main__.py       lee argumentos, llama a las funciones y guarda el informe
├── lectura.py        leer el CSV o JSON con csv/json y pathlib
├── tipos.py          inferir el tipo de una columna
└── estadisticas.py   vacíos, mínimos, máximos, medias y frecuencias
```

No se permite pandas en este hito: el objetivo es que entiendas qué hace una biblioteca de datos por dentro antes de usarla.

### 3. Entregables

- Repositorio con `pyproject.toml`, `requirements.txt`, `docs/ficha_dataset.md`, el paquete `src/explorador/` y un `README.md` que explique cómo instalar y ejecutar.
- El fichero `datos/informe_inicial.json` generado.
- Defensa oral breve (5 minutos): explicar una función del código elegida por el profesor.

Fecha de entrega: a fijar por el profesor. Se propone antes del inicio de la UD3 (20/10/2026).

### 4. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 1a | Funciones con docstring y anotaciones de tipo; control de flujo claro, sin código repetido |
| 1b | Estructura de datos adecuada a cada tarea: diccionarios para contar, conjuntos para valores distintos, listas para las filas |
| 1c | Lectura con `csv` o `json` y `pathlib`, codificación explícita, escritura correcta del informe JSON |
| 1d | Tratamiento de fichero inexistente y de valores no convertibles con excepciones concretas; uso de `logging` |
| 1e | Paquete organizado en módulos, ejecutable con `python -m`, instalable en modo editable y con `requirements.txt` |

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 1.1 Ecosistema | Python 3.14, VS Code con Python y Jupyter, y un entorno virtual `.venv` por proyecto. Instala siempre con `python -m pip` |
| 1.2 Tipos | Las variables son etiquetas; el tipo lo tiene el objeto. `/` siempre da `float`, los `float` no son exactos y las cadenas son inmutables |
| 1.3 Control de flujo | `for` recorre elementos; usa `enumerate` y `zip` en lugar de índices. `match` reconoce estructuras, no solo valores |
| 1.4 Funciones | Docstring y anotaciones siempre. Parámetros por nombre para las opciones. Nunca un valor por defecto mutable |
| 1.5 Estructuras de datos | Lista, tupla, diccionario y conjunto, cada uno para lo suyo. Asignar no copia. Las comprensiones sustituyen a los bucles sencillos |
| 1.6 Ficheros | `with`, `encoding="utf-8"` y `pathlib` siempre. CSV con el módulo `csv`, JSON con `json` |
| 1.7 Errores | El *traceback* se lee de abajo arriba. Captura solo lo que sabes tratar, lanza excepciones con mensajes claros y depura con puntos de interrupción |
| 1.8 Módulos y paquetes | Código reutilizable en `src/`, instalado en modo editable. `if __name__ == "__main__":` separa el módulo del programa. El entorno se recrea con `requirements.txt` |

## Bibliografía de la UD1

Todas las fuentes web se consultaron el 21 de septiembre de 2026.

### Documentación oficial de Python

- Python Software Foundation. (2026). *The Python Tutorial* (versión 3.14). <https://docs.python.org/3/tutorial/index.html>. Capítulos citados: [3. Introducción informal](https://docs.python.org/3/tutorial/introduction.html), [4. Control de flujo y funciones](https://docs.python.org/3/tutorial/controlflow.html), [5. Estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html), [6. Módulos](https://docs.python.org/3/tutorial/modules.html), [7. Entrada y salida](https://docs.python.org/3/tutorial/inputoutput.html), [8. Errores y excepciones](https://docs.python.org/3/tutorial/errors.html), [11. Biblioteca estándar II (logging)](https://docs.python.org/3/tutorial/stdlib2.html#logging) y [15. Aritmética de coma flotante](https://docs.python.org/3/tutorial/floatingpoint.html).
- Python Software Foundation. (2026). *venv — Creation of virtual environments*. <https://docs.python.org/3/library/venv.html>
- Python Software Foundation. (2026). *csv — CSV File Reading and Writing*. <https://docs.python.org/3/library/csv.html>
- Python Software Foundation. (2026). *Status of Python versions*. Python Developer's Guide. <https://devguide.python.org/versions/>
- Python Software Foundation. (2026). *Python install manager 26.3*. <https://www.python.org/downloads/latest/pymanager>
- van Rossum, G., Warsaw, B. y Coghlan, A. (2001, revisada). *PEP 8 – Style Guide for Python Code*. <https://www.python.org/dev/peps/pep-0008/>

### Herramientas

- Microsoft. (2026). *Jupyter Extension for Visual Studio Code*. <https://github.com/microsoft/vscode-jupyter>
- scikit-learn developers. (2025). *scikit-learn 1.8.0* [software]. Zenodo. <https://zenodo.org/records/6968622/latest>

### Lectura complementaria

- Vadillo, J. *Aprende Python desde cero a experto*. Libro gratuito, licencia CC BY-NC-SA 4.0. Descarga: <https://leanpub.com/aprende-python/> · Repositorio: <https://github.com/jvadillo/aprende-python-desde-cero-a-experto>. En español y con Python 3; algunas instrucciones de instalación se refieren a versiones antiguas, así que para instalar sigue el apartado 1.1. Correspondencia con esta unidad:

| Capítulo del libro | Apartado de la UD1 |
| --- | --- |
| 1. Introducción | 1.1 |
| 2. Variables y tipos de datos · 3. Operadores y expresiones | 1.2 |
| 4. Estructuras de control | 1.3 |
| 7. Funciones | 1.4 |
| 5. Listas y tuplas · 6. Diccionarios | 1.5 |
| 8. Excepciones | 1.7 |
| 11. Módulos y paquetes | 1.8 |

- González Duque, R. *Python para todos*. Licencia CC BY 2.5 España. <http://mundogeek.net/tutorial-python/>. Útil para repasar conceptos, pero escrito para Python 2: sustituye `raw_input()` por `input()` y usa `print()` con paréntesis.

### Fuentes de datos para el proyecto

- Gobierno de España. *datos.gob.es*, catálogo nacional de datos abiertos. <https://datos.gob.es>
- University of California, Irvine. *UCI Machine Learning Repository*. <https://archive.ics.uci.edu>
- Kaggle. *Datasets*. <https://www.kaggle.com/datasets>
