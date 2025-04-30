#1. Importar el framework o paquete
import pygame
import sys
from modulo import Perfil

#2. Definir constantes
ANCHO = 800
ALTO = 800
FPS = 60
LILA = (229, 198, 241)

#3. Inicializar pygame
pygame.init()
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

#4. Cargar recursos (imagenes)

#5. Inicializar variables

imagen = Perfil(100, 100, 80, 80, 'lizmtz01/fdp_liz.jpeg', 5)

#6. Ciclo infinito
while True:
    #7. Verificar y manejar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #8. Realizar cualquier acción por frame
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_UP]:
        imagen.rect.y -= imagen.velocidad
    if teclas[pygame.K_DOWN]:
        imagen.rect.y += imagen.velocidad
    if teclas[pygame.K_LEFT]:
        imagen.rect.x -= imagen.velocidad
    if teclas[pygame.K_RIGHT]:
        imagen.rect.x += imagen.velocidad


    #9. Limpiar la ventana
    VENTANA.fill(LILA)

    #10. Dibujar elementos en la ventana
    imagen.mostrar(VENTANA)

    #11. Actualizar la ventana
    pygame.display.update()

    #12. Ralentizar un poco las cosas
    reloj.tick(FPS)