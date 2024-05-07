import abc from ABC, abstractmethod
import pygame
class Nave(ABC):
  def __init__(self,vida,poder,posição_nave,imagem_nave):
    self.vida = vida
    self.poder = poder
    self.rectHitbox = pygame.rect(posição_nave,(50,50))    

  @abstractmethod
  def atacar(self):
    pass

  @abstractmethod
  def mover(event):
    pass

  @abstractmethod
  def limite(self):
    pass

  def show(self, screen):
    screen.
    
