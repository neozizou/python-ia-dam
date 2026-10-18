"""Preguntas que se le hacen a la lista de jugadores."""


def mas_caros(jugadores: list[dict], cuantos: int = 5) -> list[dict]:
    """Los jugadores con mayor valor de mercado, de mayor a menor.

    Los de valor cero (agentes libres) quedan fuera: ahí el cero significa
    «no hay dato», no «no vale nada».
    """
    con_valor = [j for j in jugadores if j["value_eur"] > 0]
    return sorted(con_valor, key=lambda j: j["value_eur"], reverse=True)[:cuantos]


def media_por_pais(jugadores: list[dict], minimo: int = 100) -> dict[str, float]:
    """Media de valoración por país, solo para los países con bastantes jugadores."""
    suma: dict[str, int] = {}
    cuenta: dict[str, int] = {}
    for jugador in jugadores:
        pais = jugador["nationality"]
        suma[pais] = suma.get(pais, 0) + jugador["overall"]
        cuenta[pais] = cuenta.get(pais, 0) + 1
    return {pais: round(suma[pais] / cuenta[pais], 1)
            for pais in suma if cuenta[pais] >= minimo}
