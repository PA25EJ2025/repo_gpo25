import pygame
import sys
from modulo import PerfilLoisber

pygame.init()

ANCHO, ALTO = 640, 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mover Imagen con Fondo")

fondo = pygame.image.load("Fondo_imagen.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

perfil = PerfilLoisber("Foto.png", ANCHO // 2, ALTO // 2)

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            perfil.mover(evento.key, ANCHO, ALTO)

    VENTANA.blit(fondo, (0, 0))
    perfil.dibujar(VENTANA)
    pygame.display.update()

    reloj.tick(60)
