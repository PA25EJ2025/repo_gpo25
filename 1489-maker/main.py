import pygame
import sys
from modulo import Perfil

pygame.init()

ANCHO_VENTANA = 640
ALTO_VENTANA = 480
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Perfil")

NEGRO = (0, 0, 0)
perfil = Perfil(100, 100, 80, 80, 5)

reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad

    ventana.fill(NEGRO)
    perfil.mostrar(ventana)
    pygame.display.flip()