import pygame
import math

class Arsenal(pygame.sprite.Sprite):
  def __init__(self,posição_nave,imagem_tiro, poder,  velocidade = -15,angulo=0):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(imagem_tiro)
    self.image = pygame.transform.rotate(self.image,angulo)
    self.rect= self.image.get_rect()
    self.rect.center = posição_nave
    self.poder = poder 
    self.velocidade = velocidade

  def update(self, aliens):
    self.rect.move_ip(0, self.velocidade)
    inimigos_atingidos=pygame.sprite.spritecollide(self, aliens, 0)
    for alien in inimigos_atingidos:
        alien.receber_dano(self.poder)
    if self.rect.bottom < 0 or len(inimigos_atingidos) > 0:
        self.kill()