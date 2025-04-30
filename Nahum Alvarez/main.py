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
foto_perfil = pygame.image.load("C:\Users\Salas\Desktop\repo_gpo25\Nahum Alvarez\perfil_good.jpeg")

#5. Inicializar variables
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Intenta mover la pfp")
reloj = pygame.time.Clock()

perfil = PerfilNahum(x=100, y=100, alto=80, ancho=80, velocidad=5)

#6. Ciclo infinito
while True:

    #7. Verificar y manejar los eventos
    for evento in pygame.event.get()
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad
    #9. Limpiar la ventana
    ventana.fill(color_fondo)
    #10. Dibujar elementos en la ventana
    perfil.mostrar(ventana)
    #11. Actualizar la ventana
    pygame.display.flip()
    #12. Ralentizar un poco las cosas
    reloj.tick(fps)