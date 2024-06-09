from configurações.Config import *
from .Nave import Nave
from .Arsenal import Arsenal
from .Player import Player
from .Drops import Drops
import pygame
import random


class Alien(Nave):
  def __init__(self,posição_inicial:tuple,tipo_alien:int)->None:
    #definição da animação e qual alien vai ser gerado(0 pra ufo e 1 pro roxo)
    self.tipo_alien = tipo_alien
    self.index = 0
    self.img_anim = []
    for i in range(2):
      self.img_anim.append(pygame.transform.scale(pygame.image.load(imagens_aliens).subsurface((i*64,self.tipo_alien*64),(64,64)), (64*2,64*2)))
    super().__init__(VIDA_ALIEN[self.tipo_alien], posição_inicial,self.img_anim[self.index])
    #grupo pra sprites de tiro
    self.tiros = pygame.sprite.Group()
    self.pontos = 100
    

  def atacar(self)->None:
    #sai um tiro a cada 5ms, não dá muito certo isso aqui mas ta bom por enquanto
    self.ciclo+=1
    if self.ciclo>100:
      self.ciclo=0
    match self.tipo_alien:
      case 0:
        if self.ciclo%6 == 0:
          for i in range(2):
            self.tiros.add(Arsenal((self.rect.centerx+15-i*15, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180+30-60*i ))
      
      case 1:
        if self.ciclo%5 == 0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], random.randint(165,195)))  
          
      case 2:
        if self.ciclo%5 == 0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180))  

      case 3:
        if self.ciclo%10 == 0:
          for i in range(3):
            self.tiros.add(Arsenal((self.rect.centerx+screen.get_height()//30*(-1+i), self.rect.bottom-screen.get_height()//30),  municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180))


        
    
  def receber_dano(self,dano:int)->int:
    #recebe dano e fica vermelho por um curto periodo
    super().receber_dano(dano)
    if self.vida<=0:
      if random.randint(0,10)//1<3:
        drops.add(Drops(municao_aliens, self.rect.center,random.choice([self.tipo_alien, 100])))
      return self.pontos
    return 0
      
  def mover(self)->None:
    pass

  def reposicionar(self, dimensões_antigas, dimensões_novas):
    #reposiciona os sprites dos aliens e dos tiros
    self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
    self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])
    for lista_tiros in self.tiros.sprites():
        lista_tiros.reposicionar(dimensões_antigas,dimensões_novas)

  def update(self,player:Player)->None:
    #movimenta pra baixo
    self.rect.move_ip(0,screen.get_height()//100)

    #cicla atraves das sprites e define a escala do sprite
    self.index+=0.2
    if self.index >= 2:
      self.index=0
    self.image = pygame.transform.scale(self.img_anim[int(self.index)], tamanho_alien())

    #ajusta hitbox
    self.rect.w=self.image.get_width()
    self.rect.h=self.image.get_height()

    #verifica se acertou o jogador
    self.tiros.update(player)

    #verifica se colidiu com o jogador pra tirar a vida dele
    inimigos_atingidos = pygame.sprite.spritecollide(self,player,0)
    for inimigo in inimigos_atingidos:
        inimigo.receber_dano(0.5)
    
    #atira
    if len(inimigos_atingidos)==0:
       self.atacar()

    #desenha na tela
    self.tiros.draw(screen)

    #morre se sair da tela ou se perder a vida, colocar animação de explosão aqui
    if self.vida <= 0 or self.rect.top>screen.get_height():
        self.kill()
