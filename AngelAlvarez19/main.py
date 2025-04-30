import pygame

class Perfil:
    def __init__(self, x, y, ALTO_VENTANA, ANCHO_VENTANA, FPS):
        self.x = x
        self.y = y
        self.alto = ALTO_VENTANA
        self.ancho = ANCHO_VENTANA
        self.fps = FPS
        
    def mostrar(self, ventana):
        ventana.pygame(self.x, self.y)
