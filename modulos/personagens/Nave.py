from abc import ABC, abstractmethod
from configurações.Config import *
import pygame

class Nave(ABC,pygame.sprite.Sprite):
  def __init__(self,vida:int,posição_nave:int,imagem_nave:pygame.surface.Surface)->None:
    pygame.sprite.Sprite.__init__(self)
    #carrega imagem da nave
    self.image = imagem_nave
    self.rect = self.image.get_rect()
    self.rect.left = posição_nave

    self.vida = vida

    #index para animações automaticas
    self.index = 0

    #conta o ciclo de atualizações
    self.ciclo = 0

    #grupo de sprites tiro
    self.tiros = pygame.sprite.Group()

  def receber_dano(self,dano:int)->None:
    #atualiza o valor da vida e deixa vermelho
    self.image.fill((100,0,0,70),special_flags=pygame.BLEND_ADD)
    self.vida -= dano

  @abstractmethod
  def atacar(self)->None:
    pass

  @abstractmethod
  def mover(self)->None:
    pass


    
