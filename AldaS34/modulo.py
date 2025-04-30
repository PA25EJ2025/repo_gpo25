import pygame

class Perfil:
    def __init__(self,x,y,alto,ancho,velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.imagen = pygame.image.load('Foto.png')
        self.velocidad = velocidad

    def mostrar(self,ventana):
        ventana.blit(self.imagen,(self.x, self.y))



