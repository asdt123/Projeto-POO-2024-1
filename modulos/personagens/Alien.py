from configurações.Config import *
from .Nave import Nave
from .Arsenal import Arsenal
from .Player import Player
from .Drops import Drops
import pygame
import random



class Alien(Nave):
  def __init__(self,posição_inicial:int,tipo_alien:int)->None:
    #definição da animação e qual alien vai ser gerado(0 pra ufo e 1 pro roxo)
    self.tipo_alien = tipo_alien
    self.index = 0
    self.img_anim = []
    for i in range(2):
      self.img_anim.append(pygame.transform.scale(pygame.image.load(imagens_aliens).subsurface((i*64,self.tipo_alien*64),(64,64)).convert_alpha(), self.tamanho_alien()))
    super().__init__(VIDA_ALIEN[self.tipo_alien], posição_inicial,self.img_anim[self.index])
    self.rect.bottom = -30

    if self.rect.left+self.rect.w>screen.get_width() - screen.get_width()//6: 
      self.rect.left = screen.get_width() - screen.get_width()//6 - self.rect.w
    #grupo pra sprites de tiro
    self.tiros = pygame.sprite.Group()
    self.pontos = 100

    
    self.vel_alien = [screen.get_height()//100,screen.get_height()//100]
    
  #define o tipo de ataque e arma a partir do tipo de alien
  def atacar(self)->None:
    #sai um tiro a cada 5ms, não dá muito certo isso aqui mas ta bom por enquanto
    match self.tipo_alien:
      #tiro duplo
      case 0:
        if self.ciclo%6 == 0:
          for i in range(2):
            self.tiros.add(Arsenal((self.rect.centerx+15-i*15, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180+30-60*i ))
      #tiro metralhadora
      case 1:
        if self.ciclo%5 == 0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], random.randint(165,195)))  
      #tiro unico 
      case 2:
        if self.ciclo%5 == 0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.bottom), municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180))  
      #tiro triplo
      case 3:
        if self.ciclo%10 == 0:
          for i in range(3):
            self.tiros.add(Arsenal((self.rect.centerx+screen.get_height()//30*(-1+i), self.rect.bottom-screen.get_height()//30),  municao_aliens, self.tipo_alien, DANO_ALIEN[self.tipo_alien], 180))

  #metodo para atualizar a vida
  def receber_dano(self,dano:int)->int:
    #recebe dano e fica vermelho por um curto periodo
    super().receber_dano(dano)
    if self.vida <= 0:
      if random.randint(0,10)//1<3:
        drops.add(Drops(municao_aliens, self.rect.center,random.choice([self.tipo_alien, 100])))
      return self.pontos
    return 0

  #metodo para definir movimento a partir do tipo de alien (em construção)  
  def mover(self)->None:
    if self.tipo_alien==0:
      #movimenta pra baixo
      self.rect.move_ip(0,self.vel_alien[1])
    elif self.tipo_alien==1:
      if self.ciclo%8<6:
        self.vel_alien[1]=screen.get_height()//100
      else:
        self.vel_alien[1]=-screen.get_height()//100
      #movimenta para lado
      if self.rect.left<=screen.get_width()//6 or self.rect.right>=screen.get_width() - screen.get_width()//6:
        self.vel_alien[0]=-self.vel_alien[0]
      self.rect.move_ip(self.vel_alien[0],self.vel_alien[1])
    elif self.tipo_alien==2:
      #movimenta para lado
      if self.rect.left<=screen.get_width()//6 or self.rect.right>=screen.get_width() - screen.get_width()//6:
        self.vel_alien[0]=-self.vel_alien[0]
      self.rect.move_ip(self.vel_alien[0],self.vel_alien[1])
    elif self.tipo_alien==3:
      #movimenta para lado
      if self.rect.left<=screen.get_width()//6 or self.rect.right>=screen.get_width() - screen.get_width()//6:
        self.vel_alien[0]=-self.vel_alien[0]
      self.rect.move_ip(self.vel_alien[0],self.vel_alien[1])

  #metodo para ajustar tamanho do sprite apos mudança de tela
  def tamanho_alien(self)->tuple[int,int]:
    return (screen.get_height()//7,screen.get_height()//7)
  
  #metodo para reposicionar apos mudança de tela
  def reposicionar(self, dimensões_antigas, dimensões_novas):
    #reposiciona os sprites dos aliens e dos tiros
    self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
    self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])
    for lista_tiros in self.tiros.sprites():
        lista_tiros.reposicionar(dimensões_antigas,dimensões_novas)

  #metodo para atualizar sprite ao longo da compilação
  def update(self,player:Player)->None:
    #variavel que acompanha ciclos de jogo
    self.ciclo+=1
    if self.ciclo>100:
      self.ciclo=0
    #cicla atraves das sprites e define a escala do sprite
    self.index += 0.2
    if self.index >= 2:
      self.index = 0
    self.image = pygame.transform.scale(self.img_anim[int(self.index)], self.tamanho_alien())

    #ajusta hitbox
    self.rect.w = self.image.get_width()
    self.rect.h = self.image.get_height()
    

    #verifica se acertou o jogador
    self.tiros.update(player)

    self.mover()

    #verifica se colidiu com o jogador pra tirar a vida dele
    inimigos_atingidos = pygame.sprite.spritecollide(self,player,0)
    for inimigo in inimigos_atingidos:
        inimigo.receber_dano(0.5)
    
    #atira
    if len(inimigos_atingidos) == 0:
       self.atacar()

    #desenha na tela
    self.tiros.draw(screen)

    #morre se sair da tela ou se perder a vida, colocar animação de explosão aqui
    if self.vida <= 0 or self.rect.top > screen.get_height():
        self.kill()
