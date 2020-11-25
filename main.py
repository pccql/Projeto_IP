import pygame
from Button import button
def main():
    pygame.init()
    largura=600
    altura=600
    tela=pygame.display.set_mode([largura,altura])
    pygame.display.set_caption("Salve o Natal")
    relogio=pygame.time.Clock()
    abertura=pygame.image.load("./images/SPOILER_capa.png")
    abertura=pygame.transform.smoothscale(abertura, (largura, altura))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        tela.blit(abertura,(0,0))
        relogio.tick(27)
        if button(40,"START",(115,510),(255,255,255),(255,0,0),tela,(255,255,38),(255,0,0), './fonte.ttf'):
            running = False
        pygame.display.update()




main()
