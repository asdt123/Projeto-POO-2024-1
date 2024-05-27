from configurações.Config import *
from .Nave import Nave
from .Arsenal import Arsenal
from .Player import Player
import pygame
import random

VIDA_ALIEN = [100, 50]
DANO_PLAYER = 20

class Alien(Nave):
  def __init__(self,posição_inicial:tuple,tipo_alien:int)->None:
    #definição da animação e qual alien vai ser gerado(0 pra ufo e 1 pro roxo)
    self.tipo_alien = tipo_alien
    self.index = 0
    self.img_anim = []
    for i in range(8):
      self.img_anim.append(pygame.transform.scale(pygame.image.load("imagens/inimigos/inimigos.png").subsurface((i*64,self.tipo_alien*64),(64,64)), (64*3,64*1.7)))
    super().__init__(VIDA_ALIEN[self.tipo_alien], posição_inicial,self.img_anim[self.index])
    #grupo pra sprites de tiro
    self.tiros = pygame.sprite.Group()
    self.pontos = 100
    

  def atacar(self)->None:
    #sai um tiro a cada 5ms, não dá muito certo isso aqui mas ta bom por enquanto
    if self.tipo_alien == 1:
      if len(self.tiros.sprites()) < 8:
        for i in range(2):
          self.tiros.add(Arsenal((self.rect.centerx+15-i*15, self.rect.bottom), pygame.image.load("imagens/armamento/munições.png").subsurface((0,0),(24,24)), 5, 180+30-60*i ))
    else:  
      if len(self.tiros.sprites())<5:
        self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), pygame.image.load("imagens/armamento/munições.png").subsurface((0,0),(24,24)), 5, random.randint(165,195)))  

  def receber_dano(self,dano:int)->None:
    #recebe dano, deixei pra mover pra tras so pra gente visualizar
    self.rect.move_ip(0,-5)
    super().receber_dano(dano)
    if self.vida<=0:
      return self.pontos
    return 0
      
  def mover(self)->None:
    pass

  def update(self,screen:pygame.Surface,player:Player)->None:
    #movimenta pra baixo so
    self.rect.move_ip(0,6)

    #cicla atraves das sprites
    if self.index >= 7:
      self.index=0
    self.index+=0.5
    self.image = self.img_anim[int(self.index)]

    #atira
    #self.atacar()
    #verifica se acertou o jogador
    self.tiros.update(player)
    #verifica se colidiu com o jogador pra tirar a vida dele
    inimigos_atingidos = pygame.sprite.spritecollide(self,player,0)
    for inimigo in inimigos_atingidos:
        inimigo.receber_dano(0.5)

    #desenha na tela
    self.tiros.draw(screen)

    #morre se sair da tela ou se perder a vida, colocar animação de explosão aqui
    if self.vida <= 0 or self.rect.top>550:
        self.kill()