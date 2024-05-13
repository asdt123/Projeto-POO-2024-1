from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 100

class Player(Nave):
  def __init__(self):
    #adicionando os sprites de animação
    self.img_anim=[]
    for i in range(10):
      self.img_anim.append(pygame.image.load("images/navezinha.png").subsurface((i*64,0),(64,64)))
    #deinfindo o sprite inicial
    super().__init__(VIDA_PLAYER, (250,250),self.img_anim[0])
    #grupo de sprites tiro
    self.tiros = pygame.sprite.Group()
    #auxilio visual para vida
    self.boxVida = pygame.Rect(25,25,self.vida, 10)
    

  def atacar(self):
    #cria objetos do tiro e adiciona ao grupo
    self.tiros.add(Arsenal((self.rect.centerx, self.rect.top-10), "images/bullet.png", 5))

  def mover(self,velocidade):
    #verifica se o jogador não ultrapassou os limites da tela
    if self.rect.top<0 and velocidade[1]<0 and self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0, 0))
    elif self.rect.bottom>600 and velocidade[1]>0 and self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0, 0))
    elif self.rect.top<0 and velocidade[1]<0 and self.rect.right>900 and velocidade[0]>0:
      self.rect.move_ip((0, 0))
    elif self.rect.bottom>600 and velocidade[1]>0 and self.rect.right>900 and velocidade[0]>0:
      self.rect.move_ip((0, 0))
    elif self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.right>900 and velocidade[0]>0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.top<0 and velocidade[1]<0:
      self.rect.move_ip((velocidade[0], 0))
    elif self.rect.bottom>600 and velocidade[1]>0:
      self.rect.move_ip((velocidade[0], 0))
    else:
      self.rect.move_ip(velocidade)

    #ajusta a animação dependendo do movimento
    if velocidade==(-10,-10):
      self.image=self.img_anim[9]
    if velocidade==(10,-10):
      self.image=self.img_anim[8]
    if velocidade==(0,-10):
      self.image=self.img_anim[7]
    if velocidade==(-10,0):
      self.image=self.img_anim[6]
    if velocidade==(10,0):
      self.image=self.img_anim[5]
    if velocidade==(0,0):
      self.image=self.img_anim[4]
    if velocidade==(-10,10):
      self.image=self.img_anim[3]
    if velocidade==(10,10):
      self.image=self.img_anim[2]
    if velocidade==(0,10):
      self.image=self.img_anim[1]
    
    
  def update(self,screen, aliens):
    #mostra na tela a vida do jogador
    self.boxVida.update(25,25,self.vida*2, 20)
    pygame.draw.rect(screen, (255,0,0),self.boxVida)

    #recupera a vida ate 40% mais ou menos, uma mamata
    if pygame.time.get_ticks()%30==0 and self.vida<40:
      self.vida+=3

    #desenha os tiros na tela e verifica se acertou um alien
    self.tiros.draw(screen)
    self.tiros.update(aliens) 

    #verifica se morreu e não tem o qque fazer quando morre, se pa voltar pro menu inicial
    if self.vida <= 0:
      self.kill()
    