import pygame
from pygame.locals import *
import sys
import modulo
FONDO = (0,255,0)
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
FPS = 30
SIZE_CUADRO = 80
ANCHO_MAX = ANCHO_VENTANA - SIZE_CUADRO
ALTO_MAX = ALTO_VENTANA - SIZE_CUADRO
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj = pygame.time.Clock()
pygame.display.set_caption("Evidencia 3")
foto = modulo.Perfil(0,0,SIZE_CUADRO,SIZE_CUADRO,10)
foto.mover(0,0)
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            print("Saliendo...")
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_UP:
                if foto.y - foto.velocidad >= 0:
                    foto.y = foto.y - foto.velocidad  ## sin clase para probar
            if evento.key == K_DOWN:
                if foto.y + foto.velocidad <= ALTO_MAX:
                    foto.abajo()
            if evento.key == K_LEFT:
                if foto.x - foto.velocidad >= 0:
                    foto.izquierda()
            if evento.key == K_RIGHT:
                if foto.x + foto.velocidad <= ANCHO_MAX:
                    foto.derecha()
            if evento.key == pygame.K_ESCAPE:
                print("Saliendo...")
                pygame.quit()
                sys.exit()
    ventana.fill(FONDO)
    foto.mostrar(ventana)
    pygame.display.update()
    reloj.tick(FPS)
