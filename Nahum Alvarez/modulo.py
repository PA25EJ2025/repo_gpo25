import pygame

class Perfil:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.image = pygame.transform.scale(foto_perfil, (self.ancho, self.alto))

    def mostrar(self, ventana)
        ventana.blit(self.imagen, (self.x, self.y))
