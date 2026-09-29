# Proyecto de ejemplo de la UD1: paquete `ventas`

Código completo del apartado 1.8 de los [apuntes](../UD1-python-para-quien-ya-programa.md#18-módulos-y-paquetes).

```bash
cd ud1-python/proyecto
python -m venv .venv
# Windows (PowerShell):   .venv\Scripts\Activate.ps1
# macOS / Linux:          source .venv/bin/activate
python -m pip install -e .
python -m ventas
```

Salida esperada:

```text
WARNING: Línea 5 descartada: invalid literal for int() with base 10: ''
Málaga     4845.00 €
Granada    3059.70 €
```
