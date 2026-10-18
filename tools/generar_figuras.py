"""Genera las figuras SVG de los apuntes.

    python tools/generar_figuras.py

Cada función dibuja una figura y la guarda en la carpeta figuras/ de su unidad.
Para cambiar una figura, edita su función y vuelve a ejecutar el script.
"""

from pathlib import Path

from figuras import (
    AZUL, AZUL_CLARO, BORDE, FONDO, Figura, GRIS, GRIS_CLARO, MORADO, MORADO_CLARO,
    NARANJA, NARANJA_CLARO, PANEL, ROJO, ROJO_CLARO, SUAVE, TINTA, VERDE, VERDE_CLARO,
)

RAIZ = Path(__file__).resolve().parent.parent
UNIDADES = {
    1: RAIZ / "ud1-python" / "figuras",
    2: RAIZ / "ud2-poo" / "figuras",
    3: RAIZ / "ud3-datos" / "figuras",
    4: RAIZ / "ud4-bd" / "figuras",
    5: RAIZ / "ud5-bigdata" / "figuras",
    6: RAIZ / "ud6-ml" / "figuras",
    7: RAIZ / "ud7-proyecto" / "figuras",
}


# ---------------------------------------------------------------- UD1
def ud1_variables() -> Figura:
    f = Figura(780, 290, "Las variables de Python son etiquetas, no cajas")
    f.caja(20, 20, 350, 250, relleno=PANEL, borde=BORDE)
    f.caja(410, 20, 350, 250, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "C++: una caja con tipo fijo")
    f.encabezado(430, 48, "Python: una etiqueta pegada a un objeto")

    # C++
    f.caja(60, 70, 180, 70, relleno=FONDO, borde=AZUL)
    f.texto(150, 100, "int edad", tam=13, color=AZUL, anclaje="middle", mono=True)
    f.texto(150, 125, "20", tam=20, anclaje="middle", mono=True, peso="700")
    f.nota(60, 170, "La caja reserva memoria y solo")
    f.nota(60, 190, "admite enteros.")
    f.nota(60, 220, 'edad = "veinte";', mono=True, color=ROJO)
    f.nota(60, 242, "error de compilación", color=ROJO)

    # Python
    f.etiqueta(440, 80, 90, 36, "edad", AZUL, AZUL_CLARO, tam=13)
    f.caja(620, 65, 110, 60, relleno=FONDO, borde=SUAVE)
    f.texto(675, 92, "20", tam=20, anclaje="middle", mono=True, peso="700")
    f.texto(675, 112, "int", tam=11, anclaje="middle", color=SUAVE, mono=True)
    f.flecha(535, 98, 615, 95)

    f.caja(620, 165, 110, 60, relleno=FONDO, borde=SUAVE)
    f.texto(675, 192, "'veinte'", tam=15, anclaje="middle", mono=True, peso="700")
    f.texto(675, 212, "str", tam=11, anclaje="middle", color=SUAVE, mono=True)
    f.flecha(535, 110, 615, 190, color=VERDE, guiones="6 4")
    f.nota(440, 150, "edad = \"veinte\"", mono=True, color=VERDE)
    f.nota(440, 172, "despega la etiqueta")
    f.nota(440, 192, "y la pega en otro")
    f.nota(440, 212, "objeto: el tipo va")
    f.nota(440, 232, "con el valor.")
    return f


def ud1_estructuras() -> Figura:
    f = Figura(860, 300, "Las cuatro colecciones de Python")
    datos = [
        ("list", "[6.5, 4.0, 6.5]", AZUL, AZUL_CLARO,
         ["Ordenada", "Mutable", "Admite repetidos"]),
        ("tuple", "(37.1, -3.6)", VERDE, VERDE_CLARO,
         ["Ordenada", "Inmutable", "Vale como clave"]),
        ("dict", '{"nota": 6.5}', NARANJA, NARANJA_CLARO,
         ["Clave → valor", "Claves únicas", "Acceso directo"]),
        ("set", "{6.5, 4.0}", MORADO, MORADO_CLARO,
         ["Sin orden", "Sin repetidos", "Pertenencia rápida"]),
    ]
    x = 20
    for nombre, ejemplo, color, claro, rasgos in datos:
        f.caja(x, 20, 195, 260, relleno=FONDO, borde=color)
        f.caja(x, 20, 195, 44, relleno=claro, borde=color)
        f.texto(x + 97, 49, nombre, tam=17, anclaje="middle", mono=True, peso="700")
        f.texto(x + 97, 92, ejemplo, tam=12.5, anclaje="middle", mono=True, color=TINTA)
        y = 130
        for rasgo in rasgos:
            f.circulo(x + 24, y - 5, 4, relleno=color, borde=color)
            f.nota(x + 38, y, rasgo)
            y += 30
        x += 207
    f.nota(20, 295, "Una lista de diccionarios ya es una tabla de datos: es lo que en la UD3 será un DataFrame.",
           color=SUAVE)
    return f


def ud1_alias() -> Figura:
    f = Figura(820, 330, "Asignar no es copiar")
    f.caja(20, 20, 380, 290, relleno=PANEL, borde=BORDE)
    f.caja(420, 20, 380, 290, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "b = a  →  alias")
    f.encabezado(440, 48, "c = a.copy()  →  copia")

    f.etiqueta(50, 75, 70, 34, "a", AZUL, AZUL_CLARO)
    f.etiqueta(50, 125, 70, 34, "b", AZUL, AZUL_CLARO)
    f.caja(220, 80, 150, 75, relleno=FONDO, borde=SUAVE)
    f.texto(295, 112, "[1, 2, 3, 4]", tam=15, anclaje="middle", mono=True, peso="700")
    f.texto(295, 136, "un solo objeto", tam=11, anclaje="middle", color=SUAVE)
    f.flecha(125, 92, 215, 100)
    f.flecha(125, 142, 215, 135)
    f.nota(50, 195, "b.append(4) también cambia a:", mono=False)
    f.nota(50, 215, "los dos nombres apuntan al mismo sitio.")
    f.caja(50, 235, 320, 60, relleno=ROJO_CLARO, borde=ROJO)
    f.nota(64, 258, "matriz = [[0] * 3] * 2", mono=True, color=ROJO)
    f.nota(64, 280, "crea DOS referencias a la MISMA fila.", color=ROJO)

    f.etiqueta(450, 75, 70, 34, "a", AZUL, AZUL_CLARO)
    f.etiqueta(450, 150, 70, 34, "c", VERDE, VERDE_CLARO)
    f.caja(620, 70, 150, 50, relleno=FONDO, borde=SUAVE)
    f.texto(695, 100, "[1, 2, 3, 4]", tam=14, anclaje="middle", mono=True)
    f.caja(620, 145, 150, 50, relleno=FONDO, borde=SUAVE)
    f.texto(695, 175, "[1, 2, 3, 4, 5]", tam=14, anclaje="middle", mono=True)
    f.flecha(525, 90, 615, 93)
    f.flecha(525, 165, 615, 168)
    f.nota(450, 225, "Dos objetos independientes.")
    f.caja(450, 245, 320, 50, relleno=VERDE_CLARO, borde=VERDE)
    f.nota(464, 275, "matriz = [[0] * 3 for _ in range(2)]", mono=True, color=VERDE)
    return f


def ud1_traceback() -> Figura:
    f = Figura(820, 300, "Cómo se lee un traceback")
    f.caja(20, 20, 520, 260, relleno="#1f2430", borde="#1f2430")
    lineas = [
        ("Traceback (most recent call last):", "#c7cedb"),
        ('  File "notas.py", line 5, in <module>', "#c7cedb"),
        ("    print(media(notas))", "#9fd3ff"),
        ('  File "notas.py", line 2, in media', "#c7cedb"),
        ("    return sum(valores) / len(valores)", "#9fd3ff"),
        ("           ~~~~~~~~~~~~~^~~~~~~~~~~~~~", "#ffd27f"),
        ("ZeroDivisionError: division by zero", "#ff9d8a"),
    ]
    y = 58
    for texto, color in lineas:
        f.texto(40, y, texto, tam=12.5, color=color, mono=True)
        y += 30
    f.ruta("M 560 240 L 560 70", borde=VERDE, punta=True)
    f.texto(575, 250, "3. Qué pasó: el tipo de error y su mensaje", tam=12.5, color=TINTA)
    f.texto(575, 190, "2. Dónde: la línea exacta, con marcas", tam=12.5, color=TINTA)
    f.texto(575, 180, "   bajo la operación culpable", tam=12.5, color=TINTA)
    f.texto(575, 80, "1. Cómo se llegó: la cadena de llamadas", tam=12.5, color=TINTA)
    f.texto(575, 110, "Se lee SIEMPRE de abajo arriba", tam=13.5, color=VERDE, peso="700")
    return f


# ---------------------------------------------------------------- UD2
def ud2_modelo_objetos() -> Figura:
    f = Figura(820, 330, "Clase, instancias y atributos")
    f.caja(250, 20, 300, 120, relleno=AZUL_CLARO, borde=AZUL)
    f.texto(400, 48, "class Alumno", tam=16, anclaje="middle", mono=True, peso="700")
    f.linea(265, 60, 535, 60, color=AZUL)
    f.texto(270, 83, 'centro = "C.E.S. DAM"', tam=12.5, mono=True)
    f.nota(270, 101, "atributo de CLASE: uno solo, compartido")
    f.texto(270, 125, "def ha_aprobado(self)", tam=12.5, mono=True)

    for x, nombre, nota in ((60, "ana", "6.5"), (480, "luis", "4.0")):
        f.caja(x, 200, 280, 110, relleno=FONDO, borde=VERDE)
        f.texto(x + 140, 228, f"{nombre} = Alumno(...)", tam=14, anclaje="middle",
                mono=True, peso="700")
        f.linea(x + 15, 240, x + 265, 240, color=VERDE)
        f.texto(x + 25, 263, f'self.nombre = "{nombre.title()}"', tam=12.5, mono=True)
        f.texto(x + 25, 285, f"self.nota = {nota}", tam=12.5, mono=True)
        f.nota(x + 25, 303, "atributos de INSTANCIA: uno por objeto")

    f.flecha(330, 145, 200, 195, curva=(250, 180))
    f.flecha(470, 145, 600, 195, curva=(550, 180))
    f.nota(355, 178, "cada objeto conoce a su clase", color=SUAVE)
    return f


def ud2_mro() -> Figura:
    f = Figura(780, 330, "Herencia múltiple y orden de resolución (MRO)")
    f.etiqueta(40, 40, 230, 54, "ExportableJSONMixin", MORADO, MORADO_CLARO, tam=13)
    f.etiqueta(330, 40, 160, 54, "Registrable", MORADO, MORADO_CLARO, tam=13)
    f.etiqueta(550, 40, 160, 54, "object", GRIS, GRIS_CLARO, tam=13)
    f.etiqueta(180, 180, 200, 54, "Venta", AZUL, AZUL_CLARO, tam=15)

    f.flecha(240, 178, 150, 100, curva=(180, 130))
    f.flecha(320, 178, 400, 100, curva=(370, 130))
    f.flecha(490, 67, 545, 67)

    f.nota(40, 120, "class Venta(ExportableJSONMixin, Registrable):", mono=True)
    f.caja(430, 150, 320, 150, relleno=PANEL, borde=BORDE)
    f.encabezado(450, 178, "Venta.__mro__")
    for i, nombre in enumerate(["Venta", "ExportableJSONMixin", "Registrable", "object"]):
        f.texto(452, 205 + i * 24, f"{i + 1}. {nombre}", tam=12.5, mono=True)
    f.nota(40, 250, "Python busca cada método en ese orden")
    f.nota(40, 272, "y se queda con el primero que encuentra.")
    f.nota(40, 300, "Un mixin aporta una capacidad suelta; no se usa solo.", color=SUAVE)
    return f


def ud2_generadores() -> Figura:
    f = Figura(840, 310, "Lista frente a generador")
    f.caja(20, 20, 390, 270, relleno=PANEL, borde=BORDE)
    f.caja(430, 20, 390, 270, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "Lista: [f for f in filas]")
    f.encabezado(450, 48, "Generador: (f for f in filas)")

    f.caja(40, 65, 350, 150, relleno=FONDO, borde=ROJO)
    for i in range(5):
        f.caja(55, 80 + i * 26, 320, 20, relleno=ROJO_CLARO, borde=ROJO, radio=4,
               grosor=1)
        f.texto(65, 95 + i * 26, f"fila {i + 1}", tam=11, mono=True)
    f.nota(40, 235, "Todas las filas, a la vez, en memoria.")
    f.nota(40, 257, "Con un fichero de 50 GB, no cabe.", color=ROJO)

    f.caja(450, 65, 350, 150, relleno=FONDO, borde=VERDE)
    f.caja(465, 120, 320, 22, relleno=VERDE_CLARO, borde=VERDE, radio=4, grosor=1)
    f.texto(475, 136, "fila 3", tam=11, mono=True)
    f.nota(465, 100, "yield entrega una y espera", color=VERDE)
    f.flecha(620, 160, 620, 205)
    f.nota(540, 232, "Una fila cada vez: memoria constante.")
    f.nota(540, 254, "Es la base de la UD5.", color=VERDE)
    return f


# ---------------------------------------------------------------- UD3
def ud3_ciclo() -> Figura:
    f = Figura(880, 250, "El ciclo del dato")
    pasos = [
        ("Cargar", "read_csv", AZUL, AZUL_CLARO, "3.2"),
        ("Limpiar", "nulos, tipos", NARANJA, NARANJA_CLARO, "3.4"),
        ("Transformar", "groupby, merge", MORADO, MORADO_CLARO, "3.5"),
        ("Visualizar", "matplotlib", VERDE, VERDE_CLARO, "3.6"),
        ("Interpretar", "patrones", AZUL, AZUL_CLARO, "3.7"),
        ("Comunicar", "Streamlit", VERDE, VERDE_CLARO, "3.8"),
    ]
    x = 25
    for titulo, detalle, color, claro, apartado in pasos:
        f.caja(x, 70, 118, 92, relleno=claro, borde=color)
        f.texto(x + 59, 100, titulo, tam=14, anclaje="middle", peso="700")
        f.texto(x + 59, 122, detalle, tam=11, anclaje="middle", color=SUAVE, mono=True)
        f.texto(x + 59, 148, apartado, tam=11, anclaje="middle", color=color, peso="700")
        if x < 700:
            f.flecha(x + 120, 116, x + 138, 116)
        x += 141
    f.encabezado(25, 48, "El orden no cambia: cambian las herramientas según el volumen")
    f.ruta("M 760 170 Q 440 230 85 170", borde=GRIS, guiones="6 5", punta=True)
    f.nota(330, 215, "casi siempre hay que volver a limpiar", color=GRIS)
    return f


def ud3_dataframe() -> Figura:
    f = Figura(820, 320, "Anatomía de un DataFrame")
    columnas = ["short_name", "club", "overall", "value_eur"]
    tipos = ["str", "str", "int64", "Int64"]
    filas = [
        ("0", "L. Messi", "FC Barcelona", "94", "95500000"),
        ("1", "Neymar Jr", "Paris S-G", "92", "105500000"),
        ("2", "J. Oblak", "Atlético", "91", "77500000"),
    ]
    x0, y0, ancho = 120, 90, 150
    f.caja(x0 - 70, y0 - 40, 70 + ancho * 4, 40, relleno=AZUL_CLARO, borde=AZUL, radio=6)
    for i, (col, tipo) in enumerate(zip(columnas, tipos)):
        f.texto(x0 + ancho * i + ancho / 2, y0 - 20, col, tam=13, anclaje="middle",
                mono=True, peso="700")
        f.texto(x0 + ancho * i + ancho / 2, y0 - 5, tipo, tam=10, anclaje="middle",
                color=SUAVE, mono=True)
    for j, fila in enumerate(filas):
        y = y0 + 10 + j * 38
        f.caja(x0 - 70, y, 70, 38, relleno=PANEL, borde=BORDE, radio=0, grosor=1)
        f.texto(x0 - 35, y + 24, fila[0], tam=12, anclaje="middle", mono=True, color=SUAVE)
        for i, valor in enumerate(fila[1:]):
            relleno = VERDE_CLARO if i == 2 else FONDO
            f.caja(x0 + ancho * i, y, ancho, 38, relleno=relleno, borde=BORDE, radio=0,
                   grosor=1)
            f.texto(x0 + ancho * i + ancho / 2, y + 24, valor, tam=12, anclaje="middle",
                    mono=True)
    f.texto(x0 - 35, y0 - 55, "índice", tam=11.5, anclaje="middle", color=AZUL, peso="700")
    f.flecha(x0 + ancho * 2 + ancho / 2, 255, x0 + ancho * 2 + ancho / 2, 230)
    f.texto(x0 + ancho * 2 + ancho / 2, 275, "una columna es una Series", tam=12.5,
            anclaje="middle", color=VERDE, peso="700")
    f.encabezado(230, 30, "df.shape = (3, 4)   ·   df.columns   ·   df.dtypes")
    f.nota(30, 300, "df.loc[0, \'club\'] usa etiquetas; df.iloc[0, 1], posiciones.", mono=True)
    return f


def ud3_groupby() -> Figura:
    f = Figura(860, 300, "groupby: dividir, aplicar y combinar")
    etapas = ["1. Dividir por clave", "2. Aplicar la función", "3. Combinar"]
    for i, titulo in enumerate(etapas):
        f.encabezado(30 + i * 290, 45, titulo, tam=13.5)
    datos = [("ST", 71, VERDE, VERDE_CLARO), ("CB", 65, NARANJA, NARANJA_CLARO),
             ("ST", 79, VERDE, VERDE_CLARO), ("CB", 67, NARANJA, NARANJA_CLARO)]
    for j, (puesto, valor, color, claro) in enumerate(datos):
        f.caja(30, 65 + j * 42, 200, 34, relleno=claro, borde=color, radio=6)
        f.texto(45, 87 + j * 42, puesto, tam=12.5, mono=True)
        f.texto(205, 87 + j * 42, str(valor), tam=12.5, mono=True, anclaje="end")
    f.flecha(240, 150, 300, 150)
    grupos = [("ST", ["71", "79"], VERDE, VERDE_CLARO, 65),
              ("CB", ["65", "67"], NARANJA, NARANJA_CLARO, 170)]
    for puesto, valores, color, claro, y in grupos:
        f.caja(310, y, 190, 86, relleno=claro, borde=color)
        f.texto(325, y + 24, puesto, tam=12.5, mono=True, peso="700")
        f.texto(325, y + 48, " , ".join(valores), tam=12.5, mono=True)
        media = sum(int(v) for v in valores) / len(valores)
        f.texto(325, y + 72, f"mean() = {media:.0f}", tam=12.5, mono=True, color=color)
    f.flecha(510, 150, 570, 150)
    f.caja(580, 95, 250, 110, relleno=FONDO, borde=AZUL)
    f.texto(600, 125, "posicion", tam=12.5, mono=True, color=SUAVE)
    f.texto(810, 125, "overall", tam=12.5, mono=True, color=SUAVE, anclaje="end")
    for j, (c, v) in enumerate([("ST", "75"), ("CB", "66")]):
        f.texto(600, 152 + j * 25, c, tam=12.5, mono=True)
        f.texto(810, 152 + j * 25, v, tam=12.5, mono=True, anclaje="end")
    f.nota(30, 270, "sol.groupby(\'posicion\')[\'overall\'].mean()", mono=True, color=AZUL)
    f.nota(400, 270, "Es el GROUP BY de SQL y el map-reduce de la UD5.", color=SUAVE)
    return f


def ud3_merge() -> Figura:
    f = Figura(840, 320, "merge: el JOIN de pandas")
    f.encabezado(30, 42, "jugadores")
    f.caja(30, 55, 230, 120, relleno=FONDO, borde=AZUL)
    f.texto(45, 80, "short_name", tam=12, mono=True, color=SUAVE)
    f.texto(190, 80, "posicion", tam=12, mono=True, color=SUAVE)
    for j, (c, v) in enumerate([("L. Messi", "RW"), ("J. Oblak", "GK"),
                                ("K. Koulibaly", "CB")]):
        f.texto(45, 105 + j * 25, c, tam=12, mono=True)
        f.texto(190, 105 + j * 25, v, tam=12, mono=True)
    f.encabezado(300, 42, "posiciones")
    f.caja(300, 55, 230, 120, relleno=FONDO, borde=VERDE)
    f.texto(315, 80, "posicion", tam=12, mono=True, color=SUAVE)
    f.texto(425, 80, "linea", tam=12, mono=True, color=SUAVE)
    for j, (c, p) in enumerate([("RW", "Ataque"), ("GK", "Portería"),
                                ("CB", "Defensa")]):
        f.texto(315, 105 + j * 25, c, tam=12, mono=True)
        f.texto(425, 105 + j * 25, p, tam=12, mono=True)
    f.caja(570, 55, 250, 120, relleno=PANEL, borde=BORDE)
    f.encabezado(585, 42, "how = \'left\'")
    f.texto(585, 80, "short_name", tam=12, mono=True, color=SUAVE)
    f.texto(730, 80, "linea", tam=12, mono=True, color=SUAVE)
    for j, (c, p, color) in enumerate([("L. Messi", "Ataque", TINTA),
                                       ("J. Oblak", "Portería", TINTA),
                                       ("K. Koulibaly", "Defensa", TINTA)]):
        f.texto(585, 105 + j * 25, c, tam=12, mono=True, color=color)
        f.texto(730, 105 + j * 25, p, tam=12, mono=True, color=color)
    f.flecha(265, 115, 295, 115)
    f.flecha(535, 115, 565, 115)
    f.caja(30, 200, 790, 100, relleno=PANEL, borde=BORDE)
    tipos = [("inner", "solo las que casan en ambas"), ("left", "todas las de la izquierda"),
             ("right", "todas las de la derecha"), ("outer", "todas, casen o no")]
    for i, (nombre, descripcion) in enumerate(tipos):
        x = 50 + i * 195
        f.etiqueta(x, 220, 90, 32, nombre, AZUL, AZUL_CLARO, tam=12.5)
        f.nota(x, 272, descripcion, tam=11)
    f.nota(30, 195, "Tras todo merge: ¿han cambiado las filas? ¿ha quedado alguien sin pareja?",
           color=ROJO)
    return f


# ---------------------------------------------------------------- UD4
def ud4_indice() -> Figura:
    f = Figura(840, 290, "Qué cambia al crear un índice")
    f.caja(20, 20, 390, 250, relleno=PANEL, borde=BORDE)
    f.caja(430, 20, 390, 250, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "SCAN: recorre toda la tabla")
    f.encabezado(450, 48, "SEARCH: va directo con el índice")
    for j in range(8):
        y = 70 + j * 24
        acierto = j == 5
        f.caja(45, y, 340, 20, relleno=ROJO_CLARO if not acierto else VERDE_CLARO,
               borde=ROJO if not acierto else VERDE, radio=4, grosor=1)
        f.texto(55, y + 15, f"fila {j + 1}" + ("   <- la que buscabas" if acierto else ""),
                tam=10.5, mono=True)
    f.nota(45, 282, "0,140 s / 2000 consultas", color=ROJO)
    f.caja(455, 70, 150, 100, relleno=AZUL_CLARO, borde=AZUL)
    f.texto(530, 100, "índice", tam=13, anclaje="middle", peso="700")
    f.texto(530, 125, "ciudad +", tam=11.5, anclaje="middle", mono=True)
    f.texto(530, 143, "producto", tam=11.5, anclaje="middle", mono=True)
    f.caja(655, 190, 150, 44, relleno=VERDE_CLARO, borde=VERDE)
    f.texto(730, 218, "fila 6", tam=12.5, anclaje="middle", mono=True)
    f.flecha(610, 140, 700, 185)
    f.nota(455, 200, "Estructura ordenada")
    f.nota(455, 220, "que apunta a la fila.")
    f.nota(455, 282, "0,013 s / 2000 consultas", color=VERDE)
    return f


def ud4_tabla_documento() -> Figura:
    f = Figura(860, 330, "Relacional frente a documental")
    f.caja(20, 20, 400, 290, relleno=PANEL, borde=BORDE)
    f.caja(440, 20, 400, 290, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "SQL: dos tablas y una clave ajena")
    f.encabezado(460, 48, "NoSQL: un documento completo")
    f.caja(40, 65, 360, 85, relleno=FONDO, borde=AZUL)
    f.texto(55, 90, "producto", tam=12, mono=True, color=SUAVE)
    for x, cab, val in ((55, "id", "7"), (110, "nombre", "portátil"),
                        (250, "precio", "899.90")):
        f.texto(x, 115, cab, tam=12, mono=True, color=SUAVE)
        f.texto(x, 138, val, tam=12, mono=True)
    f.caja(40, 170, 360, 110, relleno=FONDO, borde=VERDE)
    f.texto(55, 195, "especificación", tam=12, mono=True, color=SUAVE)
    for x, cab, valores in ((55, "producto_id", ["7", "7"]),
                            (190, "clave", ["ram_gb", "ssd_gb"]),
                            (300, "valor", ["16", "512"])):
        f.texto(x, 220, cab, tam=12, mono=True, color=SUAVE)
        for k, valor in enumerate(valores):
            f.texto(x, 243 + k * 23, valor, tam=12, mono=True)
    f.flecha(220, 155, 220, 168)
    f.nota(230, 165, "JOIN", color=SUAVE, mono=True)
    lineas = [
        "{", '  "nombre": "portátil",', '  "precio": 899.90,',
        '  "especificaciones": {', '    "ram_gb": 16,', '    "ssd_gb": 512',
        "  },", '  "etiquetas": ["oficina"]', "}",
    ]
    f.caja(460, 65, 360, 215, relleno=FONDO, borde=MORADO)
    for i, linea in enumerate(lineas):
        f.texto(478, 92 + i * 22, linea, tam=12, mono=True)
    f.nota(40, 300, "Esquema fijo, integridad garantizada", color=AZUL)
    f.nota(460, 300, "Esquema flexible, la validación la haces tú", color=MORADO)
    return f


def ud4_cap() -> Figura:
    f = Figura(760, 330, "Teorema CAP")
    cx, cy, r = 250, 170, 110
    f.ruta(f"M {cx} {cy - r} L {cx - r} {cy + r * 0.8} L {cx + r} {cy + r * 0.8} Z",
           relleno=PANEL, borde=BORDE, grosor=2)
    f.etiqueta(cx - 95, cy - r - 28, 190, 40, "Coherencia", AZUL, AZUL_CLARO, tam=13,
               mono=False)
    f.etiqueta(cx - r - 70, cy + r * 0.8, 150, 40, "Disponibilidad", VERDE, VERDE_CLARO,
               tam=13, mono=False)
    f.etiqueta(cx + r - 80, cy + r * 0.8, 170, 40, "Partición", NARANJA, NARANJA_CLARO,
               tam=13, mono=False)
    f.texto(cx, cy + 10, "elige 2", tam=16, anclaje="middle", peso="700", color=SUAVE)
    f.caja(470, 60, 270, 95, relleno=FONDO, borde=AZUL)
    f.encabezado(488, 88, "Relacional (ACID)")
    f.nota(488, 112, "Prioriza coherencia.")
    f.nota(488, 134, "Escala en vertical.")
    f.caja(470, 175, 270, 95, relleno=FONDO, borde=MORADO)
    f.encabezado(488, 203, "NoSQL distribuido")
    f.nota(488, 227, "Prioriza disponibilidad:")
    f.nota(488, 249, "coherencia eventual.")
    f.nota(30, 310, "En un sistema repartido la red SIEMPRE puede partirse: la P no es opcional.",
           color=SUAVE)
    return f


# ---------------------------------------------------------------- UD5
def ud5_parquet() -> Figura:
    f = Figura(840, 320, "CSV guarda filas seguidas; Parquet, columnas seguidas")
    f.caja(20, 20, 390, 280, relleno=PANEL, borde=BORDE)
    f.caja(430, 20, 390, 280, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "CSV: orientado a filas")
    f.encabezado(450, 48, "Parquet: orientado a columnas")
    colores = [AZUL_CLARO, VERDE_CLARO, NARANJA_CLARO, MORADO_CLARO]
    bordes = [AZUL, VERDE, NARANJA, MORADO]
    etiquetas = ["fecha", "ciudad", "precio", "canal"]
    for j in range(4):
        y = 72 + j * 46
        f.caja(42, y, 356, 38, relleno=FONDO, borde=SUAVE, radio=6)
        for i in range(4):
            f.caja(52 + i * 86, y + 7, 78, 24, relleno=colores[i], borde=bordes[i],
                   radio=4, grosor=1)
            f.texto(91 + i * 86, y + 23, etiquetas[i], tam=9.5, anclaje="middle")
    f.nota(42, 275, "Cada fila entera va junta en el disco.")
    f.nota(42, 296, "Leer 2 columnas obliga a recorrerlo todo.", color=ROJO)
    for i in range(4):
        x = 448 + i * 92
        usada = i in (1, 2)
        f.caja(x, 72, 84, 176, relleno=FONDO, borde=bordes[i] if usada else GRIS,
               radio=6, guiones=None if usada else "5 4")
        for j in range(4):
            f.caja(x + 8, 80 + j * 42, 68, 32,
                   relleno=colores[i] if usada else GRIS_CLARO,
                   borde=bordes[i] if usada else GRIS, radio=4, grosor=1)
            f.texto(x + 42, 100 + j * 42, etiquetas[i], tam=9.5, anclaje="middle",
                    color=TINTA if usada else GRIS)
        f.texto(x + 42, 266, "leída" if usada else "no se lee", tam=10,
                anclaje="middle", color=VERDE if usada else GRIS, peso="700")
    f.nota(448, 296, "7 veces menos espacio; 0,03 s frente a 0,98 s.", color=VERDE)
    return f


def ud5_trozos() -> Figura:
    f = Figura(860, 290, "Lectura por trozos con agregación incremental")
    f.caja(25, 70, 130, 170, relleno=PANEL, borde=BORDE)
    f.texto(90, 100, "fichero", tam=13, anclaje="middle", peso="700")
    f.texto(90, 122, "50 GB", tam=12, anclaje="middle", color=SUAVE, mono=True)
    for j in range(4):
        f.caja(45, 140 + j * 24, 90, 18, relleno=AZUL_CLARO, borde=AZUL, radio=3,
               grosor=1)
    f.flecha(160, 155, 210, 155)
    f.caja(215, 95, 200, 120, relleno=FONDO, borde=AZUL)
    f.encabezado(232, 125, "trozo de 200.000")
    f.nota(232, 150, "importe = unidades")
    f.nota(232, 170, "          * precio")
    f.nota(232, 196, "groupby + sum")
    f.flecha(420, 155, 470, 155)
    f.caja(475, 95, 180, 120, relleno=VERDE_CLARO, borde=VERDE)
    f.encabezado(492, 125, "acumulado")
    for k, (c, v) in enumerate([("Granada", "3.059"), ("Málaga", "845"), ("...", "")]):
        f.texto(492, 155 + k * 25, c, tam=12, mono=True)
        f.texto(640, 155 + k * 25, v, tam=12, mono=True, anclaje="end")
    f.ruta("M 560 230 Q 400 275 320 225", borde=SUAVE, guiones="6 4", punta=True)
    f.nota(360, 268, "y vuelta al siguiente trozo", color=SUAVE)
    f.caja(680, 95, 150, 120, relleno=FONDO, borde=NARANJA)
    f.encabezado(697, 125, "En memoria")
    f.nota(697, 150, "solo 200.000 filas,")
    f.nota(697, 172, "no el fichero entero.")
    f.nota(697, 200, "Memoria constante.", color=NARANJA)
    f.encabezado(25, 48, "pd.read_csv(..., chunksize=200_000)")
    return f


def ud5_mapreduce() -> Figura:
    f = Figura(860, 300, "Map y reduce")
    f.encabezado(30, 42, "1. Reparto")
    f.encabezado(290, 42, "2. Map en paralelo")
    f.encabezado(580, 42, "3. Reduce por clave")
    for j in range(3):
        f.caja(30, 70 + j * 70, 180, 55, relleno=PANEL, borde=BORDE)
        f.texto(45, 95 + j * 70, f"bloque {j + 1}", tam=12, mono=True, peso="700")
        f.texto(45, 115 + j * 70, "ventas sin procesar", tam=10.5, color=SUAVE)
        f.flecha(215, 97 + j * 70, 265, 97 + j * 70)
        color, claro = [(AZUL, AZUL_CLARO), (VERDE, VERDE_CLARO),
                        (NARANJA, NARANJA_CLARO)][j]
        f.caja(270, 70 + j * 70, 230, 55, relleno=claro, borde=color)
        f.texto(285, 95 + j * 70, "('Granada', importe)", tam=11.5, mono=True)
        f.texto(285, 115 + j * 70, "pares clave-valor", tam=10.5, color=SUAVE)
        f.flecha(505, 97 + j * 70, 565, 150, curva=(540, 120 + j * 20))
    f.caja(570, 95, 260, 120, relleno=FONDO, borde=MORADO)
    f.texto(590, 125, "Granada  →  12.480 €", tam=12.5, mono=True)
    f.texto(590, 152, "Málaga   →   9.130 €", tam=12.5, mono=True)
    f.texto(590, 179, "Sevilla  →   7.044 €", tam=12.5, mono=True)
    f.nota(30, 285, "Cada máquina hace su map; el reduce junta por clave. Es el groupby de la UD3, repartido.",
           color=SUAVE)
    return f


# ---------------------------------------------------------------- UD6
def ud6_flujo() -> Figura:
    f = Figura(860, 300, "Programar frente a aprender de los datos")
    f.caja(20, 20, 400, 125, relleno=PANEL, borde=BORDE)
    f.caja(20, 160, 400, 125, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "Programación clásica")
    f.encabezado(40, 188, "Machine Learning")
    for y, entradas, salida, color, claro in (
        (70, ["datos", "reglas"], "resultados", AZUL, AZUL_CLARO),
        (210, ["datos", "resultados"], "reglas", VERDE, VERDE_CLARO),
    ):
        f.etiqueta(42, y, 100, 36, entradas[0], color, claro, tam=12.5, mono=False)
        f.texto(152, y + 24, "+", tam=16, anclaje="middle", color=SUAVE)
        f.etiqueta(165, y, 110, 36, entradas[1], color, claro, tam=12.5, mono=False)
        f.flecha(282, y + 18, 310, y + 18)
        f.etiqueta(315, y, 90, 36, salida, color, claro, tam=12.5, mono=False)
    f.nota(42, 130, "Tú escribes las reglas.")
    f.nota(42, 270, "El modelo las deduce de los ejemplos.")

    f.caja(440, 20, 400, 265, relleno=PANEL, borde=BORDE)
    f.encabezado(460, 48, "Y por eso se parten los datos")
    f.caja(460, 65, 360, 46, relleno=GRIS_CLARO, borde=GRIS)
    f.texto(640, 93, "conjunto completo", tam=13, anclaje="middle")
    f.flecha(600, 115, 560, 140)
    f.flecha(680, 115, 740, 140)
    f.caja(460, 145, 220, 70, relleno=VERDE_CLARO, borde=VERDE)
    f.texto(570, 172, "entrenamiento 80 %", tam=12.5, anclaje="middle", peso="700")
    f.texto(570, 196, "el modelo aprende aquí", tam=11, anclaje="middle", color=SUAVE)
    f.caja(700, 145, 120, 70, relleno=NARANJA_CLARO, borde=NARANJA)
    f.texto(760, 172, "prueba 20 %", tam=12.5, anclaje="middle", peso="700")
    f.texto(760, 196, "no se toca", tam=11, anclaje="middle", color=SUAVE)
    f.nota(460, 245, "La prueba simula los datos futuros: si la usas para decidir algo,")
    f.nota(460, 266, "deja de medir honestamente.", color=NARANJA)
    return f


def ud6_pipeline() -> Figura:
    f = Figura(860, 320, "Pipeline: la preparación va dentro del modelo")
    f.caja(25, 55, 640, 150, relleno=PANEL, borde=AZUL, guiones="7 5")
    f.texto(45, 80, "Pipeline", tam=14, peso="700", color=AZUL, mono=True)
    f.caja(60, 95, 250, 90, relleno=FONDO, borde=SUAVE)
    f.texto(185, 118, "ColumnTransformer", tam=12.5, anclaje="middle", mono=True,
            peso="700")
    f.etiqueta(72, 132, 110, 34, "StandardScaler", VERDE, VERDE_CLARO, tam=10.5)
    f.etiqueta(190, 132, 110, 34, "OneHotEncoder", NARANJA, NARANJA_CLARO, tam=10.5)
    f.flecha(315, 140, 355, 140)
    f.etiqueta(360, 110, 180, 60, "RandomForest", MORADO, MORADO_CLARO, tam=13)
    f.flecha(545, 140, 585, 140)
    f.etiqueta(590, 110, 60, 60, "predicción", AZUL, AZUL_CLARO, tam=10, mono=False)
    f.texto(45, 232, "fit:", tam=13, mono=True, peso="700", color=VERDE)
    f.nota(85, 232, "aprende medias, categorías y árboles SOLO con el entrenamiento")
    f.texto(45, 260, "predict:", tam=13, mono=True, peso="700", color=AZUL)
    f.nota(125, 260, "aplica lo aprendido a datos nuevos, en el mismo orden")
    f.caja(685, 55, 150, 230, relleno=ROJO_CLARO, borde=ROJO)
    f.encabezado(702, 85, "Fuga de datos")
    f.nota(702, 112, "Escalar o imputar", color=ROJO)
    f.nota(702, 132, "antes de partir", color=ROJO)
    f.nota(702, 152, "deja ver la prueba", color=ROJO)
    f.nota(702, 172, "al modelo.", color=ROJO)
    f.nota(702, 208, "Síntoma: un")
    f.nota(702, 228, "resultado")
    f.nota(702, 248, "sospechosamente")
    f.nota(702, 268, "bueno.")
    f.nota(25, 300, "Regla: todo paso que aprenda algo va dentro del Pipeline.", color=AZUL)
    return f


def ud6_confusion() -> Figura:
    f = Figura(840, 415, "Matriz de confusión y métricas")
    x0, y0, c = 150, 78, 150
    f.texto(x0 + c, 44, "predicho", tam=13, anclaje="middle", peso="700", color=SUAVE)
    f.texto(x0 + c / 2, 68, "no devuelta", tam=11.5, anclaje="middle", color=SUAVE)
    f.texto(x0 + c * 1.5, 68, "devuelta", tam=11.5, anclaje="middle", color=SUAVE)
    f.texto(60, y0 + c / 2, "real: no", tam=11.5, color=SUAVE)
    f.texto(60, y0 + c * 1.5, "real: sí", tam=11.5, color=SUAVE)
    celdas = [
        (0, 0, "1340", "aciertos", VERDE, VERDE_CLARO),
        (1, 0, "3", "falsos positivos", NARANJA, NARANJA_CLARO),
        (0, 1, "247", "falsos negativos", ROJO, ROJO_CLARO),
        (1, 1, "10", "aciertos", VERDE, VERDE_CLARO),
    ]
    for i, j, valor, etiqueta, color, claro in celdas:
        f.caja(x0 + i * c, y0 + j * c, c, c, relleno=claro, borde=color, radio=6)
        f.texto(x0 + i * c + c / 2, y0 + j * c + 68, valor, tam=26, anclaje="middle",
                peso="700")
        f.texto(x0 + i * c + c / 2, y0 + j * c + 95, etiqueta, tam=10.5,
                anclaje="middle", color=SUAVE)
    f.caja(480, 85, 340, 195, relleno=PANEL, borde=BORDE)
    f.encabezado(500, 115, "Exactitud 84 %, y aun así inútil")
    f.nota(500, 142, "De 257 devoluciones reales, detecta 10.")
    f.texto(500, 175, "recall = 10 / 257 = 4 %", tam=13, mono=True, color=ROJO)
    f.texto(500, 203, "precisión = 10 / 13 = 77 %", tam=13, mono=True, color=NARANJA)
    f.nota(500, 235, "Con clases desbalanceadas la exactitud")
    f.nota(500, 257, "miente: mira el recall y la matriz.")
    f.nota(60, 400, "Filas: lo que ocurrió. Columnas: lo que dijo el modelo. La diagonal son los aciertos.",
           color=SUAVE)
    return f


def ud6_sobreajuste() -> Figura:
    f = Figura(860, 312, "Subajuste, punto óptimo y sobreajuste")
    puntos = [(30, 60), (60, 35), (95, 70), (130, 45), (165, 25), (200, 55), (235, 30)]
    titulos = [("Subajuste", "profundidad 1", ROJO),
               ("Punto óptimo", "profundidad 8", VERDE),
               ("Sobreajuste", "profundidad 20", ROJO)]
    for k, (titulo, detalle, color) in enumerate(titulos):
        x = 25 + k * 275
        f.caja(x, 40, 260, 180, relleno=PANEL, borde=BORDE)
        f.texto(x + 130, 66, titulo, tam=14, anclaje="middle", peso="700", color=color)
        f.texto(x + 130, 85, detalle, tam=11, anclaje="middle", color=SUAVE, mono=True)
        base = 200
        for px, py in puntos:
            f.circulo(x + 10 + px, base - py, 4, relleno=AZUL, borde=AZUL)
        if k == 0:
            f.ruta(f"M {x + 30} {base - 35} L {x + 250} {base - 50}", borde=color)
        elif k == 1:
            f.ruta(f"M {x + 30} {base - 45} Q {x + 140} {base - 25} {x + 250} {base - 48}",
                   borde=color)
        else:
            d = f"M {x + 30} {base - 62}"
            for px, py in puntos:
                d += f" L {x + 10 + px} {base - py}"
            f.ruta(d, borde=color)
    f.caja(25, 245, 810, 48, relleno=FONDO, borde=BORDE)
    for x, entrena, prueba, color in ((45, "2,60", "2,58", ROJO), (320, "1,42", "1,64", VERDE),
                                      (595, "0,78", "1,97", ROJO)):
        f.texto(x, 275, f"MAE entrena {entrena}", tam=12.5, mono=True, color=color)
        f.texto(x + 150, 275, f"prueba {prueba}", tam=12.5, mono=True, color=color)
    f.nota(25, 236, "El error de entrenamiento siempre baja; el de prueba toca fondo y vuelve a subir.",
           color=SUAVE)
    return f


# ---------------------------------------------------------------- UD7
def ud7_crispdm() -> Figura:
    import math

    f = Figura(780, 350, "El ciclo CRISP-DM")
    cx, cy, r = 390, 180, 120
    f.circulo(cx, cy, r + 42, relleno=PANEL, borde=BORDE, grosor=1)
    fases = [
        ("Comprensión|del negocio", AZUL, AZUL_CLARO),
        ("Comprensión|de los datos", AZUL, AZUL_CLARO),
        ("Preparación|de los datos", NARANJA, NARANJA_CLARO),
        ("Modelado", MORADO, MORADO_CLARO),
        ("Evaluación", VERDE, VERDE_CLARO),
        ("Despliegue", VERDE, VERDE_CLARO),
    ]
    for i, (nombre, color, claro) in enumerate(fases):
        angulo = -math.pi / 2 + i * (2 * math.pi / 6)
        x = cx + r * math.cos(angulo) - 75
        y = cy + r * math.sin(angulo) - 26
        f.caja(x, y, 150, 52, relleno=claro, borde=color)
        lineas = nombre.split("|")
        for k, linea in enumerate(lineas):
            desplazamiento = 32 + (k - (len(lineas) - 1) / 2) * 16 - 4
            f.texto(x + 75, y + desplazamiento, linea, tam=11.5, anclaje="middle",
                    peso="600")
    f.texto(cx, cy - 4, "CRISP-DM", tam=15, anclaje="middle", peso="700", color=SUAVE)
    f.texto(cx, cy + 18, "se recorre en bucle", tam=11.5, anclaje="middle", color=SUAVE)
    f.nota(25, 335, "Evaluar suele revelar que faltan datos o que la pregunta estaba mal planteada: y se vuelve al principio.",
           color=SUAVE)
    return f


def ud7_arquitectura() -> Figura:
    f = Figura(860, 330, "Cómo se reparte el código del proyecto")
    f.caja(300, 100, 250, 120, relleno=AZUL_CLARO, borde=AZUL)
    f.texto(425, 130, "src/paquete/", tam=15, anclaje="middle", mono=True, peso="700")
    f.texto(425, 156, "datos.py · modelo.py", tam=12, anclaje="middle", mono=True)
    f.texto(425, 178, "evaluacion.py", tam=12, anclaje="middle", mono=True)
    f.texto(425, 202, "una sola definición de todo", tam=11, anclaje="middle", color=SUAVE)
    consumidores = [
        (30, 35, "notebooks/", "exploran y explican", MORADO, MORADO_CLARO),
        (30, 230, "tests/", "vigilan que no se rompa", VERDE, VERDE_CLARO),
        (640, 35, "scripts/entrenar.py", "produce el modelo", NARANJA, NARANJA_CLARO),
        (640, 230, "app/app.py", "lo usa quien decide", VERDE, VERDE_CLARO),
    ]
    for x, y, titulo, detalle, color, claro in consumidores:
        f.caja(x, y, 200, 68, relleno=claro, borde=color)
        f.texto(x + 100, y + 30, titulo, tam=12.5, anclaje="middle", mono=True,
                peso="700")
        f.texto(x + 100, y + 52, detalle, tam=11, anclaje="middle", color=SUAVE)
    f.flecha(235, 80, 320, 108)
    f.flecha(235, 258, 320, 212)
    f.flecha(545, 112, 635, 82)
    f.flecha(545, 208, 635, 252)
    f.caja(300, 250, 250, 52, relleno=FONDO, borde=SUAVE)
    f.texto(425, 282, "modelos/modelo.joblib", tam=12.5, anclaje="middle", mono=True)
    f.flecha(740, 108, 740, 225, guiones="6 4")
    f.nota(25, 322, "Los notebooks exploran; los módulos producen. Si la limpieza está en tres sitios, dejan de coincidir.",
           color=SUAVE)
    return f


def ud2_java_python() -> Figura:
    f = Figura(880, 452, "Correspondencia entre la forma de escribirlo en Java y en Python")
    f.caja(20, 20, 395, 412, relleno=PANEL, borde=BORDE)
    f.caja(465, 20, 395, 412, relleno=PANEL, borde=BORDE)
    f.encabezado(40, 48, "Java · Acceso a Datos")
    f.encabezado(485, 48, "Python · esta unidad")

    filas = [
        ("getNombre() / setPrecio()", "@property"),
        ("record Categoria(...)", "@dataclass(frozen=True)"),
        ("enum EstadoPedido", "class EstadoPedido(Enum)"),
        ("equals / hashCode / toString", "__eq__ / __hash__ / __repr__"),
        ("interface + implements", "Protocol, sin implements"),
        ("Optional<Producto>", "Producto | None"),
        ("BigDecimal", "decimal.Decimal"),
        ("try (var f = ...) { }", "with ... as f:"),
    ]
    for i, (java, python) in enumerate(filas):
        y = 70 + i * 44
        f.etiqueta(40, y, 355, 36, java, AZUL, AZUL_CLARO, tam=12.5)
        f.etiqueta(485, y, 355, 36, python, VERDE, VERDE_CLARO, tam=12.5)
        f.flecha(420, y + 18, 460, y + 18)
    return f


def ud2_contrato_doble() -> Figura:
    f = Figura(880, 400, "El mismo contrato en la tienda y en scikit-learn: "
                         "quien lo usa no conoce ninguna clase concreta")
    for x, titulo in ((20, "La tienda"), (460, "scikit-learn")):
        f.caja(x, 20, 400, 360, relleno=PANEL, borde=BORDE)
        f.encabezado(x + 20, 48, titulo)

    def columna(x0: int, usuario: str, contrato: str, metodos: str,
                izquierda: str, derecha: str) -> None:
        f.etiqueta(x0 + 105, 68, 190, 42, usuario, AZUL, AZUL_CLARO, tam=13)
        f.flecha(x0 + 200, 110, x0 + 200, 148)

        f.caja(x0 + 45, 148, 310, 62, relleno=MORADO_CLARO, borde=MORADO, guiones="6 4")
        f.texto(x0 + 200, 172, contrato, tam=13, anclaje="middle", mono=True, peso="600")
        f.texto(x0 + 200, 193, metodos, tam=11.5, color=SUAVE, anclaje="middle", mono=True)

        f.flecha(x0 + 200, 210, x0 + 118, 266)
        f.flecha(x0 + 200, 210, x0 + 282, 266)
        f.etiqueta(x0 + 40, 266, 156, 42, izquierda, VERDE, VERDE_CLARO, tam=11.5)
        f.etiqueta(x0 + 204, 266, 156, 42, derecha, VERDE, VERDE_CLARO, tam=11.5)

    columna(20, "ProductoService", "ProductoRepository",
            "guardar · buscar · borrar · existe",
            "...Memoria", "...Fichero")
    columna(460, "Pipeline", "fit / transform",
            "y fit / predict en el último paso",
            "StandardScaler", "EscaladoPorMaximo")

    f.nota(20 + 200, 345, "Cambiar de implementación", tam=12, anclaje="middle")
    f.nota(20 + 200, 363, "no toca el código de arriba", tam=12, anclaje="middle")
    f.nota(460 + 200, 345, "Un transformador propio encaja", tam=12, anclaje="middle")
    f.nota(460 + 200, 363, "sin heredar de nada", tam=12, anclaje="middle")
    return f


# ------------------------------------------- Rutas de los hitos
def ruta_del_hito(numero: int, entrada: str, pasos: list[tuple[str, str]],
                  entrega: str) -> Figura:
    """Dibuja la ruta de un hito: de dónde se parte, los pasos y qué se entrega.

    Cada paso es una pareja (qué hay que hacer, qué fichero produce).
    """
    ancho, margen = 900, 24
    banda_alto, fila_alto, inicio = 54, 58, 100
    alto = inicio + len(pasos) * fila_alto + 14 + banda_alto + margen

    descripcion = (f"Ruta del hito {numero}. Se parte de: {entrada}. "
                   + " ".join(f"Paso {i}: {que}, produce {fichero}."
                              for i, (que, fichero) in enumerate(pasos, start=1))
                   + f" Se entrega: {entrega}.")
    f = Figura(ancho, alto, descripcion)
    interior = ancho - 2 * margen

    def banda(y: int, etiqueta: str, texto: str, borde: str, relleno: str) -> None:
        f.caja(margen, y, interior, banda_alto, relleno=relleno, borde=borde)
        f.texto(margen + 20, y + 21, etiqueta, tam=10, color=SUAVE, peso="700")
        f.texto(margen + 20, y + 41, texto, tam=13, peso="500")

    banda(margen, "PARTES DE", entrada, GRIS, GRIS_CLARO)

    f.texto(90, inicio - 8, "QUÉ HAY QUE HACER", tam=10, color=SUAVE, peso="700")
    f.texto(716, inicio - 8, "QUÉ PRODUCE", tam=10, color=SUAVE, peso="700",
            anclaje="middle")

    for i, (que, fichero) in enumerate(pasos):
        y = inicio + i * fila_alto
        if i:                                     # hilo que une un paso con el anterior
            f.linea(58, y - 30, 58, y + 11, color=BORDE, guiones="3 4")
        f.circulo(58, y + 27, 15, relleno=AZUL_CLARO, borde=AZUL)
        f.texto(58, y + 32, str(i + 1), tam=13, anclaje="middle", peso="700", color=AZUL)
        f.texto(90, y + 32, que, tam=13.5, peso="500")
        f.etiqueta(556, y + 12, 320, 31, fichero, VERDE, VERDE_CLARO, tam=11.5)

    banda(inicio + len(pasos) * fila_alto + 14, "ENTREGAS", entrega, MORADO, MORADO_CLARO)
    return f


HITOS = {
    0: ("El fichero de jugadores del curso: 100.995 filas y 37 columnas", [
        ("Leer la página del conjunto de datos y describirlo", "docs/ficha_dataset.md"),
        ("Abrir el CSV con pathlib y csv", "lectura.py"),
        ("Inferir el tipo de cada columna", "tipos.py"),
        ("Contar vacíos, mínimos, máximos y frecuencias", "estadisticas.py"),
        ("Escribir el informe y registrar los fallos", "datos/informe_inicial.json"),
        ("Organizarlo como paquete ejecutable", "src/explorador/"),
    ], "Paquete instalable, informe generado, ficha del conjunto de datos y defensa"),

    1: ("El explorador del hito 0 y su informe_inicial.json", [
        ("Separar el código en módulos por responsabilidad", "src/tu_paquete/"),
        ("Hacer el paquete instalable", "pyproject.toml"),
        ("Llevar las opciones a una dataclass", "configuracion.py"),
        ("Leer las filas con un generador, dentro de with", "lectura.py"),
        ("Escribir cuatro pruebas", "tests/"),
        ("Regenerar el informe y comprobar que no cambia", "informe_inicial.json idéntico"),
    ], "Paquete instalado con pip install -e, pruebas en verde, README y defensa"),

    2: ("El paquete del hito 1, ya instalado", [
        ("Limpiar los datos de forma reproducible", "limpieza.py · *.parquet"),
        ("Explorar: seis gráficos con su explicación", "notebooks/03_exploracion.ipynb"),
        ("Construir el panel con filtros e indicadores", "app/app.py"),
        ("Publicarlo en Streamlit Community Cloud", "enlace en el README"),
    ], "Panel publicado, cinco hallazgos en el README y defensa de 5 minutos"),

    3: ("Los datos limpios en Parquet del hito 2", [
        ("Diseñar el esquema, con claves, tipos e índice", "esquema.sql"),
        ("Cargar los datos desde Python", "bd.py"),
        ("Seis consultas parametrizadas que respondan", "consultas.py"),
        ("Guardar una parte como documentos y comparar", "README: SQL frente a NoSQL"),
        ("Hacer que el panel lea de la base de datos", "app/app.py"),
    ], "Base de datos cargada, seis consultas, comparativa y panel desplegado"),

    4: ("Tus datos, ya en una base de datos", [
        ("Multiplicar los datos hasta dos millones de filas", "escalar.py"),
        ("Medir memoria y tiempo de la versión ingenua", "tabla de medidas"),
        ("Optimizar: tipos, columnas y Parquet", "datos/procesado/"),
        ("Procesar por trozos o en flujo", "flujo.py"),
        ("Escribir conclusiones, incluido el impacto social", "README"),
    ], "Script de escalado, medidas antes y después, conclusiones y defensa"),

    5: ("Los datos limpios y la pregunta del hito 0", [
        ("Plantear el problema y partir los datos", "modelo.py"),
        ("Pipeline, modelo de referencia y tres modelos", "tabla comparativa"),
        ("Ajustar los hiperparámetros con validación cruzada", "mejores parámetros"),
        ("Evaluar: métricas, grupos, importancia y curvas", "graficos/"),
        ("Guardar el modelo junto a sus métricas", "modelos/*.joblib · metricas.json"),
    ], "Modelo entrenado y guardado, ficha del modelo en el README y defensa"),

    6: ("Todo lo de las seis unidades anteriores", [
        ("Recoger el proyecto en un repositorio ordenado", "estructura final"),
        ("Una sola definición de cada cosa", "src/tu_paquete/"),
        ("Pruebas y versiones fijadas", "tests/ · requirements.txt"),
        ("La aplicación que usa el modelo guardado", "app/app.py"),
        ("Desplegar y comprobar en un equipo limpio", "enlace público"),
        ("README y ficha del modelo", "documentación"),
    ], "Aplicación publicada, Día en la Oficina y defensa oral de 10 minutos"),
}


def hito(numero: int) -> Figura:
    entrada, pasos, entrega = HITOS[numero]
    return ruta_del_hito(numero, entrada, pasos, entrega)


def main() -> None:
    figuras = {
        (1, "variables-etiquetas"): ud1_variables,
        (1, "estructuras-datos"): ud1_estructuras,
        (1, "alias-y-copia"): ud1_alias,
        (1, "traceback"): ud1_traceback,
        (2, "modelo-objetos"): ud2_modelo_objetos,
        (2, "herencia-mro"): ud2_mro,
        (2, "lista-vs-generador"): ud2_generadores,
        (2, "java-python"): ud2_java_python,
        (2, "contrato-doble"): ud2_contrato_doble,
        (3, "ciclo-del-dato"): ud3_ciclo,
        (3, "anatomia-dataframe"): ud3_dataframe,
        (3, "groupby"): ud3_groupby,
        (3, "merge"): ud3_merge,
        (4, "indice-scan-search"): ud4_indice,
        (4, "tabla-vs-documento"): ud4_tabla_documento,
        (4, "teorema-cap"): ud4_cap,
        (5, "csv-vs-parquet"): ud5_parquet,
        (5, "lectura-por-trozos"): ud5_trozos,
        (5, "map-reduce"): ud5_mapreduce,
        (6, "programar-vs-aprender"): ud6_flujo,
        (6, "pipeline-y-fuga"): ud6_pipeline,
        (6, "matriz-confusion"): ud6_confusion,
        (6, "sobreajuste"): ud6_sobreajuste,
        (7, "crisp-dm"): ud7_crispdm,
        (7, "arquitectura-proyecto"): ud7_arquitectura,
        (1, "hito-0"): lambda h=0: hito(h),
        (2, "hito-1"): lambda h=1: hito(h),
        (3, "hito-2"): lambda h=2: hito(h),
        (4, "hito-3"): lambda h=3: hito(h),
        (5, "hito-4"): lambda h=4: hito(h),
        (6, "hito-5"): lambda h=5: hito(h),
        (7, "hito-6"): lambda h=6: hito(h),
    }
    for (unidad, nombre), funcion in figuras.items():
        ruta = UNIDADES[unidad] / f"{nombre}.svg"
        funcion().guardar(ruta)
        print(f"{ruta.relative_to(RAIZ)}  ({ruta.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
