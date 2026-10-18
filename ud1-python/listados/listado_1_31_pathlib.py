"""Encontrar el fichero de datos esté donde esté la carpeta del proyecto.

El error más repetido al empezar es `FileNotFoundError` por escribir una ruta
relativa a la carpeta desde la que se ejecuta el programa, que no siempre es la
que uno cree. `pathlib` lo resuelve: se parte del fichero de código, cuya
posición sí es fija, y se navega desde ahí.
"""

from pathlib import Path

# __file__ es la ruta de este mismo fichero .py.
AQUI = Path(__file__).resolve()
print("Este fichero:", AQUI.name)
print("Su carpeta:  ", AQUI.parent.name)

# .parents son las carpetas que lo contienen, de dentro hacia fuera.
for nivel, carpeta in enumerate(AQUI.parents[:3]):
    print(f"  parents[{nivel}] = {carpeta.name or '/'}")

# Desde listados/ hay que subir dos niveles para llegar a la raíz del repositorio.
RAIZ = AQUI.parents[2]
DATOS = RAIZ / "datos-comunes" / "jugadores.csv"      # la barra une rutas

print("\nRuta construida:", DATOS.relative_to(RAIZ))
print("¿Existe?        ", DATOS.exists())
print("Tamaño:          ", f"{DATOS.stat().st_size / 1024 / 1024:.1f} MB")

# Partes de una ruta, sin trocear cadenas a mano.
print("\nNombre:    ", DATOS.name)
print("Sin extensión:", DATOS.stem)
print("Extensión: ", DATOS.suffix)

# Construir rutas hermanas es trivial, y funciona igual en Windows y en macOS.
print("\nSi guardáramos un informe al lado:", DATOS.with_name("informe.json").name)

# Los ficheros pequeños se leen enteros de una vez.
MUESTRA = AQUI.parent / "datos" / "jugadores_muestra.csv"
primera, segunda, *resto = MUESTRA.read_text(encoding="utf-8").splitlines()
print("\nCabecera de la muestra:", primera)
print("Primer jugador:        ", segunda)
print("Jugadores en la muestra:", len(resto) + 1)
