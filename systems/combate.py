import pygame
import sys

def combate(pantalla,jugador,enemigo,sprites):

    vida_enemigo = enemigo.vida
    atacando = False
    delay = 0

    while vida_enemigo > 0 and jugador.esta_vivo():

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_SPACE and not atacando:
                    atacando = True
                    vida_enemigo -= 1
                    delay = 30

        pantalla.fill((20,20,40))

        sprite = sprites["protagonista_atacando"] if atacando else sprites["protagonista_normal"]

        pantalla.blit(sprite,(100,300))
        pantalla.blit(sprites["cueva_dragon"],(500,300))

        pygame.display.flip()

        if atacando:

            delay -= 1

            if delay <= 0:

                atacando = False
                enemigo.atacar(jugador)