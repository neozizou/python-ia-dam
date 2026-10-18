# Python aplicado a la Inteligencia Artificial

Módulo optativo de **2.º de Desarrollo de Aplicaciones Multiplataforma (DAM)** · Curso 2026-2027

📖 **Sitio web de los apuntes: <https://neozizou.github.io/python-ia-dam/>**

Materiales del módulo: apuntes de cada unidad, listados de código ejecutables y el conjunto de datos común con el que se trabaja todo el curso. El módulo se imparte del 16/09/2026 al 16/02/2027, con 3 horas semanales (53 horas lectivas según el calendario escolar de Granada).

El conjunto de datos es [`datos-comunes/jugadores.csv`](datos-comunes/README.md): las valoraciones de los jugadores de FIFA 15 a FIFA 20 (100.995 filas, 36.559 jugadores, 37 columnas, licencia CC0). Todos los ejemplos de los apuntes y todos los hitos del proyecto salen de ese mismo fichero.

## Unidades didácticas

| UD | Contenido | Horas | Fechas aprox. | Estado |
| --- | --- | --- | --- | --- |
| [UD1](ud1-python/UD1-python-para-quien-ya-programa.md) | Python para quien ya programa | 7 | 21/09 – 05/10 | Disponible |
| [UD2](ud2-poo/UD2-programacion-orientada-a-objetos.md) | Programación orientada a objetos en Python | 4 | 05/10 – 19/10 | Disponible |
| [UD3](ud3-datos/UD3-analisis-de-datos.md) | Análisis de datos con Python y primer despliegue con Streamlit | 10 | 20/10 – 16/11 | Disponible |
| [UD4](ud4-bd/UD4-sql-y-nosql.md) | SQL y NoSQL desde Python | 4 | 17/11 – 24/11 | Disponible |
| [UD5](ud5-bigdata/UD5-big-data.md) | Big Data | 5 | 30/11 – 14/12 | Disponible |
| [UD6](ud6-ml/UD6-machine-learning.md) | Machine Learning con scikit-learn | 10 | 15/12 – 19/01 | Disponible |
| [UD7](ud7-proyecto/UD7-proyecto-y-despliegue.md) | Proyecto integrador, despliegue y evaluación | 9 | 25/01 – 16/02 | Disponible |

## Resultados de aprendizaje

1. Implementa programas básicos en Python aplicados a la manipulación de datos.
2. Utiliza herramientas de análisis y procesamiento de datos con Python.
3. Aplica conceptos básicos de Machine Learning en problemas reales.
4. Comprende los principios del Big Data y su aplicación práctica en el análisis de datos.

## Cómo usar este repositorio

Necesitas **Python 3.14** y **VS Code** con las extensiones Python y Jupyter. La UD1 explica paso a paso cómo instalarlos.

```bash
git clone https://github.com/neozizou/python-ia-dam.git
cd python-ia-dam
python -m venv .venv
# Windows (PowerShell):   .venv\Scripts\Activate.ps1
# macOS / Linux:          source .venv/bin/activate
```

Cada unidad tiene su propia carpeta con la misma estructura:

```text
datos-comunes/     el fichero de jugadores del curso y su página de referencia
udN-tema/
├── UDN-tema.md    apuntes de la unidad
├── README.md      portada de la carpeta, con los enlaces
├── figuras/       las figuras de los apuntes, en SVG
├── listados/      los listados de los apuntes como ficheros .py ejecutables
└── proyecto/      código de ejemplo completo, cuando la unidad lo necesita
```

Los listados se ejecutan desde su carpeta `listados/`. Los que leen el fichero de jugadores lo localizan solos a partir de la raíz del repositorio, así que no hay que copiarlo a ningún sitio.

## Proyecto integrador

Todo el alumnado trabaja sobre el mismo fichero de jugadores, de principio a fin. Cada unidad termina en un hito que añade una capa al mismo proyecto, y como el punto de partida es idéntico para todos, cada alumno puede comprobar solo si sus cifras cuadran con las que dan los apuntes:

| Hito | Unidad | Qué se hace con el conjunto de datos |
| --- | --- | --- |
| 0 | UD1 | Describirlo y explorarlo con Python puro, sin bibliotecas |
| 1 | UD2 | Convertir el explorador en un paquete instalable y probado |
| 2 | UD3 | Limpiarlo, explorarlo y publicar un primer panel con Streamlit |
| 3 | UD4 | Guardarlo en una base de datos y consultarlo |
| 4 | UD5 | Tratarlo como problema de escala |
| 5 | UD6 | Entrenar, evaluar y ajustar un modelo |
| 6 | UD7 | Desplegar la aplicación con el modelo y defenderla |

Cada hito trae en los apuntes su **esquema de la ruta** (de qué se parte, qué produce cada paso y qué se entrega) y una **hoja de autoevaluación** con las cifras exactas que tienen que salir.

## El sitio web

Los mismos apuntes se publican como sitio web en <https://neozizou.github.io/python-ia-dam/>, con tres ayudas para estudiar:

- **Barra de búsqueda arriba**, que busca a la vez en las siete unidades y lleva al apartado exacto.
- **Índice fijo a la derecha**, titulado «En esta unidad», que colorea el apartado que se está leyendo.
- **Enlaces a la unidad anterior y a la siguiente** al final de cada unidad.

Se construye solo: cada vez que cambia un fichero `.md`, el flujo de trabajo [`publicar-sitio.yml`](.github/workflows/publicar-sitio.yml) prepara la carpeta `docs/` con [`tools/preparar_docs.py`](tools/preparar_docs.py), genera el sitio con MkDocs Material y lo despliega. Las carpetas `docs/` y `site/` no se suben al repositorio: son resultado de la construcción.

Para activarlo la primera vez: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

Para verlo en local:

```bash
pip install -r tools/requirements-sitio.txt
python tools/preparar_docs.py
mkdocs serve          # http://127.0.0.1:8000
```
