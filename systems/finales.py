from ui.pantalla import mostrar_escena

def final_fabiana(pantalla,jugador,texto):

    mostrar_escena(pantalla,texto)
    jugador.agregar_rasgo("Amor Verdadero")


def final_matias(pantalla,jugador):

    mostrar_escena(
        pantalla,
        "Matias derrota al dragon sacrificando su espada."
    )

    jugador.agregar_rasgo("Hermandad de Acero")