import pygame
from time import sleep
from Button import button
pygame.init()
largura=600
altura=600
tela=pygame.display.set_mode([largura,altura])
pygame.display.set_caption("Salve o Natal")
relogio=pygame.time.Clock()


def tela_inicial():
    abertura=pygame.image.load("./images/capa2.jpg")
    abertura=pygame.transform.smoothscale(abertura, (largura, altura))
    fim_inicial = False
    tempo_inicio = 10000000

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        tela.blit(abertura,(0,0))
        if button(40,"START",(115,510),(255,255,255),(255,0,0),tela,(255,255,38),(255,0,0), './fonte.ttf'):
            fim_inicial = True
            tempo_inicio = pygame.time.get_ticks()

        if fim_inicial and (pygame.time.get_ticks() - tempo_inicio) /1000 < 2:
            corra = pygame.image.load('./images/corra.jpg')
            corra = pygame.transform.smoothscale(corra, (largura, altura))
            tela.blit(corra, (0,0))

        if (pygame.time.get_ticks() - tempo_inicio) /1000 > 1.9:
            running = False

        pygame.display.update()
        relogio.tick(27)


def main():
    fundo = pygame.image.load("./images/cenario2.jpg")
    fundo = pygame.transform.smoothscale(fundo, (largura, altura))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        tela.blit(fundo,(0,0))
        pygame.display.update()
        relogio.tick(27)

tela_inicial()
main()