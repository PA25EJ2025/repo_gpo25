import pygame
import os

class PerfilDavid:
    def __init__(self, x, y, alto, ancho, velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad

        ruta_imagen = os.path.join("C:\\Users\\dg289\\Desktop\\repo_gpo25\\DavidNGpy\\assets", "foto.png")
        self.imagen = pygame.image.load(ruta_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))

    def mostrar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))