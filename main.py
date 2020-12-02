import pygame
from Button import button
import classes
import funcoes

pygame.init()
largura=1000
altura=650
tela=pygame.display.set_mode([largura,altura])
pygame.display.set_caption("Salve o Natal")
relogio=pygame.time.Clock()

try:
    pygame.mixer.init()
    pygame.mixer.load('./jingle_bells.ogg')
    pygame.mixer.play()
except:
    pass

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
        if button(40,"START",(190,510),(255,255,255),(255,0,0),tela,(255,255,38),(255,0,0), './fonte.ttf'):
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
    objeto = classes.Objetos(lista_objetos, jogador.rect)
    tempo_objeto = pygame.time.get_ticks()
    tempo_final = 1000000000

    dicionario_objetos = {'presente': 0, 'bolinha': 0, 'estrela': 0}
    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    
        tela.blit(fundo,(0,0))

        

        funcoes.arvore(dicionario_objetos, tela, lista_objetos[:8])

        tela.blit(jogador.surf, jogador.rect)

        jogador.andar(pygame.key.get_pressed(), lista_bracos, lista_bracos_invertido)

        tela.blit(objeto.surf,objeto.rect)

        if pygame.sprite.collide_rect(jogador, objeto):
            if objeto.presente == True:
                dicionario_objetos['presente'] += 1
            elif objeto.estrela == True:
                dicionario_objetos['estrela'] += 1
                tempo_final = pygame.time.get_ticks()
            else:
                dicionario_objetos['bolinha'] += 1
            
            objeto.kill()
            if dicionario_objetos['presente'] >= 30 and dicionario_objetos['bolinha'] >= 10:
                objeto = classes.Objetos(lista_objetos, jogador.rect)
            else:
                objeto = classes.Objetos(lista_objetos[:8], jogador.rect)
            tempo_objeto = pygame.time.get_ticks()

        total_coletados = dicionario_objetos['presente'] + dicionario_objetos['bolinha']

        if total_coletados <= 6:
            if (pygame.time.get_ticks()- tempo_objeto)/1000 > 5:
                objeto.kill()
                if dicionario_objetos['presente'] >= 30 and dicionario_objetos['bolinha'] >= 10:
                    objeto = classes.Objetos(lista_objetos, jogador.rect)
                else:
                    objeto = classes.Objetos(lista_objetos[:8], jogador.rect)
                tempo_objeto = pygame.time.get_ticks()
        elif total_coletados <= 15:
            if (pygame.time.get_ticks()- tempo_objeto)/1000 > 4:
                objeto.kill()
                if dicionario_objetos['presente'] >= 30 and dicionario_objetos['bolinha'] >= 10:
                    objeto = classes.Objetos(lista_objetos, jogador.rect)
                else:
                    objeto = classes.Objetos(lista_objetos[:8], jogador.rect)
                tempo_objeto = pygame.time.get_ticks()
        elif total_coletados <= 25:
            if (pygame.time.get_ticks()- tempo_objeto)/1000 > 3:
                objeto.kill()
                if dicionario_objetos['presente'] >= 30 and dicionario_objetos['bolinha'] >= 10:
                    objeto = classes.Objetos(lista_objetos, jogador.rect)
                else:
                    objeto = classes.Objetos(lista_objetos[:8], jogador.rect)
                tempo_objeto = pygame.time.get_ticks()
        elif total_coletados <= 35:
            if (pygame.time.get_ticks()- tempo_objeto)/1000 > 2:
                objeto.kill()
                if dicionario_objetos['presente'] >= 30 and dicionario_objetos['bolinha'] >= 10:
                    objeto = classes.Objetos(lista_objetos, jogador.rect)
                else:
                    objeto = classes.Objetos(lista_objetos[:8], jogador.rect)
                tempo_objeto = pygame.time.get_ticks()


        funcoes.contador(dicionario_objetos, tela)
        
        if dicionario_objetos['estrela'] > 0 and (pygame.time.get_ticks() - tempo_final) /1000 < 4:
            fim = pygame.image.load('./images/telafinal.png')
            fim = pygame.transform.smoothscale(fim, (largura, altura))
            tela.blit(fim,(0,0))
        

        if (pygame.time.get_ticks() - tempo_final) /1000 > 3.9:
            running = False
        
            
        pygame.display.update()
        
        relogio.tick(27)

tela_inicial()
main()
