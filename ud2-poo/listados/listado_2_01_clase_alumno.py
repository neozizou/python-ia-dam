"""Listado 2.1. Una clase mínima: atributos de instancia y de clase."""


class Alumno:
    """Representa a un alumno matriculado en un ciclo."""

    centro = "C.E.S. DAM"          # atributo de CLASE: compartido por todas las instancias

    def __init__(self, nombre: str, nota: float):
        self.nombre = nombre       # atributos de INSTANCIA: uno por objeto
        self.nota = nota

    def ha_aprobado(self) -> bool:
        """Indica si la nota llega al 5."""
        return self.nota >= 5


ana = Alumno("Ana", 6.5)
luis = Alumno("Luis", 4.0)

print(ana.nombre, ana.ha_aprobado())     # Ana True
print(luis.nombre, luis.ha_aprobado())   # Luis False
print(ana.centro, luis.centro)           # C.E.S. DAM C.E.S. DAM
print(type(ana))                         # <class '__main__.Alumno'>
