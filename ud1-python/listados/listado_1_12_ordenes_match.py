"""Listado 1.12. Intérprete de órdenes con match."""

comando = input("Orden: ").strip().lower()

match comando.split():
    case ["salir"]:
        print("Hasta luego")
    case ["cargar", fichero]:                  # captura el 2.º elemento
        print(f"Cargando {fichero}...")
    case ["filtrar", columna, valor]:
        print(f"Filtrando {columna} = {valor}")
    case ["ayuda" | "?"]:                      # alternativas
        print("Órdenes: cargar, filtrar, salir")
    case _:                                    # comodín: cualquier otro caso
        print(f"Orden desconocida: {comando}")
