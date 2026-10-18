"""Listado 1.11. Encadenar condiciones con if / elif / else."""

media = 87

if media < 0 or media > 99:
    nivel = "Valoración no válida"
elif media < 60:
    nivel = "Reserva"
elif media < 70:
    nivel = "Suplente"
elif media < 80:
    nivel = "Titular"
elif media < 90:
    nivel = "Estrella"
else:
    nivel = "Clase mundial"

print(f"Media {media}: {nivel}")       # Media 87: Estrella

# La misma idea en una línea, cuando solo hay dos casos.
titular = "sí" if media >= 70 else "no"
print("¿Es titular?", titular)         # ¿Es titular? sí
