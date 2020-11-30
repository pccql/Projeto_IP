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
    return [presente1,presente2,presente3,presente4,presente5,presente6,bola,bola,estrela]

def noel():
    braco_cima = pygame.image.load('./images/papai_noel_correndo.png')
    braco_baixo = pygame.image.load('./images/papainoelcorrendo2.png')
    braco_cima_invertido = pygame.image.load('./images/papai_noel_correndovirado.png')
    braco_baixo_invertido = pygame.image.load('./images/papainoelcorrendo2virado.png')
    return [[braco_baixo, braco_cima], [braco_baixo_invertido, braco_cima_invertido]]

def contador(dicionario_objetos, tela):
    pygame.draw.rect(tela, (255,255,38), (450, 25, 100, 35))
    pygame.draw.rect(tela, (255,255,38), (575, 25, 100, 35))

    presente = pygame.image.load('./images/presente3.png')
    presente = pygame.transform.smoothscale(presente, (28,32))
    tela.blit(presente, presente.get_rect(center=(475,40)))

    font = pygame.font.Font('./fonte.ttf', 40)
    text = font.render(f"{dicionario_objetos['presente']}", True, (0,0,0))
    tela.blit(text, text.get_rect(center=(512,44)))

    bola = pygame.image.load('./images/bolinha.png')
    bola = pygame.transform.smoothscale(bola, (20,30))
    tela.blit(bola, bola.get_rect(center=(600,42)))

    font = pygame.font.Font('./fonte.ttf', 40)
    text = font.render(f"{dicionario_objetos['bolinha']}", True, (0,0,0))
    tela.blit(text, text.get_rect(center=(637, 43)))


def arvore(dicionario_objetos, tela, lista_objetos):
    coordx = 820
    coordy = 430
    
    arvore = pygame.image.load('./images/arvorenormal.png')  #(220, 283)
    if dicionario_objetos['bolinha'] >= 3: 
        arvore = pygame.image.load('./images/arvore1bola.png')
    if dicionario_objetos['bolinha'] >= 6:
        arvore = pygame.image.load('./images/arvore2bolas.png')
    if dicionario_objetos['bolinha'] >= 10: 
        arvore = pygame.image.load('./images/arvore3bolas.png')
    
    if dicionario_objetos['estrela'] > 0: 
        arvore = pygame.image.load('./images/arvorepronta.png')

    arvore = pygame.transform.smoothscale(arvore, (190,190))
    tela.blit(arvore, (810,295))
    
    if dicionario_objetos['presente'] >= 5: 
        tela.blit(lista_objetos[0], (coordx,coordy))
    if dicionario_objetos['presente'] >= 10:
        tela.blit(lista_objetos[1], (coordx+15,coordy+10))
    if dicionario_objetos['presente'] >= 15: 
        tela.blit(lista_objetos[2], (coordx+35,coordy+20))
    if dicionario_objetos['presente'] >= 20:
        tela.blit(lista_objetos[3], (coordx+65,coordy+30))
    if dicionario_objetos['presente'] >= 25: 
        tela.blit(lista_objetos[4], (coordx+100,coordy+15))
    if dicionario_objetos['presente'] >= 30:
        tela.blit(lista_objetos[5], (coordx+140,coordy+7))
    
    
        
    
    
    
