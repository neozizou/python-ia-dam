"""Listado 2.18. Un transformador con la interfaz de scikit-learn."""


class TransformadorBase:
    """Todo transformador aprende con fit y aplica con transform."""

    def fit(self, valores: list[float]) -> "TransformadorBase":
        raise NotImplementedError

    def transform(self, valores: list[float]) -> list[float]:
        raise NotImplementedError

    def fit_transform(self, valores: list[float]) -> list[float]:
        """Patrón plantilla: se escribe una vez y lo heredan todos."""
        return self.fit(valores).transform(valores)


class NormalizadorMinMax(TransformadorBase):
    """Lleva los valores al rango [0, 1] con el mínimo y el máximo aprendidos."""

    def fit(self, valores: list[float]) -> "NormalizadorMinMax":
        self.minimo_ = min(valores)          # el guion bajo final marca lo aprendido
        self.maximo_ = max(valores)
        return self                          # devolver self permite encadenar

    def transform(self, valores: list[float]) -> list[float]:
        recorrido = self.maximo_ - self.minimo_
        return [round((v - self.minimo_) / recorrido, 3) for v in valores]


importes = [845.0, 2699.7, 899.9, 3059.7]

normalizador = NormalizadorMinMax()
print(normalizador.fit_transform(importes))    # [0.0, 0.837, 0.025, 1.0]

# Lo aprendido se reutiliza con datos nuevos, sin volver a entrenar
print(normalizador.transform([1000.0]))        # [0.07]
