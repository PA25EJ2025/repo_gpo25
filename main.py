import pygame
import sys
from modulo import PerfilCarlos

# Inicialización
pygame.init()

# Tamaño ventana
ANCHO, ALTO = 640, 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mover Imagen con Fondo")

# Fondo videojuego
fondo = pygame.image.load("CarlosCastillo19/Fondo-Videojuego.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Crear el perfil
perfil = PerfilCarlos("CarlosCastillo19/FotoPerfil.png", ANCHO // 2, ALTO // 2)

# Reloj
reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            perfil.mover(evento.key, ANCHO, ALTO)

    # Dibujar fondo y la imagen
    VENTANA.blit(fondo, (0, 0))
    perfil.dibujar(VENTANA)
    pygame.display.update()

    reloj.tick(60)


#1. Importar el framework o paquete

#2. Definir constantes

#3. Inicializar pygame

#4. Cargar recursos (imagenes)
#5. Inicializar variables

#6. Ciclo infinito
    #7. Verificar y manejar los eventos
    #8. Realizar cualquier acción por frame

    #9. Limpiar la ventana

    #10. Dibujar elementos en la ventana
    
    #11. Actualizar la ventana
    
    #12. Ralentizar un poco las cosas
