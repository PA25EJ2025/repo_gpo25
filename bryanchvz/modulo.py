import pygame

class Perfil:
    def __init__(self,x,y,alto,ancho,imagen,velocidad):
        self.x = x
        self.y = y
        self.alto = alto
        self.ancho = ancho
        self.velocidad = velocidad
        self.imagen = pygame.image.load("bryanchvz/pfp_bryan.jpg")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
    
    def mostrar(self,ventana):
        ventana.blit(self.imagen, (self.x,self.y))