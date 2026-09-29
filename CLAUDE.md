# CLAUDE.md · Materiales de «Python aplicado a la Inteligencia Artificial»

Este repositorio contiene los apuntes y el código del módulo optativo de 2.º DAM (curso 2026-2027). Lo leen alumnos que vienen de programar en C++ en 1.º. Todo el contenido está en **español de España**.

## Contexto del módulo

- 3 horas semanales (lunes 2 h, martes 1 h), del 16/09/2026 al 16/02/2027: 53 horas lectivas.
- Unidades: UD1 Python (7 h) · UD2 POO (5 h) · UD3 Análisis de datos + Streamlit (10 h) · UD4 SQL y NoSQL (4 h) · UD5 Big Data (5 h) · UD6 Machine Learning (10 h) · UD7 Proyecto, despliegue y evaluación (9 h) · 3 h de colchón.
- Proyecto integrador: cada alumno trabaja todo el curso con un mismo conjunto de datos real (hitos en el README raíz).
- Entorno: Python 3.14, VS Code con las extensiones Python y Jupyter, un entorno virtual `.venv` por proyecto, paquetes en `src/` instalados con `pip install -e .`. Despliegue final en Streamlit Community Cloud.

## Estructura

```text
README.md                 índice del módulo (actualizar la columna «Estado» al publicar una unidad)
udN-tema/
├── UDN-tema.md           apuntes de la unidad (fichero principal)
├── README.md             portada de la carpeta: enlaces a los apuntes y al resto
├── listados/             un fichero .py por listado ejecutable + datos/
└── proyecto/             proyecto completo cuando la unidad lo necesita
```

## Estructura de los apuntes de cada unidad

1. Nombre del fichero `UDN-tema.md`; título `# UDN · Nombre`, línea de módulo y curso, enlace de vuelta al índice e índice de secciones con enlaces.
2. **Presentación de la unidad**: tabla de criterios de evaluación (CE · criterio · apartados), temporalización por sesiones con fechas, requisitos previos, cómo usar la carpeta y convenciones.
3. Apartados `## N.M Título`. Cada uno empieza con una frase que resume la idea principal y termina con `### Para practicar` (3-4 ejercicios; los autónomos llevan «(A)»).
4. **Práctica de la unidad**, ligada al hito del proyecto integrador, con tabla «CE · evidencias».
5. **Resumen de la unidad**: tabla «Apartado · Idea clave».
6. **Bibliografía de la UDN**, con fecha de consulta de las fuentes web.

## Convenciones de formato

- Cada bloque de código va precedido de su pie en negrita: `**Listado N.M.** Descripción · [ver fichero](listados/listado_N_MM_nombre.py)`. La numeración es correlativa dentro de la unidad.
- Bloques de código siempre con lenguaje (`python`, `bash`, `powershell`, `text`, `csv`, `json`, `toml`).
- Las sesiones interactivas empiezan por `>>>` y no tienen fichero en `listados/`.
- Recuadros con alertas de GitHub:
  - `> [!NOTE]` + `**Desde C++.**` para comparaciones con C++.
  - `> [!TIP]` para buenas prácticas.
  - `> [!WARNING]` para errores frecuentes.
  - `> [!IMPORTANT]` para reglas clave.
- Tablas para comparaciones y referencias; prosa breve, frases de menos de 25 palabras.
- Todo dato tomado de la web se cita en línea con un enlace `([Fuente](url))` y se añade a la bibliografía de la unidad. Priorizar documentación oficial.

## Convenciones del código

- Python 3.14, PEP 8, nombres en español y en `snake_case`.
- Funciones con docstring y anotaciones de tipo; f-strings; `pathlib`; `encoding="utf-8"` al abrir ficheros.
- Cada listado de `listados/` debe ejecutarse sin errores desde esa carpeta, salvo los que fallan a propósito (se indica en su docstring). Las líneas que provocan errores didácticos se dejan comentadas con «descomenta para ver el error».
- Antes de publicar una unidad, ejecutar todos sus listados y comprobar que la salida coincide con la que muestran los apuntes.

## Sitio web

Los apuntes se publican en GitHub Pages con MkDocs Material. `tools/preparar_docs.py` copia cada fichero a `docs/` y reescribe los enlaces: los enlaces entre páginas apuntan a su ruta del sitio y los enlaces a código apuntan a GitHub. Al añadir una unidad hay que registrarla en `PAGINAS` y `ENLACES_INTERNOS` de ese script y en el `nav` de `mkdocs.yml`. Las alertas de GitHub (`> [!TIP]`) se traducen a avisos de Material mediante `tools/hooks_alertas.py`, así que se escriben una sola vez, en el formato de GitHub.

## Flujo de trabajo

- El contenido de cada unidad se diseña con el profesor fuera del repositorio; aquí se incorpora ya revisado.
- Cambios en ramas `claude/…` y mediante pull request; nunca directamente sobre `main`.
- No modificar los apuntes de una unidad ya impartida sin indicarlo en el mensaje de la pull request.
