from .Nave import Nave
from .Arsenal import Arsenal
from configurações.Config import *
import pygame
import random

VIDA_PLAYER = 100

class Player(Nave):
  def __init__(self,posição_vida:int,skin:int)->None:
    #adicionando os sprites de animação
    self.skin = skin
    self.alternar_skin = 0
    self.img_anim = []
    for i in range(20):
      self.img_anim.append(pygame.image.load("imagens/jogadores/naves.png").subsurface((i%10*64,(self.skin+i//10)*64),(64,64)))
    #deinfindo o sprite inicial
    super().__init__(VIDA_PLAYER,(250,250),self.img_anim[0])
    #grupo de sprites tiro
    self.tiros = pygame.sprite.Group()
    #auxilio visual para vida
    self.boxVida = pygame.Rect(posição_vida,25,self.vida,10)
    #total de pontos do jogador
    self.pontos = 0
    #esolha da munnição
    self.tipo_mun = [True, False, False, False, False]
    self.index_mun = 0
    

  def atacar(self)->None:
    #analisa a mutição ativa, cria objetos do tiro e adiciona ao grupo
    if self.skin < 8:
      self.alternar_skin = 10
    if self.tipo_mun[0]:
      self.tiros.add(Arsenal((self.rect.centerx, self.rect.top-10), pygame.image.load("imagens/armamento/munições.png").subsurface((0,0),(24,24)), 5))
    elif self.tipo_mun[1]:
      if len(self.tiros.sprites())<9:
        for i in range(3):
          self.tiros.add(Arsenal((self.rect.centerx+20-i*20, self.rect.top-10), pygame.image.load("imagens/armamento/munições.png").subsurface((24,0),(24,24)), 5, -30+30*i ))
    elif self.tipo_mun[2]:
      self.tiros.add(Arsenal((self.rect.centerx, self.rect.top-10), pygame.image.load("imagens/armamento/munições.png").subsurface((48,0),(24,24)), 5, random.randint(-30,30) ))
    elif self.tipo_mun[3]:
      if len(self.tiros.sprites())<12:
        for i in range(2):
          self.tiros.add(Arsenal((self.rect.centerx+15-i*30, self.rect.top-10), pygame.image.load("imagens/armamento/munições.png").subsurface((24,0),(24,24)), 5))


  def mover(self,velocidade:int)->None:
    #nova proporção do sprite
    proporção=(screen.get_height()//4.6875,screen.get_height()//4.6875)

    #ajusta a animação dependendo do movimento
    if velocidade[0] < 0 and velocidade[1] < 0:
      self.image = pygame.transform.scale(self.img_anim[self.alternar_skin+9], proporção)
    if velocidade[0] > 0 and velocidade[1] < 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+8], proporção)
    if velocidade[0] == 0 and velocidade[1] < 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+7], proporção)
    if velocidade[0] < 0 and velocidade[1] == 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+6], proporção)
    if velocidade[0] > 0 and velocidade[1] == 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+5], proporção)
    if velocidade[0] == 0 and velocidade[1] == 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+4], proporção)
    if velocidade[0] < 0 and velocidade[1] > 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+3], proporção)
    if velocidade[0] > 0 and velocidade[1] > 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+2], proporção)
    if velocidade[0] == 0 and velocidade[1] > 0:
      self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+1], proporção)

    #ajusta hitbox
    self.rect.w=self.image.get_width()
    self.rect.h=self.image.get_height()

    #verifica se o jogador não ultrapassou os limites da tela
    if self.rect.top<0 and velocidade[1]<0 and self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0, 0))
    elif self.rect.bottom>screen.get_height() and velocidade[1]>0 and self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0, 0))
    elif self.rect.top<0 and velocidade[1]<0 and self.rect.right>screen.get_width()-2 and velocidade[0]>0:
      self.rect.move_ip((0, 0))
    elif self.rect.bottom>screen.get_height() and velocidade[1]>0 and self.rect.right>screen.get_width()-5  and velocidade[0]>0:
      self.rect.move_ip((0, 0))
    elif self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.right>screen.get_width()-5 and velocidade[0]>0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.top<0 and velocidade[1]<0:
      self.rect.move_ip((velocidade[0], 0))
    elif self.rect.bottom>screen.get_height() and velocidade[1]>0:
      self.rect.move_ip((velocidade[0], 0))
    else:
      self.rect.move_ip(velocidade)

    
    
  def update(self,screen:pygame.Surface,aliens:pygame.sprite.Group)->None:
    #mostra na tela a vida do jogador
    self.boxVida.update(self.boxVida.left,25,self.vida*2, 20)
    pygame.draw.rect(screen,(255,0,0),self.boxVida)
    
    #ativa apenas uma munição
    for i in range(len(self.tipo_mun)):
        self.tipo_mun[i] = False
        if i == self.index_mun%5:
          self.tipo_mun[i] = True

    #recupera a vida ate 40% mais ou menos, uma mamata
    if pygame.time.get_ticks()%30 == 0 and self.vida<40:
      self.vida += 3

    #desenha os tiros na tela e verifica se acertou um alien
    self.tiros.draw(screen)
    self.tiros.update(aliens,self)

    #imprime a pontuação
    fonte = pygame.font.SysFont("Monospace", 18, True, True)
    mensagem = f"Pontuação: {self.pontos}"
    format_text = fonte.render(mensagem, False, (255,255,255))
    screen.blit(format_text,(self.boxVida.left,60))

    self.alternar_skin = 0

    #verifica se morreu e não tem o qque fazer quando morre, se pa voltar pro menu inicial
    if self.vida <= 0:
      self.kill()
    