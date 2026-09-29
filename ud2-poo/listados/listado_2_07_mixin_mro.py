"""Listado 2.7. Herencia múltiple, mixins y MRO."""

import json


class ExportableJSONMixin:
    """Añade exportación a JSON a cualquier clase con __dict__."""

    def a_json(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)


class Registrable:
    """Añade un mensaje de registro."""

    def describir(self) -> str:
        return f"{type(self).__name__} con {len(self.__dict__)} atributos"


class Venta(ExportableJSONMixin, Registrable):
    def __init__(self, ciudad: str, importe: float):
        self.ciudad = ciudad
        self.importe = importe


v = Venta("Granada", 3059.7)
print(v.a_json())                     # {"ciudad": "Granada", "importe": 3059.7}
print(v.describir())                  # Venta con 2 atributos

# Orden de resolución de métodos: dónde busca Python cada nombre
for clase in Venta.__mro__:
    print(clase.__name__, end=" -> ")
print("fin")
