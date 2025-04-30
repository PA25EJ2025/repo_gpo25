import pygame

class PerfilLoisber:
    def __init__(self, imagen_path, x, y):
        self.imagen = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen, (80, 80))
        self.x = x
        self.y = y
        self.velocidad = 5

    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

    def mover(self, tecla, ancho_ventana, alto_ventana):
        if tecla == pygame.K_LEFT and self.x > 0:
            self.x -= self.velocidad
        elif tecla == pygame.K_RIGHT and self.x < ancho_ventana - 80:
            self.x += self.velocidad
        elif tecla == pygame.K_UP and self.y > 0:
            self.y -= self.velocidad
        elif tecla == pygame.K_DOWN and self.y < alto_ventana - 80:
            self.y += self.velocidad
