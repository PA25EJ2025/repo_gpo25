#1. Importar el framework o paquete
import pygame
from pygame.locals import*
import sys
import random

#2. Definir constantes
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
COLOR = (0, 250, 0)
FPS = 30
SIZE_CUADRO = 10
ANCHO_MAX = ANCHO_VENTANA - SIZE_CUADRO
ANCHO_MIN = ALTO_VENTANA - SIZE_CUADRO

#3. Inicializar pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Movimiento")
reloj = pygame.time.Clock()

#4. Cargar recursos (imagenes)
objeto = pygame.image.load("cuadro.png")

#5. Inicializar variables
x = ANCHO_VENTANA // 2
y = ALTO_VENTANA // 2

#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= FPS
    if teclas[pygame.K_RIGHT]:
        x += FPS
    if teclas[pygame.K_UP]:
        y -= FPS
    if teclas[pygame.K_DOWN]:
        y += FPS
    #9. Limpiar la ventana
    ventana.fill(COLOR)
    #10. Dibujar elementos en la ventana
    ventana.blit(objeto, (x, y))
    #11. Actualizar la ventana
    pygame.display.flip()

    #12. Ralentizar un poco las cosas
    reloj.tick(30)