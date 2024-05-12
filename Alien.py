from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 50
DANO_PLAYER = 20

class Alien(Nave):
  def __init__(self, posição_inicial):
    super().__init__(VIDA_PLAYER, posição_inicial,"images/alien.png")
    self.tiros = pygame.sprite.Group()
    self.tempo = 0
    

  def atacar(self, player):
    if pygame.time.get_ticks()%5==0:
      self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), "images/bullet.png", 5, 25, 180))
    self.tiros.update(player)  

  def receber_dano(self, dano):
    self.rect.move_ip(0,-5)
    super().receber_dano(dano)
      
  def mover(self):
    pass
    
  def limite(self):
    pass
    
  def update(self, screen, player):
    self.rect.move_ip(0,10)
    self.atacar(player)
    self.tiros.draw(screen)
    if self.vida <= 0 or self.rect.top>550:
        self.kill()
    