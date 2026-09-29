"""Listado 4.7. SQLAlchemy: el mismo código para SQLite y para MariaDB."""

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text

# La URL describe el motor, el controlador, las credenciales y la base de datos
URL_SQLITE = f"sqlite:///{Path('datos') / 'ventas.db'}"

# En un servidor real sería algo así (nunca con la contraseña escrita en el código):
#   URL_MARIADB = (
#       f"mariadb+mariadbconnector://{os.environ['BD_USUARIO']}:"
#       f"{os.environ['BD_CLAVE']}@servidor:3306/ventas"
#   )
url = os.environ.get("BD_URL", URL_SQLITE)

motor = create_engine(url)

with motor.connect() as conexion:
    total = conexion.execute(
        text("SELECT COUNT(*) FROM venta WHERE ciudad = :ciudad"),
        {"ciudad": "Granada"},
    ).scalar()
    print(f"Granada: {total} ventas")

# pandas acepta el motor igual que una conexión de sqlite3
top = pd.read_sql(
    "SELECT ciudad, ROUND(SUM(unidades * precio), 2) AS importe "
    "FROM venta GROUP BY ciudad ORDER BY importe DESC LIMIT 3",
    motor,
)
print(top)
