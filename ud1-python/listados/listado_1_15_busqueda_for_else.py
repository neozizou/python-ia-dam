"""Listado 1.15. La cláusula else de un bucle: terminar sin encontrar nada.

El `else` de un `for` se ejecuta cuando el bucle termina **sin** pasar por un
`break`. Sirve justo para esto: buscar algo y reaccionar si no aparece, sin
tener que llevar una variable «encontrado» a mano.
"""

PLANTILLA = [
    ("L. Messi", "RW, CF, ST"),
    ("Sergio Ramos", "CB"),
    ("J. Oblak", "GK"),
    ("K. De Bruyne", "CAM, CM"),
]

for nombre, posiciones in PLANTILLA:
    for posicion in posiciones.split(","):
        if posicion.strip() == "GK":
            print(f"{nombre:<14} es portero")
            break                    # encontrado: salimos del bucle interno
    else:
        print(f"{nombre:<14} juega de campo")   # el for terminó sin break
