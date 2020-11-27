import pygame
def presentes():
    presente1 = pygame.image.load('./images/presente1.png')
    presente1 = pygame.transform.smoothscale(presente1, (45,45))
    presente2 = pygame.image.load('./images/presente2.png')
    presente2 = pygame.transform.smoothscale(presente2, (60,60))
    presente3 = pygame.image.load('./images/presente3.png')
    presente3 = pygame.transform.smoothscale(presente3, (45,45))
    presente4 = pygame.image.load('./images/presente4.png')
    presente4 = pygame.transform.smoothscale(presente4, (45,45))
    presente5 = pygame.image.load('./images/presente5.png')
    presente5 = pygame.transform.smoothscale(presente5, (60,45))
    presente6 = pygame.image.load('./images/presente6.png')
    presente6 = pygame.transform.smoothscale(presente6, (45,45))
    bola = pygame.image.load('./images/bolinha.png')
    bola = pygame.transform.smoothscale(bola, (30,45))
    estrela = pygame.image.load('./images/estrela.png')
    estrela = pygame.transform.smoothscale(estrela, (45,45))
    return [presente1,presente2,presente3,presente4,presente4,presente5,presente6,bola,estrela]

def noel():
    braco_cima = pygame.image.load('./images/papai_noel_correndo.png')
    braco_baixo = pygame.image.load('./images/papainoelcorrendo2.png')
    braco_cima_invertido = pygame.image.load('./images/papai_noel_correndovirado.png')
    braco_baixo_invertido = pygame.image.load('./images/papainoelcorrendo2virado.png')
    return [[braco_baixo, braco_cima], [braco_baixo_invertido, braco_cima_invertido]]