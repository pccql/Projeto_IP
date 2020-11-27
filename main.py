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
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

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


    braco_cima = pygame.image.load('./papai_noel_correndoteste.png')
    braco_baixo = pygame.image.load('./papainoelcorrendo2teste.png')
    lista_bracos = [braco_baixo, braco_cima]
    braco_cima_invertido = pygame.image.load('./papai_noel_correndoviradoteste.png')
    braco_baixo_invertido = pygame.image.load('./papainoelcorrendo2viradoteste.png')
    lista_bracos_invertido = [braco_baixo_invertido, braco_cima_invertido]

    jogador = classes.Papai_noel(lista_bracos)

    presente1 = pygame.image.load('./presente1teste.png')
    presente1 = pygame.transform.smoothscale(presente1, (45,45))
    presente2 = pygame.image.load('./images/presente2.png')
    presente3 = pygame.image.load('./images/presente3.png')
    presente4 = pygame.image.load('./images/presente4.png')
    presente5 = pygame.image.load('./images/presente5.png')
    presente6 = pygame.image.load('./images/presente6.png')
    bola = pygame.image.load('./images/bolinha.png')
    estrela = pygame.image.load('./images/estrela.png')
    lista_objetos = [presente1,presente2,presente3,presente4,presente4,presente5,presente6,bola,estrela]


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
