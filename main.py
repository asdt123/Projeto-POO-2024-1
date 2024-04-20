import pygame

# Import and initialize the pygame library
import pygame
from pygame.locals import *

#inicialização da biblioteca pygames
pygame.init()


class Personagem:
    '''
    rect = definição do espaço que ocupa na tela
    rectHitbox = espaço do ataque
    lado = definição da frente do personagem, False está virado para esquerda e True para direita
    ataque = lista mostrando qual ataque foi ativado no momento, no momento com 2 ataques diferentes
    noChao = verdadeiro para se o objeto está na altura minima
    emQueda = verdadeiro para se o objeto atingiu a altura maxima de salto
    alturaMinima = altura minima que o objeto pode chegar
    alturaInicial = altura que o objeto tinha antes de pular
    alturaMaxima = altura maxima que o objeto alcança em salto
    velocidade = velocidade de movimento
    colidiuAcima = se colidiu acima de outro objeto
    colidiuAbaixo = se colidiu abaixo de outro objeto
    colidiuLateral = se colidiu lateralmente com outro objeto, index 0 para esquerda e 1 para direita
    '''
    def __init__(self, janela, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.rectHitbox = pygame.Rect(self.rect.centerx, self.rect.y, 70,30)
        self.lado = False
        self.ataque = [False,False]
        self.noChao = True
        self.emQueda = False
        self.alturaMinima = janela.get_height()
        self.alturaInicial = janela.get_height()
        self.alturaMaxima = self.rect.h*5
        self.velocidade = 0
        self.colidiuAcima = False
        self.colidiuAbaixo = False
        self.colidiuLateral = [False,False]
    
    '''
    Realiza movimento do objeto no eixo x, verificando se está dentro do limite da janela
    e se não tem outro objeto a frente. Alem disso, impede movimento no ar e mantem velocidade
    no salto
    '''
    def mover(self, janela, velocidade):
        if self.noChao: 
            self.velocidade=velocidade
            if velocidade<0:
                self.lado = False
            elif velocidade >0:
                self.lado = True
        if self.colidiuLateral[0] and velocidade>0:
            self.velocidade=0
        elif self.colidiuLateral[1] and velocidade<0:
            self.velocidade=0
        elif self.rect.x+self.velocidade < 0:
            self.velocidade=0
            self.rect.x=0
        elif self.rect.x + self.rect.w+self.velocidade>=janela.get_width():
            self.velocidade=0
            self.rect.x=janela.get_width()-self.rect.w
        else:
            self.rect.x+=self.velocidade
    
    '''
    Realiza salto do objeto, verificando a altura maxima que pode chegar e definindo
    a velocidade de queda e subida. Impede ultrapassar outros objetos
    '''
    def pulo(self, velocidade):
        if self.noChao:
            self.noChao = False
            self.alturaInicial = self.rect.bottom
        elif not self.noChao and not self.emQueda:
            if self.alturaInicial-self.rect.y<self.alturaMaxima:
                self.rect.y-=velocidade
                if self.alturaInicial-self.rect.y>=self.alturaMaxima:
                    self.emQueda=True
        elif self.emQueda:
            if self.rect.y+self.rect.h < self.alturaMinima:
                self.rect.y+=velocidade
                if self.rect.y+self.rect.h >= self.alturaMinima:
                    self.rect.y=self.alturaMinima-self.rect.h
                    self.emQueda=False
                    self.noChao=True
        

    '''
    Ativa o ataque basico :sujeito a alterações
    '''   
    def atacar(self):
        if self.ataque[0] == False and self.ataque[1] == False:
            if self.lado:
                self.rectHitbox = pygame.Rect(self.rect.centerx, self.rect.y, 70,30)
            else:
                self.rectHitbox = pygame.Rect(self.rect.centerx - 70, self.rect.y, 70,30)                
            self.ataque[0] = True

    '''
    Ativa o ataque especial :sujeito a alterações
    '''
    def atacarSonico(self):
        if self.ataque[0] == False and self.ataque[1] == False:
            if self.lado:
                self.rectHitbox = pygame.Rect(self.rect.centerx, self.rect.centery-35, 200,60)
            else:
                self.rectHitbox = pygame.Rect(self.rect.centerx - 200, self.rect.centery-35, 200,60)                
            self.ataque[1] = True

    '''
    identifica e sinaliza colisões nos 4 lados do objeto : falta definir colisão com multiplos objetos, provavelmente usar lista
    '''
    def colisaoObstaculo(self, obstaculo, janela):
        if self.rect.right>=obstaculo.rect.left and self.rect.left<=obstaculo.rect.right:
            if self.rect.top<obstaculo.rect.bottom and self.rect.bottom>obstaculo.rect.top:
                if self.rect.right==obstaculo.rect.left:
                    self.colidiuLateral[0]=True
                elif self.rect.left==obstaculo.rect.right:
                    self.colidiuLateral[1]=True
            elif self.rect.top>=obstaculo.rect.bottom:
                self.colidiuLateral=[False,False]
                self.colidiuAbaixo = True
                if self.alturaMaxima>janela.get_height() - obstaculo.rect.bottom:
                    self.alturaMaxima = janela.get_height() - obstaculo.rect.bottom
            elif self.rect.bottom<obstaculo.rect.top:
                self.colidiuLateral=[False,False]
                self.alturaMinima=obstaculo.rect.top
                self.colidiuAcima = True
        elif self.rect.x+self.rect.w<obstaculo.rect.x or self.rect.x>obstaculo.rect.x+obstaculo.rect.w:
            self.colidiuLateral=[False,False]
            if self.colidiuAcima:    
                self.colidiuAcima=False
                self.noChao=False
                self.alturaMaxima=self.rect.height
                self.alturaMinima=janela.get_height()
            else:    
                self.colidiuAbaixo=False
                self.alturaMaxima=self.rect.h*5
            

        
    '''
    desenha o objeto e o ataque escolhido na janela e atualiza sua movimentação total
    '''
    def desenhar(self, janela):
        pygame.draw.rect(janela, (255,0,0), self.rect)
        if self.ataque[0] or self.ataque[1]:
            pygame.draw.rect(janela, (255,0,0), self.rectHitbox)
            if self.noChao:
                if self.ataque[0]:
                    if self.lado and not self.colidiuLateral[0]:
                        self.rect.x += 5
                    elif not self.lado and not self.colidiuLateral[1]:
                        self.rect.x -=5
                else:
                    if self.lado and not self.colidiuLateral[1]:
                        self.rect.x -= 5
                    elif not self.lado and not self.colidiuLateral[0]:
                        self.rect.x +=5
            self.ataque[0] = False
            self.ataque[1] = False
        if not self.noChao:
            self.pulo(10*60//frames)

class Obstaculo:
    '''
    rect = espaço que ocupa na tela
    '''
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
    '''
    Desenha o objeto na tela
    '''
    def desenhar(self, janela):
        pygame.draw.rect(janela, (0,255,0), self.rect)

            
'''
define velocidade inicial, tamanho da janela, ativa o loop principal do jogo,
define o numero de frames que o jogo vai rodar, inicia a verificação do tempo
e cria os objetos

o posicionamento sempre deve ser relativo ao tamanho da tela para evitar erros
ao redimensionar ela, por exemplo, ao colocar em tela cheia
'''      
velocidade = 0
screen = pygame.display.set_mode([750, 750])
running = True
frames = 30
relogio = pygame.time.Clock()
personagem = Personagem(screen,0,700,50,50)
obstaculo = Obstaculo(300,625,200,50)
obstaculo2 = Obstaculo(350, 500, 50, 50)
while running:
    relogio.tick(frames)
    #verificação dos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                personagem.pulo(10*30//frames)
            if event.key == K_LEFT:
                velocidade=-10*30//frames
            if event.key == K_RIGHT:
                velocidade=10*30//frames
            if event.key == K_SPACE:
                personagem.atacar()
            if event.key == K_b:
                personagem.atacarSonico()
        if event.type == KEYUP:
            if (event.key == K_LEFT or event.key == K_RIGHT):
                velocidade=0
    
    personagem.mover(screen, velocidade)
    personagem.colisaoObstaculo(obstaculo, screen)
 #   personagem.colisaoObstaculo(obstaculo2, screen)
    screen.fill((255, 255, 255))
    personagem.desenhar(screen)
    obstaculo.desenhar(screen)
    obstaculo2.desenhar(screen)
    pygame.display.flip()
    

    

# Done! Time to quit.
pygame.quit()
