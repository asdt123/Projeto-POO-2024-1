import pygame

class Arsenal(pygame.sprite.Sprite):
  def __init__(self,posição_nave,imagem_tiro, poder):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(imagem_tiro)
    self.rect= self.image.get_rect()
    self.rect.center = posição_nave
    self.poder = poder 


  def update(self, velocidade, aliens):
    self.rect.move_ip(0,velocidade)
    inimigos_atingidos=pygame.sprite.spritecollide(self, aliens, 0)
    for alien in inimigos_atingidos:
        alien.receber_dano(self.poder)
    if self.rect.bottom < 0 or len(inimigos_atingidos) > 0:
        self.kill()