def aplicar_evento(evento,jugador):

    if "+2 de oro" in evento:
        jugador.ganar_oro(2)

    if "-1 de vida" in evento:
        jugador.perder_vida(1)