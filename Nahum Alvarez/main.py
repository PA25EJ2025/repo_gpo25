#1. Importar el framework o paquete
import pygame
import sys
from pygame.locals import *
from modulo import PerfilNahum

#2. Definir constantes
ancho_ventana = 600
alto_ventana = 400
color_fondo = 80, 31, 96
fps = 60

#3. Inicializar pygame
pygame.init()

#4. Cargar recursos (imagenes)
foto_perfil = pygame.image.load("Nahum Alvarez/perfil_good.png")

#5. Inicializar variables
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Intenta mover la pfp")
reloj = pygame.time.Clock()

perfil = PerfilNahum(x=100, y=100, alto=80, ancho=80, velocidad=5)

#6. Ciclo infinito
    #7. Verificar y manejar los eventos
    #8. Realizar cualquier acción por frame

    #9. Limpiar la ventana

    #10. Dibujar elementos en la ventana
    
    #11. Actualizar la ventana
    
    #12. Ralentizar un poco las cosas