"""Listado 2.11. Una clase que se comporta como una colección."""


class Dataset:
    """Colección de filas (diccionarios) con la interfaz de una secuencia."""

    def __init__(self, filas: list[dict]):
        self._filas = filas

    def __len__(self) -> int:
        return len(self._filas)

    def __getitem__(self, indice):
        return self._filas[indice]          # admite índices y rebanadas

    def __iter__(self):
        return iter(self._filas)

    def __contains__(self, ciudad: str) -> bool:
        return any(f["ciudad"] == ciudad for f in self._filas)

    def __repr__(self) -> str:
        return f"Dataset({len(self)} filas)"


datos = Dataset([
    {"ciudad": "Granada", "importe": 2699.7},
    {"ciudad": "Málaga", "importe": 845.0},
    {"ciudad": "Sevilla", "importe": 899.9},
])

print(len(datos))                    # 3
print(datos[0]["ciudad"])            # Granada
print(datos[:2])                     # rebanada
print("Málaga" in datos)             # True
for fila in datos:                   # iterable en un for
    print(fila["ciudad"], end=" ")
print()
print(datos)                         # Dataset(3 filas)
