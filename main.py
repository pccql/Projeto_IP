import pygame
from Button import button
import classes
import funcoes

pygame.init()
largura=750
altura=600
tela=pygame.display.set_mode([largura,altura])
pygame.display.set_caption("Salve o Natal")
relogio=pygame.time.Clock()


def tela_inicial():
    abertura=pygame.image.load("./images/capa.png")
    abertura=pygame.transform.smoothscale(abertura, (largura, altura))
    fim_inicial = False
    tempo_inicio = 10000000

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        tela.blit(abertura,(0,0))
        if button(40,"START",(115,510),(255,255,255),(255,0,0),tela,(255,255,38),(255,0,0), './fonte.ttf'):
            fim_inicial = True
            tempo_inicio = pygame.time.get_ticks()

        if fim_inicial and (pygame.time.get_ticks() - tempo_inicio) /1000 < 2:
            corra = pygame.image.load('./images/tela de inicio.png')
            corra = pygame.transform.smoothscale(corra, (largura, altura))
            tela.blit(corra, (0,0))

        if (pygame.time.get_ticks() - tempo_inicio) /1000 > 1.9:
            running = False
        

        pygame.display.update()
        relogio.tick(27)


def main():
    fundo = pygame.image.load("./images/cenario.png")
    fundo = pygame.transform.smoothscale(fundo, (largura, altura))


    lista_bracos = funcoes.noel()[0]
    lista_bracos_invertido = funcoes.noel()[1]

    jogador = classes.Papai_noel(lista_bracos)

    lista_objetos = funcoes.presentes()
    objeto = classes.Objetos(lista_objetos)

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

        tela.blit(objeto.surf,objeto.rect)

        if pygame.sprite.collide_rect(jogador, objeto):
            objeto.kill()
            objeto = classes.Objetos(lista_objetos)
            
        pygame.display.update()

        relogio.tick(27)

tela_inicial()
main()
