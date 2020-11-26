import pygame
from Button import button
import classes

pygame.init()
largura=750
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

    # teste
    braco_cima = pygame.image.load('./images/papai_noel_correndo.png')
    braco_baixo = pygame.image.load('./images/papainoelcorrendo2.png')
    lista_bracos = [braco_baixo, braco_cima]
    braco_cima_invertido = pygame.image.load('./images/papai_noel_correndovirado.png')
    braco_baixo_invertido = pygame.image.load('./images/papainoelcorrendo2virado.png')
    lista_bracos_invertido = [braco_baixo_invertido, braco_cima_invertido]

    jogador = classes.Papai_noel(lista_bracos)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        tela.blit(fundo,(0,0))

        tela.blit(jogador.surf, jogador.rect)

        jogador.andar(pygame.key.get_pressed(), lista_bracos, lista_bracos_invertido)

        pygame.display.update()
        relogio.tick(27)

tela_inicial()
main()
