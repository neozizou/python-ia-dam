# UD2 · Programación orientada a objetos en Python

**Python aplicado a la Inteligencia Artificial** · 2.º DAM · Curso 2026-2027

[← Volver al índice del módulo](../README.md)

## Índice

- [Presentación de la unidad](#presentación-de-la-unidad)
- [2.1 Clases y objetos en Python](#21-clases-y-objetos-en-python)
- [2.2 Encapsulación: propiedades y métodos de clase](#22-encapsulación-propiedades-y-métodos-de-clase)
- [2.3 Herencia, polimorfismo y mixins](#23-herencia-polimorfismo-y-mixins)
- [2.4 Contratos: clases abstractas y protocolos](#24-contratos-clases-abstractas-y-protocolos)
- [2.5 El modelo de datos: métodos especiales, dataclasses y enumeraciones](#25-el-modelo-de-datos-métodos-especiales-dataclasses-y-enumeraciones)
- [2.6 Protocolos del lenguaje: generadores, gestores de contexto y decoradores](#26-protocolos-del-lenguaje-generadores-gestores-de-contexto-y-decoradores)
- [2.7 Diseño: composición frente a herencia](#27-diseño-composición-frente-a-herencia)
- [Ampliación](#ampliación)
- [Práctica de la unidad · Hito 1 del proyecto integrador](#práctica-de-la-unidad--hito-1-del-proyecto-integrador)
- [Resumen de la unidad](#resumen-de-la-unidad)
- [Bibliografía de la UD2](#bibliografía-de-la-ud2)

## Presentación de la unidad

Ya sabes qué es una clase: lo viste en C++ en 1.º. Esta unidad, de 5 horas, no repite la teoría de la orientación a objetos, sino que enseña **cómo la entiende Python**, que es bastante distinto: no hay `private`, los atributos se calculan con propiedades, la herencia múltiple es habitual y los objetos se integran en el lenguaje implementando métodos especiales.

Todo lo que aparece aquí reaparece en el resto del curso. Los generadores permiten procesar ficheros grandes en la UD5, los gestores de contexto abren y cierran conexiones a bases de datos en la UD4, los decoradores son la forma de trabajar de Streamlit y el patrón `fit`/`transform` es el corazón de scikit-learn en la UD6.

### Resultado de aprendizaje y criterios de evaluación

**RA1.** Implementa programas básicos en Python aplicados a la manipulación de datos.

| CE | Criterio de evaluación | Apartados |
| --- | --- | --- |
| 1a | Desarrolla programas en Python con variables, estructuras de control y funciones | 2.1, 2.2, 2.5 |
| 1b | Utiliza estructuras de datos para organizar la información | 2.5, 2.6 |
| 1e | Diseña, estructura y utiliza módulos y paquetes para organizar y reutilizar el código | 2.3, 2.4, 2.6, 2.7 |

La orientación a objetos no aparece de forma explícita en los criterios, pero es el medio para cumplir 1a y 1e, y la condición para entender las bibliotecas de los RA2 y RA3.

### Temporalización

| Sesión | Fecha | Horas | Contenidos |
| --- | --- | --- | --- |
| 1 | Lunes 05/10/2026 (2.ª hora) | 1 | 2.1 Clases y objetos |
| 2 | Martes 06/10/2026 | 1 | 2.2 Encapsulación |
| 3 | Martes 13/10/2026 | 1 | 2.3 Herencia y mixins · 2.4 Contratos |
| 4 | Lunes 19/10/2026 | 2 | 2.5 Modelo de datos · 2.6 Protocolos · 2.7 Diseño |

El lunes 12/10 es festivo. La práctica de la unidad se trabaja de forma autónoma y se entrega junto con el hito 1 del proyecto.

### Cómo usar esta carpeta

| Carpeta | Contenido |
| --- | --- |
| [`listados/`](listados/) | Los 18 listados de la unidad como ficheros `.py`, con los datos de ejemplo en `listados/datos/` |

Ejecuta los listados desde `ud2-poo/listados/`, con el entorno virtual activado:

```bash
cd ud2-poo/listados
python listado_2_08_abc.py
```

## 2.1 Clases y objetos en Python

Una clase se define con `class` y sus métodos reciben siempre como primer parámetro el objeto sobre el que se llaman, que por convenio se llama `self`. No hay fichero de cabecera, ni declaración de atributos: los atributos de instancia **nacen al asignarlos**, normalmente dentro de `__init__` ([The Python Tutorial](https://docs.python.org/3/tutorial/classes.html)).

**Listado 2.1.** Una clase mínima: atributos de instancia y de clase · [ver fichero](listados/listado_2_01_clase_alumno.py)

```python
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
print(ana.centro, luis.centro)           # C.E.S. DAM C.E.S. DAM
```

- `__init__` no es un constructor como el de C++: el objeto ya existe cuando se llama, y `__init__` solo lo inicializa.
- `self` es **explícito** en la definición, pero no se pasa al llamar: `ana.ha_aprobado()` equivale a `Alumno.ha_aprobado(ana)`.
- Un atributo de clase es único y compartido. Si escribes `ana.centro = "Otro"`, no cambias el de la clase: creas un atributo de instancia que lo tapa solo para `ana`.
- No hay destructor equivalente a `~Alumno()`. La memoria se libera sola; para liberar recursos se usan gestores de contexto (apartado 2.6).

> [!NOTE]
> **Desde C++.** En Python todo es un objeto, incluidas las clases, las funciones y los módulos. No existen `struct`, plantillas ni sobrecarga de métodos por tipo de parámetro: una clase tiene un solo `__init__`, y las variantes se resuelven con valores por defecto o con constructores alternativos (apartado 2.2).

### No existe `private`

Python no tiene modificadores de acceso. La visibilidad se expresa con convenios que el lenguaje no impone: un guion bajo inicial significa «uso interno, no lo toques». Dos guiones bajos activan el *name mangling*, que renombra el atributo para evitar colisiones en las subclases, pero tampoco lo oculta ([The Python Tutorial](https://docs.python.org/3/tutorial/classes.html#private-variables)).

**Listado 2.2.** No hay `private`: hay convenios · [ver fichero](listados/listado_2_02_visibilidad.py)

```python
class Conexion:
    def __init__(self, servidor: str, clave: str):
        self.servidor = servidor       # público
        self._intentos = 0             # «no lo toques»: convenio
        self.__clave = clave           # name mangling: pasa a _Conexion__clave

    def mostrar_clave_oculta(self) -> str:
        return "*" * len(self.__clave)


c = Conexion("mariadb.local", "secreto")

print(c._intentos)              # 0: Python te deja, pero no deberías
# print(c.__clave)              # AttributeError
print(c._Conexion__clave)       # 'secreto': el mangling no es seguridad
```

### Para practicar

1. Escribe la clase `Modulo` con `nombre`, `horas` y una lista de `notas`. Añade los métodos `añadir_nota(nota)` y `media()`.
2. Añade a `Alumno` un atributo de clase `total` que cuente cuántos objetos se han creado. Compruébalo creando tres alumnos.
3. (A) Traduce a Python esta clase de C++ y explica qué se pierde y qué se gana:

```cpp
class Punto {
private:
    double x, y;
public:
    Punto(double x, double y) : x(x), y(y) {}
    double distanciaAlOrigen() const;
};
```

## 2.2 Encapsulación: propiedades y métodos de clase

En C++ se escriben *getters* y *setters* para controlar el acceso. En Python eso se considera ruido: se empieza con atributos públicos y, si más adelante hace falta validar o calcular algo, se convierte el atributo en **propiedad** sin cambiar el código que ya lo usaba.

**Listado 2.3.** Encapsulación con `@property` · [ver fichero](listados/listado_2_03_property.py)

```python
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
ana.nota = 11                        # ValueError: Nota fuera de rango: 11
```

Fíjate en `calificacion`: una propiedad **sin setter** es un atributo de solo lectura que se calcula cada vez. Es el mismo mecanismo que usan pandas (`df.shape`) y scikit-learn.

### Métodos de clase y métodos estáticos

| Decorador | Primer parámetro | Para qué sirve |
| --- | --- | --- |
| *(ninguno)* | `self`, la instancia | Métodos normales, que usan los datos del objeto |
| `@classmethod` | `cls`, la clase | Constructores alternativos: crear objetos desde otro formato |
| `@staticmethod` | *(ninguno)* | Funciones auxiliares relacionadas con la clase, que no usan sus datos |

**Listado 2.4.** Constructores alternativos y métodos estáticos · [ver fichero](listados/listado_2_04_classmethod.py)

```python
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
print(venta.importe)                    # 360.0
```

Un `@classmethod` es la alternativa pythónica a la sobrecarga de constructores de C++: en lugar de varios `Venta(...)`, tienes `Venta.desde_fila_csv(...)`, `Venta.desde_json(...)`, y cada uno dice en su nombre lo que hace. Usa `cls(...)` y no `Venta(...)` para que siga funcionando en las subclases.

### Para practicar

1. Convierte `horas` de la clase `Modulo` en una propiedad que rechace valores negativos.
2. Añade a `Modulo` la propiedad de solo lectura `aprobados`, que devuelva cuántas notas llegan al 5.
3. Añade un `@classmethod` llamado `desde_texto` que cree un `Modulo` a partir de una cadena como `"Programación;192"`.
4. (A) Busca en la documentación de pandas tres propiedades de un `DataFrame` (por ejemplo, `shape`, `columns` y `dtypes`) y explica por qué son propiedades y no métodos.

## 2.3 Herencia, polimorfismo y mixins

La sintaxis es más corta que en C++ y no hay que declarar los métodos como virtuales: **todos** se pueden sobrescribir.

**Listado 2.5.** Herencia y `super()` · [ver fichero](listados/listado_2_05_herencia.py)

```python
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
```

- `super()` da acceso a la implementación de la clase padre, tanto en `__init__` como en cualquier otro método.
- `isinstance(objeto, Clase)` e `issubclass(A, B)` responden a las preguntas de parentesco.

### Polimorfismo sin herencia: *duck typing*

En C++ el polimorfismo exige una jerarquía común. En Python basta con que el objeto tenga el método que vas a llamar: «si camina como un pato y grazna como un pato, es un pato».

**Listado 2.6.** *Duck typing* · [ver fichero](listados/listado_2_06_duck_typing.py)

```python
class LectorCSV:
    def leer(self) -> list[dict]:
        return [{"ciudad": "Granada", "importe": 2699.7}]


class ApiSimulada:                 # no hereda de nada, pero sirve igual
    def leer(self) -> list[dict]:
        return [{"ciudad": "Sevilla", "importe": 899.9}]


def cargar(origen) -> list[dict]:
    """Funciona con cualquier objeto que tenga un método leer()."""
    return origen.leer()
```

Esto explica por qué en la UD6 podrás cambiar `LinearRegression()` por `RandomForestRegressor()` sin tocar el resto del programa: todos los modelos de scikit-learn tienen `fit` y `predict`.

### Herencia múltiple, MRO y mixins

Python permite heredar de varias clases. Para evitar ambigüedades, calcula el **MRO** (*Method Resolution Order*), el orden en que busca cada atributo ([The Python Tutorial](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)). El uso más frecuente son los **mixins**: clases pequeñas que aportan una capacidad concreta y no se usan solas.

**Listado 2.7.** Herencia múltiple, mixins y MRO · [ver fichero](listados/listado_2_07_mixin_mro.py)

```python
import json


class ExportableJSONMixin:
    """Añade exportación a JSON a cualquier clase con __dict__."""

    def a_json(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False)


class Registrable:
    def describir(self) -> str:
        return f"{type(self).__name__} con {len(self.__dict__)} atributos"


class Venta(ExportableJSONMixin, Registrable):
    def __init__(self, ciudad: str, importe: float):
        self.ciudad = ciudad
        self.importe = importe


v = Venta("Granada", 3059.7)
print(v.a_json())          # {"ciudad": "Granada", "importe": 3059.7}
print(Venta.__mro__)       # Venta -> ExportableJSONMixin -> Registrable -> object
```

> [!TIP]
> Un mixin se nombra con el sufijo `Mixin`, no define `__init__` y resuelve una sola cosa. scikit-learn está construido así: sus transformadores heredan de `BaseEstimator` y de `TransformerMixin`, que es quien les regala el método `fit_transform`.

### Para practicar

1. Crea `Vehiculo` con `matricula` y `ruedas`, y las subclases `Coche` y `Moto`. Sobrescribe un método `describir()` en cada una.
2. Escribe una función que reciba una lista de objetos cualesquiera con método `describir()` y los imprima. Comprueba que funciona con clases sin parentesco.
3. Escribe un mixin `ComparablePorImporteMixin` que añada el método `mas_caro_que(otro)`.
4. (A) Ejecuta el listado 2.7 y explica el MRO que imprime. ¿Qué pasaría si las dos clases padre tuvieran un método con el mismo nombre?

## 2.4 Contratos: clases abstractas y protocolos

Cuando varias clases deben ofrecer la misma interfaz, conviene escribirlo en el código. Python tiene dos formas de hacerlo.

### Clases abstractas (`abc`)

Una clase que hereda de `ABC` y marca métodos con `@abstractmethod` **no se puede instanciar**, y obliga a sus subclases a implementarlos. Es el equivalente a una clase con métodos virtuales puros en C++ ([docs.python.org, abc](https://docs.python.org/3/library/abc.html)).

**Listado 2.8.** El contrato de un lector de datos · [ver fichero](listados/listado_2_08_abc.py)

```python
from abc import ABC, abstractmethod


class Lector(ABC):
    """Contrato común: todo lector sabe leer y devolver filas."""

    def __init__(self, ruta: Path):
        self.ruta = ruta

    @abstractmethod
    def leer(self) -> list[dict]:
        """Devuelve las filas del fichero como lista de diccionarios."""

    def resumen(self) -> str:                 # método concreto heredado por todos
        return f"{self.ruta.name}: {len(self.leer())} filas"


class LectorCSV(Lector):
    def __init__(self, ruta: Path, delimitador: str = ";"):
        super().__init__(ruta)
        self.delimitador = delimitador

    def leer(self) -> list[dict]:
        with self.ruta.open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f, delimiter=self.delimitador))
```

Al intentar `Lector(ruta)` Python responde:

```text
TypeError: Can't instantiate abstract class Lector without an implementation for abstract method 'leer'
```

Una clase abstracta puede mezclar métodos abstractos, que cada subclase escribe, y métodos concretos como `resumen()`, que todas heredan. Ese reparto es el patrón plantilla, y lo verás otra vez en el listado 2.18.

### Protocolos (`typing.Protocol`)

Un protocolo describe la interfaz **sin herencia**: cualquier clase que tenga esos métodos encaja. Es el *duck typing* puesto por escrito para que el editor pueda comprobarlo ([docs.python.org, typing](https://docs.python.org/3/library/typing.html#typing.Protocol)).

**Listado 2.9.** `typing.Protocol` · [ver fichero](listados/listado_2_09_protocol.py)

```python
from typing import Protocol


class Leible(Protocol):
    """Cualquier objeto con este método encaja, herede o no de aquí."""

    def leer(self) -> list[dict]: ...


class LectorMemoria:                       # no hereda de Leible
    def leer(self) -> list[dict]:
        return [{"ciudad": "Granada", "importe": 2699.7}]


def cargar(origen: Leible) -> int:
    """El editor avisa si le pasas algo sin método leer()."""
    return len(origen.leer())
```

| Usa… | Cuando… |
| --- | --- |
| Clase abstracta | Las clases son tuyas, comparten código y quieres obligar a implementar métodos |
| `Protocol` | Solo te importa la forma del objeto, y puede venir de otra biblioteca |

### Para practicar

1. Añade `LectorJSON` a la jerarquía del listado 2.8 y comprueba que `resumen()` funciona sin escribirlo de nuevo.
2. Crea una clase abstracta `Exportador` con el método abstracto `exportar(datos, ruta)` e impleméntala para CSV y para JSON.
3. (A) Escribe un `Protocol` llamado `Modelo` con `fit(x, y)` y `predict(x)`, y una clase que lo cumpla sin heredar de él. Explica qué relación tiene con scikit-learn.

## 2.5 El modelo de datos: métodos especiales, dataclasses y enumeraciones

Los **métodos especiales** o *dunder* (por *double underscore*) conectan tus objetos con la sintaxis del lenguaje: `print`, `+`, `==`, `len()`, `for`, `in`. No se llaman directamente; Python los llama por ti ([docs.python.org, Data model](https://docs.python.org/3/reference/datamodel.html#special-method-names)).

| Método | Lo invoca… | Equivalente en C++ |
| --- | --- | --- |
| `__init__` | Crear el objeto | Constructor |
| `__repr__` | `repr(obj)`, la consola | — |
| `__str__` | `print(obj)`, `str(obj)` | `operator<<` |
| `__eq__`, `__lt__` | `==`, `<`, `sorted` | `operator==`, `operator<` |
| `__add__` | `+` | `operator+` |
| `__len__` | `len(obj)` | `size()` |
| `__getitem__` | `obj[i]` | `operator[]` |
| `__iter__` | `for x in obj` | Iteradores |
| `__contains__` | `x in obj` | — |
| `__call__` | `obj(...)` | `operator()` |

**Listado 2.10.** Que tus objetos se comporten como los nativos · [ver fichero](listados/listado_2_10_dunder_dinero.py)

```python
from functools import total_ordering


@total_ordering                      # genera <=, >, >= a partir de __eq__ y __lt__
class Importe:
    def __init__(self, euros: float):
        self.euros = round(euros, 2)

    def __repr__(self) -> str:       # para el programador (depuración)
        return f"Importe({self.euros})"

    def __str__(self) -> str:        # para el usuario (print)
        return f"{self.euros:.2f} €"

    def __eq__(self, otro) -> bool:
        return isinstance(otro, Importe) and self.euros == otro.euros

    def __lt__(self, otro) -> bool:
        return self.euros < otro.euros

    def __add__(self, otro) -> "Importe":
        return Importe(self.euros + otro.euros)


print(Importe(899.90) + Importe(180.00))     # 1079.90 €
print(sorted([Importe(899.9), Importe(180.0)]))   # [Importe(180.0), Importe(899.9)]
```

**Listado 2.11.** Una clase que se comporta como una colección · [ver fichero](listados/listado_2_11_coleccion.py)

```python
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
```

Con esos cuatro métodos, `Dataset` ya admite `len(datos)`, `datos[0]`, `datos[:2]`, `for fila in datos` y `"Málaga" in datos`. Es exactamente la sensación que da un `DataFrame` de pandas: se comporta como una colección del lenguaje porque implementa estos métodos.

### `dataclasses`: clases de datos sin código repetitivo

Muchas clases solo agrupan datos. El decorador `@dataclass` genera por ti `__init__`, `__repr__` y `__eq__` a partir de las anotaciones de tipo ([docs.python.org, dataclasses](https://docs.python.org/3/library/dataclasses.html)).

**Listado 2.12.** `dataclasses` · [ver fichero](listados/listado_2_12_dataclass.py)

```python
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
print(v1)             # Venta(ciudad='Granada', producto='portátil', unidades=3, …)
print(asdict(v1))     # dict listo para json.dump
```

- `order=True` genera además las comparaciones, que ordenan campo por campo.
- `frozen=True` crea objetos inmutables, que pueden usarse como claves de un diccionario.
- `field(default_factory=list)` es la solución correcta a la trampa del listado 1.20: cada objeto recibe su propia lista.

### Enumeraciones

Cuando un valor solo puede tomar unos pocos valores fijos, una enumeración evita las cadenas sueltas y los errores de escritura ([docs.python.org, enum](https://docs.python.org/3/library/enum.html)).

**Listado 2.13.** Enumeraciones · [ver fichero](listados/listado_2_13_enum.py)

```python
from enum import Enum


class Estado(Enum):
    MATRICULADO = "matriculado"
    APROBADO = "aprobado"
    SUSPENSO = "suspenso"


estado = Estado.APROBADO
print(estado.name, estado.value)      # APROBADO aprobado
print(Estado("suspenso"))             # Estado.SUSPENSO: desde el valor
```

### Para practicar

1. Añade a `Importe` el método `__sub__` y comprueba que `Importe(10) - Importe(3)` funciona.
2. Reescribe la clase `Venta` del listado 2.4 como `dataclass` y comprueba que el resultado es equivalente.
3. Amplía `Dataset` con un método `filtrar(ciudad)` que devuelva otro `Dataset`, y comprueba que se puede encadenar.
4. (A) Explica la diferencia entre `__str__` y `__repr__` con un ejemplo en el que ambos devuelvan cosas distintas. ¿Cuál se usa dentro de una lista?

## 2.6 Protocolos del lenguaje: generadores, gestores de contexto y decoradores

Tres mecanismos que ya has usado sin saber cómo funcionaban y que ahora vas a escribir tú.

### Generadores

Una función con `yield` no devuelve un valor: devuelve un **generador**, que produce los valores de uno en uno y solo cuando se le piden. Es la base del procesamiento de ficheros grandes, porque no carga nada en memoria.

**Listado 2.14.** Iteradores y generadores · [ver fichero](listados/listado_2_14_generadores.py)

```python
import csv
from pathlib import Path
from typing import Iterator


def filas_csv(ruta: Path) -> Iterator[dict]:
    """Devuelve las filas de una en una; no carga el fichero entero."""
    with ruta.open(encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            yield fila          # yield: entrega un valor y espera al siguiente next()


generador = filas_csv(Path("datos") / "ventas.csv")
print(next(generador)["ciudad"])          # Granada: solo se ha leído una línea

# Expresión generadora: como una comprensión, pero perezosa
unidades = (f["unidades"] for f in filas_csv(ruta) if f["unidades"])
print(sum(int(u) for u in unidades))      # 19
```

> [!TIP]
> La diferencia entre `[f for f in filas]` y `(f for f in filas)` es enorme con ficheros grandes: los corchetes construyen la lista completa en memoria; los paréntesis no construyen nada hasta que recorres el resultado. En la UD5 usaremos esta idea para tratar volúmenes que no caben en el ordenador.

### Gestores de contexto

`with` funciona con cualquier objeto que implemente `__enter__` y `__exit__`. Es el equivalente de RAII en C++: garantiza que la liberación ocurre aunque salte una excepción ([docs.python.org, contextlib](https://docs.python.org/3/library/contextlib.html)).

**Listado 2.15.** `with` para tus propios objetos · [ver fichero](listados/listado_2_15_context_manager.py)

```python
import time
from contextlib import contextmanager


class Cronometro:
    """Mide el tiempo de un bloque with."""

    def __init__(self, etiqueta: str):
        self.etiqueta = etiqueta

    def __enter__(self) -> "Cronometro":
        self.inicio = time.perf_counter()
        return self                      # lo que recibe la variable tras «as»

    def __exit__(self, tipo_exc, valor_exc, traza) -> bool:
        self.segundos = time.perf_counter() - self.inicio
        print(f"{self.etiqueta}: {self.segundos:.4f} s")
        return False                     # False: si hubo excepción, se propaga


with Cronometro("suma de un millón de enteros"):
    total = sum(range(1_000_000))


@contextmanager                          # la versión corta, con un generador
def cronometro(etiqueta: str):
    inicio = time.perf_counter()
    try:
        yield                            # aquí se ejecuta el cuerpo del with
    finally:
        print(f"{etiqueta}: {time.perf_counter() - inicio:.4f} s")
```

En la UD4 usarás esto mismo para abrir y cerrar conexiones a MariaDB sin dejar conexiones colgadas.

### Decoradores

Un decorador es una función que recibe otra función y devuelve una versión envuelta. `@medir` encima de una función equivale a `funcion = medir(funcion)`. `functools.wraps` conserva el nombre y el docstring del original ([docs.python.org, functools](https://docs.python.org/3/library/functools.html#functools.wraps)).

**Listado 2.16.** Escribir un decorador · [ver fichero](listados/listado_2_16_decoradores.py)

```python
import functools
import time


def medir(func):
    """Decorador que muestra cuánto tarda la función."""

    @functools.wraps(func)               # conserva nombre y docstring del original
    def envoltorio(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.perf_counter() - inicio:.4f} s")
        return resultado

    return envoltorio


@medir                      # equivale a: suma_cuadrados = medir(suma_cuadrados)
def suma_cuadrados(n: int) -> int:
    """Suma los cuadrados de los n primeros enteros."""
    return sum(i * i for i in range(n))
```

Ya conoces varios decoradores: `@property`, `@classmethod`, `@staticmethod`, `@dataclass` y `@contextmanager`. En la UD3, Streamlit usará `@st.cache_data` para no recalcular un análisis en cada recarga de la página, y funciona exactamente así.

### Para practicar

1. Escribe un generador `lineas_no_vacias(ruta)` que entregue solo las líneas con contenido de un fichero de texto.
2. Convierte el `Cronometro` en un gestor de contexto que, además, guarde el tiempo en un fichero de registro.
3. Escribe un decorador `@reintentar(veces=3)` que vuelva a llamar a la función si lanza una excepción. Pista: necesitas una función que devuelva el decorador.
4. (A) Compara el consumo de memoria de `sum([i * i for i in range(10_000_000)])` y `sum(i * i for i in range(10_000_000))`. Explica la diferencia.

## 2.7 Diseño: composición frente a herencia

La herencia crea una dependencia fuerte: si cambia la clase padre, cambian todas las hijas. La **composición** —que un objeto contenga a otros y les delegue trabajo— suele ser más flexible. La regla práctica: hereda cuando la subclase **es** una variante del padre; compón cuando el objeto simplemente **usa** a otro.

**Listado 2.17.** Composición · [ver fichero](listados/listado_2_17_composicion.py)

```python
class Informe:
    """No hereda de LectorCSV ni de Calculadora: los USA."""

    def __init__(self, lector: LectorCSV, calculadora: Calculadora):
        self.lector = lector
        self.calculadora = calculadora

    def unidades_por_ciudad(self) -> dict[str, float]:
        filas = self.lector.leer()
        return self.calculadora.total_por_clave(filas, "ciudad", "unidades")


informe = Informe(LectorCSV(Path("datos") / "ventas.csv"), Calculadora())
print(informe.unidades_por_ciudad())     # {'Granada': 5.0, 'Málaga': 14.0}
```

Pasar los colaboradores por el constructor permite cambiarlos sin tocar `Informe`: para leer JSON basta con darle otro lector. En la UD6, un `Pipeline` de scikit-learn hace justo esto con una lista de transformadores.

### Cómo están diseñadas las bibliotecas que vas a usar

El siguiente listado reúne casi todo lo de la unidad: una clase base que define el contrato y escribe el método común, una subclase que lo implementa, y el convenio de scikit-learn de guardar lo aprendido en atributos terminados en guion bajo ([scikit-learn, Developing estimators](https://scikit-learn.org/stable/developers/develop.html)).

**Listado 2.18.** Un transformador con la interfaz de scikit-learn · [ver fichero](listados/listado_2_18_transformador.py)

```python
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


normalizador = NormalizadorMinMax()
print(normalizador.fit_transform([845.0, 2699.7, 899.9, 3059.7]))   # [0.0, 0.837, 0.025, 1.0]
print(normalizador.transform([1000.0]))                             # [0.07]
```

Que `fit` devuelva `self` es lo que permite escribir `modelo.fit(X, y).predict(X_nuevo)`. Y separar `fit` de `transform` es lo que evita la fuga de datos que estudiaremos en la UD6: lo aprendido con los datos de entrenamiento se aplica después a los de prueba.

### Para practicar

1. Reescribe el listado 2.17 para que `Informe` acepte cualquier objeto con método `leer()`, y pásale un lector de JSON.
2. Añade `EstandarizadorZ`, que reste la media y divida por la desviación típica. Pista: `statistics.mean` y `statistics.pstdev`.
3. (A) Busca en la documentación de scikit-learn qué métodos exige a un transformador y compáralos con el listado 2.18.

## Ampliación

Estos tres mecanismos no entran en la evaluación, pero aparecen al leer código de bibliotecas.

- **Descriptores.** Son la maquinaria que hay debajo de `@property`, `@classmethod` y los campos de un ORM: clases que definen `__get__`, `__set__` o `__delete__` y controlan el acceso a un atributo de otra clase.
- **`__slots__`.** Declarar `__slots__ = ("ciudad", "importe")` impide crear atributos nuevos y ahorra memoria al no guardar el `__dict__` de cada objeto. Se usa cuando hay millones de instancias.
- **Metaclases.** Una metaclase es la clase de una clase: permite modificar las clases cuando se definen. Es la herramienta con la que están hechos los modelos de Django o de Pydantic. La regla habitual: si dudas de si necesitas una metaclase, no la necesitas.

## Práctica de la unidad · Hito 1 del proyecto integrador

Vas a **refactorizar** el explorador del hito 0: mismo resultado, mejor diseño. Es el trabajo real de un programador que recibe código que funciona y tiene que dejarlo mantenible.

### 1. Punto de partida

Tu paquete `explorador` de la UD1, con su `informe_inicial.json` ya generado. Ese fichero es tu prueba: al terminar el refactor, el programa debe producir **exactamente el mismo JSON**.

### 2. Qué hay que construir

| Elemento | Requisito |
| --- | --- |
| `Lector` | Clase abstracta (`ABC`) con el método abstracto `leer()`, y las subclases `LectorCSV` y `LectorJSON` |
| `Columna` | Clase con el nombre, los valores y propiedades de solo lectura: `vacios`, `porcentaje_vacios`, `tipo` y, si es numérica, `minimo`, `maximo` y `media` |
| `Dataset` | Colección de filas con `__len__`, `__getitem__`, `__iter__` y `__repr__`, y un método `informe()` que devuelva el diccionario del informe |
| `ResumenColumna` | `dataclass` con los datos de cada columna, convertida a diccionario con `asdict` |
| Generador | La lectura de filas debe hacerse con `yield`, sin cargar el fichero entero |
| Gestor de contexto | Abrir el fichero dentro de un `with`, propio o el de `open` |
| Decorador | `@medir` aplicado al método que genera el informe, que registre el tiempo con `logging` |

### 3. Entregables

- El paquete refactorizado en `src/explorador/`, con los módulos separados por responsabilidad.
- `datos/informe_inicial.json` regenerado y **idéntico** al de la UD1. Incluye en el `README.md` cómo lo has comprobado.
- Un apartado en el `README.md` de tres a cinco líneas: qué decisiones de diseño has tomado y por qué elegiste herencia o composición en cada caso.
- Defensa oral breve (5 minutos): justificar una clase y explicar qué pasaría si se cambiara el formato de entrada.

### 4. Qué se evalúa

| CE | Evidencias en la práctica |
| --- | --- |
| 1a | Clases con responsabilidad única, propiedades en lugar de getters y validación de datos |
| 1b | Uso adecuado de `dataclass`, diccionarios y colecciones propias para organizar la información |
| 1e | Paquete reorganizado por responsabilidades, contrato explícito con `ABC` y reutilización sin duplicar código |

## Resumen de la unidad

| Apartado | Idea clave |
| --- | --- |
| 2.1 Clases y objetos | `self` es explícito, los atributos nacen al asignarlos y no hay `private`: hay convenios `_` y `__` |
| 2.2 Encapsulación | Atributos públicos hasta que hagan falta propiedades. `@classmethod` sustituye a la sobrecarga de constructores |
| 2.3 Herencia y mixins | Todos los métodos son sobrescribibles. El *duck typing* permite polimorfismo sin jerarquía, y los mixins añaden capacidades sueltas |
| 2.4 Contratos | `ABC` obliga a implementar métodos; `Protocol` describe la forma del objeto sin herencia |
| 2.5 Modelo de datos | Los métodos especiales integran tus objetos en el lenguaje. `dataclass` escribe por ti `__init__`, `__repr__` y `__eq__` |
| 2.6 Protocolos | `yield` procesa sin cargar en memoria, `__enter__`/`__exit__` garantizan la liberación y un decorador envuelve una función sin tocarla |
| 2.7 Diseño | Hereda si **es**; compón si **usa**. `fit`/`transform` y devolver `self` son el patrón de scikit-learn |

## Bibliografía de la UD2

Todas las fuentes web se consultaron el 21 de septiembre de 2026.

### Documentación oficial de Python

- Python Software Foundation. (2026). *The Python Tutorial, capítulo 9: Classes*. <https://docs.python.org/3/tutorial/classes.html>. Apartados citados: [9.6 Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables) y [9.5.1 Multiple Inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance).
- Python Software Foundation. (2026). *The Python Language Reference: Special method names*. <https://docs.python.org/3/reference/datamodel.html#special-method-names>
- Python Software Foundation. (2026). *dataclasses — Data Classes*. <https://docs.python.org/3/library/dataclasses.html>
- Python Software Foundation. (2026). *abc — Abstract Base Classes*. <https://docs.python.org/3/library/abc.html>
- Python Software Foundation. (2026). *typing.Protocol*. <https://docs.python.org/3/library/typing.html#typing.Protocol>
- Python Software Foundation. (2026). *enum — Support for enumerations*. <https://docs.python.org/3/library/enum.html>
- Python Software Foundation. (2026). *contextlib — Utilities for with-statement contexts*. <https://docs.python.org/3/library/contextlib.html>
- Python Software Foundation. (2026). *functools.wraps*. <https://docs.python.org/3/library/functools.html#functools.wraps>

### Bibliotecas del curso

- scikit-learn developers. *Developing scikit-learn estimators*. <https://scikit-learn.org/stable/developers/develop.html>

### Lectura complementaria

- Vadillo, J. *Aprende Python desde cero a experto*. Licencia CC BY-NC-SA 4.0. <https://github.com/jvadillo/aprende-python-desde-cero-a-experto>. Capítulo 9 (Clases y objetos) para los apartados 2.1 y 2.2, y capítulo 10 (Herencia) para el 2.3.
