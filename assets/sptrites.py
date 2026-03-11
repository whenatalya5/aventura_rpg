import pygame
import os

def cargar_sprites():

    base = "images"

    sprites = {

        # protagonista
        "protagonista": pygame.image.load(os.path.join(base,"prota.jpeg")).convert_alpha(),
        "protagonista_atacando": pygame.image.load(os.path.join(base,"prota1.jpeg")).convert_alpha(),

        # enemigos
        "enemigo": pygame.image.load(os.path.join(base,"enemigo.jpeg")).convert_alpha(),
        "enemigo2": pygame.image.load(os.path.join(base,"enemigo1.jpeg")).convert_alpha(),

        # dragón
        "dragon": pygame.image.load(os.path.join(base,"dragon.jpeg")).convert_alpha(),
        "dragon2": pygame.image.load(os.path.join(base,"dragon1.jpeg")).convert_alpha(),

        # fondos
        "capital": pygame.image.load(os.path.join(base,"fondo1.jpeg")).convert(),
        "bosque": pygame.image.load(os.path.join(base,"fondo2.jpeg")).convert(),
        "mazmorra": pygame.image.load(os.path.join(base,"fondo3.jpeg")).convert(),
        "ruinas": pygame.image.load(os.path.join(base,"fondo4.jpeg")).convert(),
        "pueblo": pygame.image.load(os.path.join(base,"fondo5.jpeg")).convert(),
        "lava": pygame.image.load(os.path.join(base,"fondo6.jpeg")).convert(),
        "templo": pygame.image.load(os.path.join(base,"fondo7.jpeg")).convert(),
        "montaña": pygame.image.load(os.path.join(base,"fondo8.jpeg")).convert(),

        # botones
        "flecha_arriba": pygame.image.load(os.path.join(base,"arriba.jpeg")).convert_alpha(),
        "flecha_abajo": pygame.image.load(os.path.join(base,"abajo.jpeg")).convert_alpha(),

        # tecla espacio
        "espacio": pygame.image.load(os.path.join(base,"espace.jpeg")).convert_alpha(),

    }

    return sprites