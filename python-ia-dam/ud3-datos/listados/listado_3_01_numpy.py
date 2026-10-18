"""NumPy: por qué pandas es rápido.

Un `array` de NumPy guarda muchos números del mismo tipo juntos en memoria y
opera sobre todos a la vez, sin bucle de Python. A eso se le llama
**vectorización**, y es la diferencia entre que un cálculo tarde un segundo o
cien.
"""

import time

import numpy as np

# Un array se crea desde una lista, pero por dentro no es una lista.
medias = np.array([94, 93, 91, 91, 89])
print("array:", medias, "· tipo de los datos:", medias.dtype)

# Las operaciones se aplican a todos los elementos a la vez.
print("\nmedias + 1:   ", medias + 1)
print("medias > 90:  ", medias > 90)
print("solo los > 90:", medias[medias > 90])     # máscara booleana

# Y las estadísticas vienen hechas.
print(f"\nmedia {medias.mean():.1f} · máximo {medias.max()} · desviación {medias.std():.2f}")

# La diferencia de velocidad, con dos millones de valoraciones inventadas.
valores = [float(v) for v in np.random.default_rng(42).integers(40, 95, 2_000_000)]
array = np.array(valores)


def cronometrar(tarea) -> tuple[float, float]:
    inicio = time.perf_counter()
    resultado = tarea()
    return (time.perf_counter() - inicio) * 1000, resultado


print("\nDos millones de valoraciones:")
for nombre, con_lista, con_array in (
    ("media", lambda: sum(valores) / len(valores), lambda: array.mean()),
    ("cuántas pasan de 85", lambda: sum(1 for v in valores if v > 85),
     lambda: int((array > 85).sum())),
):
    ms_lista, r1 = cronometrar(con_lista)
    ms_array, r2 = cronometrar(con_array)
    print(f"  {nombre:<20} lista {ms_lista:>6.1f} ms · NumPy {ms_array:>5.1f} ms "
          f"· {ms_lista / ms_array:>4.0f} veces más rápido")

print("\nLa ventaja depende de la operación, pero hay otra que no se mide en")
print("tiempo: con NumPy escribes `array.mean()` en lugar de un bucle, y eso")
print("es lo que hace legible el código de pandas que viene a continuación.")
