import pygame 
from pygame.locals import *
import sys
from modulo import *

#Constantes

ANCHO_VENTANA = 1000
ALTO_VENTANA = 760

#Inicio
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()

#Carga de recursos
tortuga = Perfil(100,100,80,80,10 )

#Ciclo
while True:
    #Manejo de eventos
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:
            if evento.key == pygame.K_UP:
                tortuga.y -= tortuga.velocidad
            if evento.key == pygame.K_DOWN:
                tortuga.y += tortuga.velocidad
            if evento.key == pygame.K_LEFT:
                tortuga.x -= tortuga.velocidad
            if evento.key == pygame.K_RIGHT:
                tortuga.x += tortuga.velocidad

    #Dibujo
    ventana.fill((0,0,0))
    tortuga.mostrar(ventana)


    pygame.display.update()
