import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO_VENTANA = 640
ALTO_VENTANA = 480
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover foto de perfil")

# Clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load("perfil.jpeg")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

# Crear instancia de Perfil
perfil = Perfil(100, 100, 80, 80, 5)

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    reloj.tick(60)  # 60 FPS
    VENTANA.fill((255, 255, 255))  # Limpiar la pantalla (blanco)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad

    # Mostrar imagen
    perfil.mostrar(VENTANA)
    pygame.display.update()

pygame.quit()
sys.exit()
