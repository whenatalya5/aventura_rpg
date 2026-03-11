import pygame
import sys
import random

from core.jugador import Jugador
from core.enemigo import Enemigo

from systems.combate import combate
from systems.eventos import aplicar_evento
from systems.finales import final_fabiana, final_matias

from ui.pantalla import mostrar_escena, menu_opciones
from assets.sprites import cargar_sprites

from story.texto_inicio import TEXTO_INICIO
from story.texto_capital import TEXTO_CAPITAL
from story.texto_personajes import TEXTO_FABIANA, TEXTO_MATIAS, TEXTO_COMPANERO
from story.texto_eventos import EVENTOS
from story.texto_mei import TEXTO_MEI
from story.texto_dragon import TEXTO_DRAGON
from story.texto_finales import TEXTO_DECISION_FINAL, TEXTO_NUEVA_PARTIDA


def main():

    pygame.init()

    pantalla = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Aventura RPG")

    sprites = cargar_sprites()

    jugador = Jugador("Aventurero")

    mostrar_escena(pantalla,TEXTO_INICIO)
    mostrar_escena(pantalla,TEXTO_CAPITAL,sprites["capital"])

    mostrar_escena(pantalla,TEXTO_FABIANA)
    mostrar_escena(pantalla,TEXTO_MATIAS)

    opcion = menu_opciones(pantalla,TEXTO_COMPANERO,[1,2])
    companero = "Matias" if opcion == 1 else "Fabiana"

    evento = random.choice(EVENTOS)
    mostrar_escena(pantalla,evento)
    aplicar_evento(evento,jugador)

    respuesta = menu_opciones(pantalla,TEXTO_MEI,[1,2,3])

    if respuesta in [2,3]:
        jugador.agregar_rasgo("Proteccion Elfica")
        mostrar_escena(pantalla,"Mei te concede protección élfica.")

    mostrar_escena(pantalla,TEXTO_DRAGON,sprites["lava"])

    dragon = Enemigo("Dragon Corrompido",3,1)

    combate(pantalla,jugador,dragon,sprites)

    if companero == "Fabiana":
        final_fabiana(pantalla,jugador,TEXTO_DECISION_FINAL)
    else:
        final_matias(pantalla,jugador)

    mostrar_escena(
        pantalla,
        f"""{TEXTO_NUEVA_PARTIDA}

ORO: {jugador.oro}
VIDA: {jugador.vida}
RASGOS: {jugador.rasgos}
"""
    )

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()