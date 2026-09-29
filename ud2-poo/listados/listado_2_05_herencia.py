"""Listado 2.5. Herencia y super()."""


class Persona:
    def __init__(self, nombre: str, dni: str):
        self.nombre = nombre
        self.dni = dni

    def presentarse(self) -> str:
        return f"Soy {self.nombre}"


class Alumno(Persona):
    def __init__(self, nombre: str, dni: str, ciclo: str):
        super().__init__(nombre, dni)     # llama al __init__ de Persona
        self.ciclo = ciclo

    def presentarse(self) -> str:         # sobrescribe el método
        return f"{super().presentarse()} y estudio {self.ciclo}"


class Profesor(Persona):
    def __init__(self, nombre: str, dni: str, modulo: str):
        super().__init__(nombre, dni)
        self.modulo = modulo

    def presentarse(self) -> str:
        return f"{super().presentarse()} e imparto {self.modulo}"


personas = [
    Alumno("Ana", "00000000A", "DAM"),
    Profesor("Jaime", "00000000B", "Python aplicado a la IA"),
]

for p in personas:                        # polimorfismo: cada uno responde a su manera
    print(p.presentarse())

print(isinstance(personas[0], Persona))   # True
print(issubclass(Alumno, Persona))        # True
