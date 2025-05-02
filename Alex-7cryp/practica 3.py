import pygame
import os

# Inicializa pygame
pygame.init()

# Definir tamaño de la ventana
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mover Foto de Perfil")

# Definir la clase Perfil
class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load("perfil.jpg")  # Asegúrate de poner la imagen correcta
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

# Crear el objeto perfil
perfil = Perfil(100, 100, 80, 80, 5)

# Bucle principal del juego
corriendo = True
while corriendo:
    ventana.fill((255, 255, 255))  # Fondo blanco
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover la foto con las teclas de dirección
    if teclas[pygame.K_UP]:
        perfil.y -= perfil.velocidad
    if teclas[pygame.K_DOWN]:
        perfil.y += perfil.velocidad
    if teclas[pygame.K_LEFT]:
        perfil.x -= perfil.velocidad
    if teclas[pygame.K_RIGHT]:
        perfil.x += perfil.velocidad

    # Asegurar que la imagen no se salga de la pantalla
    if perfil.x < 0:
        perfil.x = 0
    if perfil.x > ANCHO_VENTANA - perfil.ancho:
        perfil.x = ANCHO_VENTANA - perfil.ancho
    if perfil.y < 0:
        perfil.y = 0
    if perfil.y > ALTO_VENTANA - perfil.alto:
        perfil.y = ALTO_VENTANA - perfil.alto

    # Mostrar la imagen
    perfil.mostrar(ventana)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar el FPS
    pygame.time.Clock().tick(60)

# Finalizar pygame
pygame.quit()
