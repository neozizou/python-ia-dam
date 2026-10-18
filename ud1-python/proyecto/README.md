# Proyecto de ejemplo de la UD1: paquete `ojeador`

Código completo del apartado 1.8 de los [apuntes](../UD1-python-para-quien-ya-programa.md#18-módulos-y-paquetes). Lee el fichero de jugadores del curso (`datos-comunes/jugadores.csv`) y responde dos preguntas sobre una edición.

```bash
cd ud1-python/proyecto
python -m venv .venv
# Windows (PowerShell):   .venv\Scripts\Activate.ps1
# macOS / Linux:          source .venv/bin/activate
python -m pip install -e .
python -m ojeador
```

Salida esperada:

```text
FIFA 2020: 18,278 jugadores

Los cinco más caros:
  Neymar Jr            Paris Saint-Germain     105.5 M€
  L. Messi             FC Barcelona             95.5 M€
  K. Mbappé            Paris Saint-Germain      93.5 M€
  E. Hazard            Real Madrid              90.0 M€
  K. De Bruyne         Manchester City          90.0 M€

Media más alta, entre los 38 países con 100 jugadores o más:
  Uruguay          71.6
  Brazil           71.2
  Portugal         70.5
  Czech Republic   70.3
  Spain            70.0
```

| Fichero | Qué hace |
| --- | --- |
| `src/ojeador/__init__.py` | La interfaz pública del paquete: qué puede usar quien lo importe |
| `src/ojeador/lectura.py` | Abre el CSV y convierte los números |
| `src/ojeador/consultas.py` | Las preguntas: los más caros y la media por país |
| `src/ojeador/__main__.py` | Lo que se ejecuta con `python -m ojeador` |
