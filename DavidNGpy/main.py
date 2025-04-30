import pygame
import sys
from pygame.locals import *
from perfil import Perfil

ANCHO_VENTANA = 840
ALTO_VENTANA = 480
FPS = 30
ROJO = (255, 0, 0)

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Foto de Perfil")

reloj = pygame.time.Clock()
foto_perfil = Perfil(0, 0, 80, 80, 10)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Teclas para mover
    teclas = pygame.key.get_pressed()
    if teclas[K_LEFT] and foto_perfil.x > 0:
        foto_perfil.x -= foto_perfil.velocidad
    if teclas[K_RIGHT] and foto_perfil.x < ANCHO_VENTANA - foto_perfil.ancho:
        foto_perfil.x += foto_perfil.velocidad
    if teclas[K_UP] and foto_perfil.y > 0:
        foto_perfil.y -= foto_perfil.velocidad
    if teclas[K_DOWN] and foto_perfil.y < ALTO_VENTANA - foto_perfil.alto:
        foto_perfil.y += foto_perfil.velocidad

    ventana.fill(ROJO)
    foto_perfil.mostrar(ventana)  # <- Esto muestra la imagen
    pygame.display.update()
    reloj.tick(FPS)



