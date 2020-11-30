import pygame
from random import randint

class Papai_noel(pygame.sprite.Sprite):
    def __init__(self, lista_bracos):
        super(Papai_noel, self).__init__()
        self.surf = lista_bracos[0]
        self.numero = 1
        self.rect = self.surf.get_rect(center=(500,450))

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

        if self.rect.right >= 1000:
            self.rect.right = 1000
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 388:
            self.rect.top = 388
        if self.rect.bottom >= 650:
            self.rect.bottom = 650
        
class Objetos(pygame.sprite.Sprite):
    def __init__(self, lista_objetos, pos_jogador):
        super(Objetos, self).__init__()
        self.estrela = False
        self.presente = False
        ordem = randint(0,len(lista_objetos)-1)
        self.surf = lista_objetos[ordem]
        if ordem == 8:
            self.estrela = True
        elif ordem == 6 or ordem == 7:
            self.presente = False
        else:
            self.presente = True

        posx=randint(23,877)
        posy=randint(460,630)

        while abs(posx - pos_jogador[0])<250  or abs(posx - 810)<100:
            posx=randint(23,877)

        self.rect = self.surf.get_rect(center=(posx,posy))
        