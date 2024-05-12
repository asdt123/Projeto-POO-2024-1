from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 100

class Player(Nave):
  def __init__(self):
    super().__init__(VIDA_PLAYER, (250,250),"images/rocket.png")
    self.tiros = pygame.sprite.Group()
    

  def atacar(self, screen):
    self.tiros.add(Arsenal((self.rect.centerx, self.rect.top), "images/bullet.png", 5))

  def mover(self,velocidade):
    if self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.right>900 and velocidade[0]>0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.top<0 and velocidade[1]<0:
      self.rect.move_ip((velocidade[0], 0))
    elif self.rect.bottom>=600 and velocidade[1]>0:
      self.rect.move_ip((velocidade[0], 0))
    else:
      self.rect.move_ip(velocidade)
    
  def limite(self):
    pass
    
  def update(self,screen, aliens):
    self.tiros.draw(screen)
    self.tiros.update(aliens) 
    if self.vida <= 0:
      self.kill()
    