"""Listado 2.3. Encapsulación con @property."""


class Alumno:
    def __init__(self, nombre: str, nota: float):
        self.nombre = nombre
        self.nota = nota            # pasa por el setter, así que también valida

    @property
    def nota(self) -> float:
        """Nota entre 0 y 10."""
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if not 0 <= valor <= 10:
            raise ValueError(f"Nota fuera de rango: {valor}")
        self._nota = valor

    @property
    def calificacion(self) -> str:
        """Atributo calculado: no se almacena, se deduce de la nota."""
        if self._nota < 5:
            return "Insuficiente"
        if self._nota < 7:
            return "Bien"
        return "Notable o superior"


ana = Alumno("Ana", 6.5)
print(ana.nota, ana.calificacion)    # 6.5 Bien

ana.nota = 9.0                       # se usa como un atributo normal
print(ana.calificacion)              # Notable o superior

try:
    ana.nota = 11
except ValueError as e:
    print("Error:", e)               # Error: Nota fuera de rango: 11
