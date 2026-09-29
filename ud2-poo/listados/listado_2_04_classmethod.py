"""Listado 2.4. Constructores alternativos y métodos estáticos."""


class Venta:
    def __init__(self, ciudad: str, producto: str, unidades: int, precio: float):
        self.ciudad = ciudad
        self.producto = producto
        self.unidades = unidades
        self.precio = precio

    @classmethod
    def desde_fila_csv(cls, fila: dict) -> "Venta":
        """Crea una Venta a partir de una fila de csv.DictReader."""
        return cls(
            ciudad=fila["ciudad"],
            producto=fila["producto"],
            unidades=int(fila["unidades"]),
            precio=cls.a_float(fila["precio"]),
        )

    @staticmethod
    def a_float(texto: str) -> float:
        """Convierte un número en formato español ('1.234,56') en float."""
        return float(texto.replace(".", "").replace(",", "."))

    @property
    def importe(self) -> float:
        return round(self.unidades * self.precio, 2)


fila = {"ciudad": "Granada", "producto": "monitor", "unidades": "2", "precio": "180,00"}
venta = Venta.desde_fila_csv(fila)
print(venta.ciudad, venta.importe)      # Granada 360.0
print(Venta.a_float("1.180,00"))        # 1180.0: se llama sin crear objetos
