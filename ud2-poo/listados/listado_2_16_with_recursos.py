"""`with`: lo que se abre, se cierra, pase lo que pase.

Es el equivalente del try-with-resources de Java, y lo vas a usar en todas las
unidades: ficheros en la UD3, conexiones en la UD4, lecturas por trozos en la UD5.
"""

import sqlite3
from pathlib import Path

RUTA = Path("datos/prueba_with.txt")
RUTA.parent.mkdir(parents=True, exist_ok=True)

# Sin with: hay que acordarse de cerrar, y si algo falla antes, no se cierra.
fichero = RUTA.open("w", encoding="utf-8")
fichero.write("primera línea\n")
fichero.close()
print("¿Cerrado a mano?", fichero.closed)

# Con with: se cierra al salir del bloque, también si salta una excepción.
try:
    with RUTA.open("a", encoding="utf-8") as f:
        f.write("segunda línea\n")
        raise RuntimeError("algo ha ido mal a mitad de la escritura")
except RuntimeError as error:
    print("Excepción:", error)
print("¿Cerrado por el with?", f.closed)
print("Contenido:", RUTA.read_text(encoding="utf-8").split())

# El mismo patrón con una conexión a una base de datos (UD4).
with sqlite3.connect(":memory:") as conexion:
    conexion.execute("CREATE TABLE producto (codigo TEXT, nombre TEXT)")
    conexion.execute("INSERT INTO producto VALUES ('T-100', 'Teclado mecánico')")
    print("\nFilas:", conexion.execute("SELECT * FROM producto").fetchall())

RUTA.unlink()
