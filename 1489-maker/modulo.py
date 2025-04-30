import pygame

class Perfil:
        def __init__(self, x, y, alto, ancho, velocidad):
            self.x = x
            self.y = y
            self.alto = alto
            self.ancho = ancho
            self.velocidad = velocidad
            self.imagen = pygame.image.load (r"C:\Users\maxpa\repo_gpo25\images.jpg")
            self.imagen = pygame.transform.scale(self.imagen, (100, 100))

        def mostrar(self, ventana):
            ventana.blit(self.imagen, (self.x, self.y))