from abc import ABC, abstractmethod
import pygame

class Nave(ABC, pygame.sprite.Sprite):
  def __init__(self,vida,posição_nave,imagem_nave):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load(imagem_nave)
    self.rect= self.image.get_rect()
    self.rect.center = posição_nave
    self.vida = vida

  def receber_dano(self, dano):
    self.vida-=dano

  @abstractmethod
  def atacar(self):
    pass

  @abstractmethod
  def mover(self):
    pass

  @abstractmethod
  def limite(self):
    pass

    
