import pygame
from pygame.locals import *
from modulo import Perfil
import sys


ANCHO_VENTANA = 1000
ALTURA_VENTANA = 760
reloj = pygame.time.Clock()

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA))
pygame.display.set_caption("Profile Picture")

#Inicializar la clase de la imagen de perfil
patrick = Perfil(90,90,80,80,'patrick.jpeg',10)

#Iniciar el ciclo de la aplicacion
while True:
    reloj.tick(60)
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        patrick.y -= patrick.velocidad

    if teclas[pygame.K_DOWN]:
        patrick.y += patrick.velocidad

    if teclas[pygame.K_LEFT]:
        patrick.x -= patrick.velocidad

    if teclas[pygame.K_RIGHT]:
        patrick.x += patrick.velocidad

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill((0,0,0))
    patrick.mostrar(ventana,patrick.x,patrick.y)
    
    
    pygame.display.update()