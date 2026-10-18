# CLAUDE.md · Materiales de «Python aplicado a la Inteligencia Artificial»

Este repositorio contiene los apuntes y el código del módulo optativo de 2.º DAM (curso 2026-2027). Lo leen alumnos que vienen de programar en C++ en 1.º. Todo el contenido está en **español de España**.

## Contexto del módulo

- 3 horas semanales (lunes 2 h, martes 1 h), del 16/09/2026 al 16/02/2027: 53 horas lectivas.
- Unidades: UD1 Python (7 h) · UD2 POO (4 h) · UD3 Análisis de datos + Streamlit (10 h) · UD4 SQL y NoSQL (4 h) · UD5 Big Data (5 h) · UD6 Machine Learning (10 h) · UD7 Proyecto, despliegue y evaluación (9 h) · 4 h de colchón.
- **Conjunto de datos común**: todo el módulo trabaja con `datos-comunes/jugadores.csv` (valoraciones de FIFA 15 a 20: 100.995 filas, 36.559 jugadores, 37 columnas, licencia CC0). Los ejemplos de los apuntes y los hitos salen de ahí. La excepción es la UD2, que enseña estructura y usa la tienda de Acceso a Datos. Su página de referencia es `datos-comunes/README.md`.
- Trampas del dataset que hay que respetar en todo listado que toque dinero: FIFA 15 trae `value_eur` y `wage_eur` a cero en sus 15.465 filas, `release_clause_eur` no existe antes de FIFA 18, y cada edición tiene unos 250 agentes libres con valor cero. Los nulos de `pace`…`physic` (11,1 %) y `gk_*` (88,9 %) son estructurales y complementarios: no se imputan.
- **Evaluación**: autoevaluación del alumno en cada hito (formativa, no puntúa), más un Día en la Oficina sin IA y una defensa oral. No hay proyecto final con conjunto de datos propio: los hitos van de la mano de los apuntes a propósito.
- Entorno: Python 3.14, VS Code con las extensiones Python y Jupyter, un entorno virtual `.venv` por proyecto, paquetes en `src/` instalados con `pip install -e .`. Despliegue final en Streamlit Community Cloud.

## Estructura

```text
README.md                 índice del módulo (actualizar la columna «Estado» al publicar una unidad)
udN-tema/
├── UDN-tema.md           apuntes de la unidad (fichero principal)
├── README.md             portada de la carpeta: enlaces a los apuntes y al resto
├── figuras/              figuras SVG de la unidad
├── listados/             un fichero .py por listado ejecutable + datos/
└── proyecto/             proyecto completo cuando la unidad lo necesita
sitio/
├── overrides/            plantillas propias de MkDocs Material (título del índice, traducciones)
└── stylesheets/extra.css estilos propios del sitio
tools/                    scripts del sitio y de las figuras
```

## Estructura de los apuntes de cada unidad

1. Nombre del fichero `UDN-tema.md`; título `# UDN · Nombre`, línea de módulo y curso, enlace de vuelta al índice e índice de secciones con enlaces.
2. **Presentación de la unidad**: tabla de criterios de evaluación (CE · criterio · apartados), temporalización por sesiones con fechas, requisitos previos, cómo usar la carpeta y convenciones.
3. Apartados `## N.M Título`. Cada uno empieza con una frase que resume la idea principal y termina con `### Para practicar` (3-4 ejercicios; los autónomos llevan «(A)»).
4. **Práctica de la unidad**, ligada al hito del proyecto integrador, con tabla «CE · evidencias» y una **hoja de autoevaluación**: comprobaciones concretas y con cifras («te deben quedar N filas») para que el alumno sepa solo si va bien. Abre con el esquema de la ruta del hito (`figuras/hito-N.svg`): de dónde se parte, los pasos numerados con lo que produce cada uno y lo que se entrega. Lo genera `ruta_del_hito()` en `tools/generar_figuras.py`, a partir del diccionario `HITOS`; el texto alternativo del Markdown es el `<title>` del SVG, así que al cambiar un paso hay que regenerar la figura y volver a copiar ese texto.
5. **Resumen de la unidad**: tabla «Apartado · Idea clave».
6. **Bibliografía de la UDN**, con fecha de consulta de las fuentes web.
7. **Continuar**: tabla de tres columnas con la unidad anterior, el índice del módulo y la siguiente. Las rutas son relativas (`../udN-tema/UDN-tema.md`) para que funcionen en GitHub, y `tools/preparar_docs.py` las traduce a las del sitio.

## Convenciones de formato

- Cada bloque de código va precedido de su pie en negrita: `**Listado N.M.** Descripción · [ver fichero](listados/listado_N_MM_nombre.py)`. La numeración es correlativa dentro de la unidad.
- Bloques de código siempre con lenguaje (`python`, `bash`, `powershell`, `text`, `csv`, `json`, `toml`).
- Las sesiones interactivas empiezan por `>>>` y no tienen fichero en `listados/`.
- Recuadros con alertas de GitHub:
  - `> [!NOTE]` + `**Desde C++.**` para comparaciones con C++.
  - `> [!NOTE]` + `**Desde Java.**` para comparaciones con Acceso a Datos, el módulo que el alumnado cursa en paralelo.
  - `> [!TIP]` para buenas prácticas.
  - `> [!WARNING]` para errores frecuentes.
  - `> [!IMPORTANT]` para reglas clave.
- **Se explica, no se enuncia.** El objetivo es que el alumno entienda, no que reconozca. Cada bloque de código va precedido del concepto y del porqué, y seguido de qué ha pasado y qué conviene mirar. Si una idea necesita tres párrafos, lleva tres párrafos: el tiempo de clase no cambia, lo que crece es lo que pueden estudiar solos.
- Frases cortas, pero las que hagan falta. Nada de párrafos de una línea que dan por sabido lo que no lo está. Antes de usar un término por primera vez, se define.
- Tablas para comparaciones y referencias.
- Figuras: SVG en `udN-tema/figuras/`, generadas por `tools/generar_figuras.py` con los ayudantes de `tools/figuras.py`. La excepción es `ud3-datos/figuras/dispersion-ejemplo.svg`, que no es un esquema sino un gráfico de verdad y lo dibuja `tools/generar_dispersion.py` con matplotlib sobre el conjunto de datos común. Las que empiezan por `fig-N-M-` son copias sin modificar de las figuras del repositorio `ad-dam` (Acceso a Datos, CC0): no se regeneran y su pie cita de qué figura del otro módulo proceden. Se insertan con `![pie](figuras/nombre.svg)` seguido de `*Figura N.M. Pie.*`, siempre después del texto que explican. Fondo claro propio, para que se lean en modo claro y oscuro.
- Enunciados de ejercicios: cuando el ejercicio tenga un resultado concreto, el enunciado incluye los datos de ejemplo y la salida esperada en un bloque de código. Un enunciado que no se pueda comprobar solo está mal escrito.
- Todo dato tomado de la web se cita en línea con un enlace `([Fuente](url))` y se añade a la bibliografía de la unidad. Priorizar documentación oficial.

## Convenciones del código

- Python 3.14, PEP 8, nombres en español y en `snake_case`.
- Funciones con docstring y anotaciones de tipo; f-strings; `pathlib`; `encoding="utf-8"` al abrir ficheros.
- Cada listado de `listados/` debe ejecutarse sin errores desde esa carpeta, salvo los que fallan a propósito (se indica en su docstring). Las líneas que provocan errores didácticos se dejan comentadas con «descomenta para ver el error».
- Antes de publicar una unidad, ejecutar todos sus listados y comprobar que la salida coincide con la que muestran los apuntes.

## Sitio web

Los apuntes se publican en GitHub Pages con MkDocs Material. `tools/preparar_docs.py` copia cada fichero a `docs/` y reescribe los enlaces: los enlaces entre páginas apuntan a su ruta del sitio y los enlaces a código apuntan a GitHub. Al añadir una unidad hay que registrarla en `PAGINAS` y `ENLACES_INTERNOS` de ese script y en el `nav` de `mkdocs.yml`. Las alertas de GitHub (`> [!TIP]`) se traducen a avisos de Material mediante `tools/hooks_alertas.py`, así que se escriben una sola vez, en el formato de GitHub.

La carpeta `sitio/` contiene lo que personaliza el tema y **no** se copia a `docs/` salvo los estilos:

- `sitio/overrides/partials/toc.html`: titula «En esta unidad» el índice de la derecha en las páginas `udN`.
- `sitio/overrides/partials/languages/custom.html`: textos propios del buscador; lo que no esté ahí se toma del español del tema. Lo activa `theme.language: custom`.
- `sitio/stylesheets/extra.css`: índice lateral fijo con el apartado actual coloreado, buscador más ancho, figuras centradas y pie de navegación. `preparar_docs.py` lo copia a `docs/stylesheets/`.

`docs/` y `site/` se generan y están en `.gitignore`: nunca se editan a mano.

## Flujo de trabajo

- El contenido de cada unidad se diseña con el profesor fuera del repositorio; aquí se incorpora ya revisado.
- La UD2 usa como ejemplo la tienda de la UD0 de Acceso a Datos (`https://github.com/neozizou/ad-dam`). El paquete `ud2-poo/listados/tienda/` es su versión en Python y debe seguir reflejando el modelo de ese repositorio; se ejecuta con `python -m tienda.app` desde `listados/`.
- Cambios en ramas `claude/…` y mediante pull request; nunca directamente sobre `main`.
- No modificar los apuntes de una unidad ya impartida sin indicarlo en el mensaje de la pull request.
