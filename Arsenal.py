import pygame
import math

class Arsenal(pygame.sprite.Sprite):
  def __init__(self,posição_nave,imagem_tiro, poder,  velocidade = -25, angulo=0):
    pygame.sprite.Sprite.__init__(self)
    #carrega imagem do tiro, rotaciona ela a partir do angulo
    self.image = pygame.image.load(imagem_tiro)
    self.image = pygame.transform.rotate(self.image,angulo)
    self.rect= self.image.get_rect()
    self.rect.center = posição_nave
    #definição do dano, da velocidade e do angulo do tiro
    self.poder = poder 
    self.velocidade = velocidade
    self.angulo = angulo

  def update(self, inimigos):
    #movimenta o tiro dependendo do angulo e da velocidade
    self.rect.move_ip(math.sin(math.radians(self.angulo))*self.velocidade, math.cos(math.radians(self.angulo))*self.velocidade)
    #verifica se atingiu algum inimigo, dando dano nele e matando o sprite
    inimigos_atingidos=pygame.sprite.spritecollide(self, inimigos, 0)
    for inimigo in inimigos_atingidos:
        inimigo.receber_dano(self.poder)
    if self.rect.bottom < 0 or len(inimigos_atingidos) > 0:
        self.kill()