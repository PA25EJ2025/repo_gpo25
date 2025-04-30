import pygame

class Perfil:

    def __init__(self, x, y, alto, ancho, ruta_imagen, velocidad):
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = velocidad

    def mostrar(self, ventana):
        ventana.blit(self.imagen, self.rect)
