import pygame as pg
#Crear clase d
class Perfil:
    def __init__(self,x,y,ancho,alto,imagen,velocidad):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.imagen = pg.image.load(imagen)
        self.imagen = pg.transform.scale(self.imagen,(self.ancho,self.alto))
        self.velocidad = velocidad

    def mostrar(self,ventana,x,y): 
        ventana.blit(self.imagen,(self.x,self.y))