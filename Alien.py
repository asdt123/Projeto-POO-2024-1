from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 50
DANO_PLAYER = 20

class Alien(Nave):
  def __init__(self, posição_inicial):
    super().__init__(VIDA_PLAYER, posição_inicial,"images/alien.png")
    self.tiros = pygame.sprite.Group()
    

  def atacar(self, screen):
    pass
    
      
  def mover(self):
    pass
    
  def limite(self):
    pass
    
  def update(self):
    self.rect.move_ip(0,10)
    if self.vida <= 0 or self.rect.top>550:
        self.kill()
    