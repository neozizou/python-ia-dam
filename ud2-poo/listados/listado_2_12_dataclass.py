"""Listado 2.12. dataclasses: clases de datos sin código repetitivo."""

from dataclasses import asdict, dataclass, field


@dataclass(order=True)
class Venta:
    ciudad: str
    producto: str
    unidades: int
    precio: float
    etiquetas: list[str] = field(default_factory=list)   # nunca una lista literal

    @property
    def importe(self) -> float:
        return round(self.unidades * self.precio, 2)


v1 = Venta("Granada", "portátil", 3, 899.90)
v2 = Venta("Granada", "portátil", 3, 899.90)

print(v1)                    # __repr__ automático
print(v1 == v2)              # True: __eq__ automático compara los campos
print(v1.importe)            # 2699.7
print(asdict(v1))            # dict listo para json.dump

# @dataclass(frozen=True) crea objetos inmutables, válidos como claves de dict
