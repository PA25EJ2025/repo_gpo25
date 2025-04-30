import pygame
class Perfil:
    def __init__(self,x,y,ancho,alto,velocidad,imagen):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.imagen = pygame.image.load('Jaret890/Shinoa_icon.jpg')

    def mostrar(self,x,y,ventana):
        ventana.blit(self.imagen,(self.x,self.y))