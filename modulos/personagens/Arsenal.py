import pygame
import math
from configurações.Config import *

class Arsenal(pygame.sprite.Sprite):
  def __init__(self,posição_nave:tuple,endereço_tiro:str, id_tiro: int,poder:int,angulo = 0)->None:
    pygame.sprite.Sprite.__init__(self)
    
    #carrega imagem do tiro, escala ela a partir do tamanho da janela e rotaciona ela a partir do angulo
    self.index=0
    self.img_anim=[]
    for i in range(4):
      self.img_anim.append(pygame.transform.scale(pygame.image.load(endereço_tiro).subsurface((i*64,id_tiro*64),(64,64)).convert_alpha(), tamanho_municao()))
    self.image = pygame.transform.rotate(self.img_anim[self.index], angulo)
    self.rect = self.image.get_rect()
    self.rect.center = posição_nave
    
    #definição do dano, da velocidade e do angulo do tiro
    self.poder = poder 
    self.velocidade = -1*(tamanho_municao()[0]+1)
    self.angulo = angulo

  def reposicionar(self, dimensões_antigas, dimensões_novas):
    self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
    self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])

  
  def update(self,inimigos,aliado = None)->None:
    self.index+=0.7
    if self.index > 3:
      self.index=0
    self.image = pygame.transform.scale(self.img_anim[int(self.index)], tamanho_municao())
    self.image = pygame.transform.rotate(self.img_anim[int(self.index)], self.angulo)
    self.rect = self.image.get_rect()


    #movimenta o tiro dependendo do angulo e da velocidade
    
    self.velocidade=-1*(tamanho_municao()[0]+1)
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
       

