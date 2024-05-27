import pygame
import math
from configurações.Config import *

class Arsenal(pygame.sprite.Sprite):
  def __init__(self,posição_nave:tuple,imagem_tiro:str,poder:int,angulo = 0,velocidade = -25)->None:
    pygame.sprite.Sprite.__init__(self)
    proporção=(screen.get_height()//25,screen.get_height()//25)

    #carrega imagem do tiro, escala ela a partir do tamanho da janela e rotaciona ela a partir do angulo
    self.image = pygame.transform.scale(imagem_tiro,proporção)
    self.image = pygame.transform.rotate(self.image,angulo)
    self.rect = self.image.get_rect()
    self.rect.center = posição_nave
    
    #definição do dano, da velocidade e do angulo do tiro
    self.poder = poder 
    self.velocidade = -1*(proporção[0]+1)
    self.angulo = angulo

  
  def update(self,inimigos,aliado = None)->None:
    proporção=(screen.get_height()//25,screen.get_height()//25)
    #movimenta o tiro dependendo do angulo e da velocidade
    self.velocidade=-1*(proporção[0]+1)
    self.rect.move_ip(math.sin(math.radians(self.angulo))*self.velocidade, math.cos(math.radians(self.angulo))*self.velocidade)
    #verifica se atingiu algum inimigo, dando dano nele e matando o sprite
    inimigos_atingidos = pygame.sprite.spritecollide(self,inimigos, 0)
    if aliado != None:
      for inimigo in inimigos_atingidos:
          aliado.pontos += inimigo.receber_dano(self.poder)
    else:
      for inimigo in inimigos_atingidos:
          inimigo.receber_dano(self.poder)
    
    if self.rect.bottom < -30 or self.rect.bottom > screen.get_height() or len(inimigos_atingidos) > 0:  
      self.kill()
       

