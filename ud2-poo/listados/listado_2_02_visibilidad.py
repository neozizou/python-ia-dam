"""Listado 2.2. No hay private: hay convenios."""


class Conexion:
    def __init__(self, servidor: str, clave: str):
        self.servidor = servidor       # público
        self._intentos = 0             # «no lo toques»: convenio
        self.__clave = clave           # name mangling: pasa a _Conexion__clave

    def mostrar_clave_oculta(self) -> str:
        return "*" * len(self.__clave)


c = Conexion("mariadb.local", "secreto")

print(c.servidor)               # mariadb.local
print(c._intentos)              # 0: Python te deja, pero no deberías
print(c.mostrar_clave_oculta())   # *******
# print(c.__clave)              # AttributeError
print(c._Conexion__clave)       # 'secreto': el mangling no es seguridad
