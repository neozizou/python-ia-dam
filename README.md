# Python aplicado a la Inteligencia Artificial

Módulo optativo de **2.º de Desarrollo de Aplicaciones Multiplataforma (DAM)** · Curso 2026-2027

📖 **Sitio web de los apuntes: <https://neozizou.github.io/python-ia-dam/>**

Materiales del módulo: apuntes de cada unidad, listados de código ejecutables y datos de ejemplo. El módulo se imparte del 16/09/2026 al 16/02/2027, con 3 horas semanales (53 horas lectivas según el calendario escolar de Granada).

## Unidades didácticas

| UD | Contenido | Horas | Fechas aprox. | Estado |
| --- | --- | --- | --- | --- |
| [UD1](ud1-python/UD1-python-para-quien-ya-programa.md) | Python para quien ya programa | 7 | 21/09 – 05/10 | Disponible |
| [UD2](ud2-poo/UD2-programacion-orientada-a-objetos.md) | Programación orientada a objetos en Python | 5 | 05/10 – 19/10 | Disponible |
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
udN-tema/
├── UDN-tema.md    apuntes de la unidad
├── README.md      portada de la carpeta, con los enlaces
├── listados/      los listados de los apuntes como ficheros .py ejecutables
└── proyecto/      código de ejemplo completo, cuando la unidad lo necesita
```

Los listados se ejecutan desde su carpeta `listados/`, para que las rutas a `datos/` funcionen.

## Proyecto integrador

A lo largo del curso cada alumno o equipo trabaja siempre con el mismo conjunto de datos real:

| Hito | Unidad | Qué se hace con el conjunto de datos |
| --- | --- | --- |
| 0 | UD1 | Elegirlo y describirlo con Python puro |
| 1 | UD2 | Refactorizar el explorador a objetos, sin cambiar el resultado |
| 2 | UD3 | Limpiarlo, explorarlo y publicar un primer panel con Streamlit |
| 3 | UD4 | Guardarlo en una base de datos y consultarlo |
| 4 | UD5 | Tratarlo como problema de escala |
| 5 | UD6 | Entrenar, evaluar y ajustar un modelo |
| 6 | UD7 | Desplegar la aplicación con el modelo y defenderla |

## El sitio web

Los mismos apuntes se publican como sitio web con buscador en <https://neozizou.github.io/python-ia-dam/>.

Se construye solo: cada vez que cambia un fichero `.md`, el flujo de trabajo [`publicar-sitio.yml`](.github/workflows/publicar-sitio.yml) prepara la carpeta `docs/` con [`tools/preparar_docs.py`](tools/preparar_docs.py), genera el sitio con MkDocs Material y lo despliega. Las carpetas `docs/` y `site/` no se suben al repositorio: son resultado de la construcción.

Para activarlo la primera vez: **Settings → Pages → Build and deployment → Source: GitHub Actions**.

Para verlo en local:

```bash
pip install -r tools/requirements-sitio.txt
python tools/preparar_docs.py
mkdocs serve          # http://127.0.0.1:8000
```
