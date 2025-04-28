import pygame
class Perfil:
    def __init__(self,x,y,ancho,alto,velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = pygame.image.load("KevinHdz29/foto.png")
        self.velocidad = velocidad
    def mostrar(self,ventana):
        ventana.blit(self.imagen,(self.x,self.y,self.ancho,self.alto))
    def mover(self,x,y):
        self.x = x
        self.y = y
    def arriba(self):
        self.y = self.y - self.velocidad
    def abajo(self):
        self.y = self.y + self.velocidad
    def izquierda(self):
        self.x = self.x - self.velocidad
    def derecha(self):
        self.x = self.x + self.velocidad
