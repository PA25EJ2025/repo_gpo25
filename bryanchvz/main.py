#1. Importar el framework o paquete
import pygame
import sys 
from modulo import Perfil

#2. Definir constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
FPS = 30
NEGRO = (0,0,0)

#3. Inicializar pygame
pygame.init()
#4. Cargar recursos (imagenes)
perfil_imagen = pygame.image.load("bryanchvz/pfp_bryan.jpg")
perfil_imagen = pygame.transform.scale(perfil_imagen, (80,80))

#5. Inicializar variables
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mover la foto de perfil de GitHub")

perfil = Perfil(x=100, y= 100, alto = 80, ancho = 80, velocidad = 10, imagen = "bryanchvz/pfp_bryan.jpg")

#6. Ciclo infinito

clock = pygame.time.Clock()

while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
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

    ventana.fill(NEGRO)
    #10. Dibujar elementos en la ventana
    perfil.mostrar(ventana)

    #11. Actualizar la ventana
    pygame.display.update()    
    #12. Ralentizar un poco las cosas
    clock.tick(FPS)