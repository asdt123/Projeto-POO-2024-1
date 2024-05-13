from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 50
DANO_PLAYER = 20

class Alien(Nave):
  def __init__(self, posição_inicial, tipo_alien):
    #definição da animação e qual alien vai ser gerado(0 pra ufo e 1 pro roxo)
    self.index=0
    self.img_anim=[]
    for i in range(8):
      self.img_anim.append(pygame.transform.scale(pygame.image.load("images/inimigos.png").subsurface((i*64,tipo_alien*64),(64,64)), (64*2,64*2)))
    super().__init__(VIDA_PLAYER, posição_inicial,self.img_anim[self.index])
    #grupo pra sprites de tiro
    self.tiros = pygame.sprite.Group()
    

  def atacar(self, player):
    #sai um tiro a cada 5ms, não dá muito certo isso aqui mas ta bom por enquanto
    if pygame.time.get_ticks()%5==0:
      self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom-40), "images/bullet.png", 5, -25, 180))

    #verifica se acertou o jogador
    self.tiros.update(player)  

  def receber_dano(self, dano):
    #recebe dano, deixei pra mover pra tras so pra gente visualizar
    self.rect.move_ip(0,-5)
    super().receber_dano(dano)
      
  def mover(self):
    pass

  def update(self, screen, player):
    #movimenta pra baixo so
    self.rect.move_ip(0,10)

    #cicla atraves das sprites
    if self.index >= 7:
      self.index=0
    self.index+=0.5
    self.image = self.img_anim[int(self.index)]

    #atira
    self.atacar(player)

    #verifica se colidiu com o jogador pra tirar a vida dele
    inimigos_atingidos=pygame.sprite.spritecollide(self, player, 0)
    for inimigo in inimigos_atingidos:
        inimigo.receber_dano(0.5)

    #desenha na tela
    self.tiros.draw(screen)

    #morre se sair da tela ou se perder a vida, colocar animação de explosão aqui
    if self.vida <= 0 or self.rect.top>550:
        self.kill()
    