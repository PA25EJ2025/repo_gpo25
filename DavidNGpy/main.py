#1. Importar el framework o paquete
import pygame
from pygame.locals import *
import sys
import modulo
#2. Definir constantes
ANCHO_VENTANA=840
ALTO_VENTANA=480
FPS=30
ROJO=(255,0,0)
#3. Inicializar pygame
pygame.init()
ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
reloj=pygame.time.Clock()
#4. Cargar recursos (imagenes)
foto=pygame.image.load("foto")
#5. Inicializar variables

#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame

    #9. Limpiar la ventana
    ventana.fill(ROJO)

    #10. Dibujar elementos en la ventana
    
    #11. Actualizar la ventana
    pygame.display.update()
    
    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)
