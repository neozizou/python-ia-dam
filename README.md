# Python aplicado a la Inteligencia Artificial

Módulo optativo de **2.º de Desarrollo de Aplicaciones Multiplataforma (DAM)** · Curso 2026-2027

Apuntes, listados de código ejecutables y el conjunto de datos con el que se trabaja todo el curso. El módulo se imparte del 16/09/2026 al 16/02/2027, tres horas semanales, 53 horas lectivas.

## Un solo conjunto de datos, de principio a fin

Todo el módulo trabaja sobre el mismo fichero: [`datos-comunes/jugadores.csv`](datos-comunes/README.md), las valoraciones de los jugadores de FIFA 15 a FIFA 20. Son 100.995 filas, 36.559 jugadores y 37 columnas, con licencia CC0.

No es una decisión estética. Como todos partimos del mismo sitio, los apuntes pueden decirte **las cifras exactas que te tienen que salir** en cada paso, y así sabes solo si vas bien sin esperar a que nadie te corrija. Y como el fichero es el mismo para toda la clase, podéis compararos y ayudaros sin que cada uno esté resolviendo un problema distinto.

El fichero tiene sus trampas, y están contadas en su [página de referencia](datos-comunes/README.md): columnas de dinero vacías en la primera edición, ceros que en realidad son ausencias y una columna con los datos sucios. Lidiar con eso es parte del trabajo.

## Unidades didácticas

| UD | Contenido | Horas | Fechas aprox. | Estado |
| --- | --- | --- | --- | --- |
| [UD1](ud1-python/UD1-python-para-quien-ya-programa.md) | Python para quien ya programa | 7 | 21/09 – 05/10 | Disponible |
| [UD2](ud2-poo/UD2-programacion-orientada-a-objetos.md) | Programación orientada a objetos en Python | 4 | 05/10 – 19/10 | Disponible |
| [UD3](ud3-datos/UD3-analisis-de-datos.md) | Análisis de datos con Python y primer despliegue con Streamlit | 10 | 20/10 – 16/11 | Disponible |
| UD4 | SQL y NoSQL desde Python | 4 | 17/11 – 24/11 | Por actualizar |
| UD5 | Big Data | 5 | 30/11 – 14/12 | Por actualizar |
| UD6 | Machine Learning con scikit-learn | 10 | 15/12 – 19/01 | Por actualizar |
| UD7 | Proyecto integrador, despliegue y evaluación | 9 | 25/01 – 16/02 | Por actualizar |

Las cuatro últimas unidades se están reescribiendo sobre el conjunto de datos del curso. Hasta que estén listas no se enlazan desde aquí, para que nadie estudie por un material que va a cambiar.

## El proyecto integrador

Cada unidad termina en un **hito** que añade una capa al mismo proyecto. Al final del curso no tienes siete ejercicios sueltos: tienes una aplicación que lee un fichero de datos reales, los limpia, los explora, los guarda, entrena un modelo con ellos y está publicada en internet.

| Hito | Unidad | Qué se hace con el conjunto de datos |
| --- | --- | --- |
| 0 | UD1 | Describirlo y explorarlo con Python puro, sin bibliotecas |
| 1 | UD2 | Convertir el explorador en un paquete instalable y probado |
| 2 | UD3 | Limpiarlo, explorarlo y publicar un primer panel con Streamlit |
| 3 | UD4 | Guardarlo en una base de datos y consultarlo |
| 4 | UD5 | Tratarlo como problema de escala |
| 5 | UD6 | Entrenar, evaluar y ajustar un modelo |
| 6 | UD7 | Desplegar la aplicación con el modelo y defenderla |

Cada hito viene en los apuntes con dos cosas que no te puedes saltar: un **esquema de la ruta**, que dice de qué se parte, qué produce cada paso y qué hay que entregar, y una **hoja de autoevaluación** con las cifras que te tienen que salir.

## Cómo se evalúa

- **Autoevaluación de cada hito.** Es formativa: no pone nota, sirve para que sepas si vas bien y para que detectes pronto lo que no cuadra. Son las cifras de la hoja de autoevaluación y tres o cuatro preguntas sobre lo que acabas de hacer.
- **Día en la Oficina.** Una sesión de trabajo sin ayuda de IA, con un encargo acotado y el ordenador delante. Es donde se ve lo que de verdad sabes hacer.
- **Defensa oral.** Explicar tus decisiones: por qué limpiaste así, por qué ese modelo, qué significa el resultado. Un proyecto que no sabes defender no cuenta como tuyo.

## Resultados de aprendizaje

1. Implementa programas básicos en Python aplicados a la manipulación de datos.
2. Utiliza herramientas de análisis y procesamiento de datos con Python.
3. Aplica conceptos básicos de Machine Learning en problemas reales.
4. Comprende los principios del Big Data y su aplicación práctica en el análisis de datos.

## Qué necesitas para empezar

**Python 3.14** y **VS Code** con las extensiones Python y Jupyter. La UD1 explica paso a paso cómo instalarlo todo, desde cero y sin dar nada por sabido.

```bash
git clone https://github.com/neozizou/python-ia-dam.git
cd python-ia-dam
python -m venv .venv
# Windows (PowerShell):   .venv\Scripts\Activate.ps1
# macOS / Linux:          source .venv/bin/activate
```

Cada unidad tiene su carpeta, siempre con la misma estructura:

```text
datos-comunes/     el fichero de jugadores del curso y su página de referencia
udN-tema/
├── UDN-tema.md    apuntes de la unidad
├── README.md      portada de la carpeta, con los enlaces
├── figuras/       las figuras de los apuntes, en SVG
├── listados/      los listados de los apuntes como ficheros .py ejecutables
└── proyecto/      código de ejemplo completo, cuando la unidad lo necesita
```

Los listados se ejecutan **desde su carpeta `listados/`**, con el entorno virtual activado. Los que leen el fichero de jugadores lo localizan solos a partir de la raíz del repositorio, así que no hay que copiarlo a ningún sitio ni cambiar ninguna ruta.

## El sitio web

Los mismos apuntes se leen como sitio web en <https://neozizou.github.io/python-ia-dam/>, con tres ayudas para estudiar:

- **Barra de búsqueda arriba**, que busca a la vez en todas las unidades y lleva al apartado exacto.
- **Índice fijo a la derecha**, titulado «En esta unidad», que colorea el apartado que se está leyendo.
- **Enlaces a la unidad anterior y a la siguiente** al final de cada unidad.

Se construye solo: cada vez que cambia un fichero `.md`, el flujo de trabajo [`publicar-sitio.yml`](.github/workflows/publicar-sitio.yml) prepara la carpeta `docs/` con [`tools/preparar_docs.py`](tools/preparar_docs.py), genera el sitio con MkDocs Material y lo despliega. Las carpetas `docs/` y `site/` no se suben al repositorio: son resultado de la construcción.

Para verlo en local:

```bash
pip install -r tools/requirements-sitio.txt
python tools/preparar_docs.py
mkdocs serve          # http://127.0.0.1:8000
```
