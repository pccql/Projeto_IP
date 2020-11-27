import pygame
from random import randint
class Papai_noel(pygame.sprite.Sprite):
    def __init__(self, lista_bracos):
        super(Papai_noel, self).__init__()
        self.surf = lista_bracos[0]
        self.numero = 1
        self.rect = self.surf.get_rect(center=(300,450))

    def andar(self, teclas, lista_bracos, lista_bracos_invertido):
        if teclas[pygame.K_UP]:
            self.rect.move_ip(0,-10)
        if teclas[pygame.K_DOWN]:
            self.rect.move_ip(0,10)

        if teclas[pygame.K_RIGHT]:
            self.rect.move_ip(10,0)
            self.numero += 0.25
            if self.numero % 1 == 0:
                self.numero = int(self.numero)
                self.surf = lista_bracos[self.numero % 2] 

        if teclas[pygame.K_LEFT]:
            self.rect.move_ip(-10,0)
            self.numero += 0.25
            if self.numero % 1 == 0:
                self.numero = int(self.numero)
                self.surf = lista_bracos_invertido[self.numero % 2] 

        if self.rect.right >= 780:
            self.rect.right = 780
        if self.rect.left <= -30:
            self.rect.left = -30
        if self.rect.top <= 395:
            self.rect.top = 395
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
        
class Objetos(pygame.sprite.Sprite):
    def __init__(self, lista_objetos):
        super(Objetos, self).__init__()
        ordem = randint(0,len(lista_objetos)-1)
        self.surf = lista_objetos[0]
        posx=randint(23,577)
        posy=randint(460,577)
        self.rect = self.surf.get_rect(center=(posx,posy))
        