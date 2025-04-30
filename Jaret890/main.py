import pygame
import sys
from pygame.locals import *
import modulo

NEGRO = (0,0,0)
ANCHO_VENTANA = 750
ALTO_VENTANA = 650
FPS = 60

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()

icon = modulo.Perfil(0,0,0,0,5,'Jaret890/Shinoa_icon')

while True:
    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_UP]:
        icon.y -= icon.velocidad
    elif tecla[pygame.K_DOWN]:
        icon.y += icon.velocidad
    elif tecla[pygame.K_RIGHT]:
        icon.x += icon.velocidad
    elif tecla[pygame.K_LEFT]:
        icon.x -= icon.velocidad
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(NEGRO)
    icon.mostrar(ventana,icon.x,icon.y)
    pygame.display.update()
    reloj.tick(FPS)