from .Nave import Nave
from .Arsenal import Arsenal
from configurações.Config import *
import pygame
import random



class Player(Nave):
  def __init__(self,tipo_player:int,skin:int)->None:
    #adicionando os sprites de animação
    self.skin = skin
    self.alternar_skin = 0
    self.tipo_player = tipo_player

    #sprites normais
    #até a 4 skin tem animação de tiro diferente, o resto não
    self.img_anim = []
    if self.skin<8:
      for i in range(20):
        self.img_anim.append(pygame.image.load(imagens_naves).subsurface((i%10*64,(self.skin+i//10)*64),(64,64)).convert_alpha())
    else:
      for i in range(10):
        self.img_anim.append(pygame.image.load(imagens_naves).subsurface((i%10*64,self.skin*64),(64,64)).convert_alpha())

    #sprites de morte
    self.index_morte = 0
    self.img_anim_morte = []
    if self.skin<8:
      #sprites pros modelos com animação de tiro
      for i in range(4):
        self.img_anim_morte.append(pygame.image.load(morte_naves).subsurface((i*64,(self.skin//2)*64),(64,64)).convert_alpha())
    else:
      #sprites pros modelos sem animação de tiro
      for i in range(4):
        self.img_anim_morte.append(pygame.image.load(morte_naves).subsurface((i*64,(self.skin-4)*64),(64,64)).convert_alpha())
    
    #definindo o sprite inicial
    super().__init__(VIDA_PLAYER,(250,250),self.img_anim[0])
    
    #grupo de sprites tiro
    self.tiros = pygame.sprite.Group()
    
    #auxilio visual para vida
    self.boxVida = pygame.Rect(barra_vida(self.tipo_player, self.vida))
    
    #total de pontos do jogador
    self.pontos = 0
    
    #sprites pros modelos com animação de tiro
    self.tipo_mun_spr = []
    for i in range(2):
      self.tipo_mun_spr.append(pygame.image.load(municao_naves).subsurface((64,i*64),(64,64)).convert_alpha())
      self.tipo_mun_spr.append(pygame.image.load(municao_naves).subsurface((64,64),(64,64)).convert_alpha())

    #escolha da munição
    self.tipo_mun = ['inf', 60, 60, 60]
    self.mun_ativ = 0
    

  def atacar(self)->None:
    #analisa se o jogador está vivo, a munição ativa, cria objetos do tiro e adiciona ao grupo
    if self.vida>0:
      if self.skin < 8:
        self.alternar_skin = 10
      #depois troco isso, quando acabar de fazer mais munição. da pra otimizar muito
      #tiro unico energia
      if self.mun_ativ==0:
        if self.ciclo%2==0 and self.tipo_mun[self.mun_ativ]!=0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.top-screen.get_height()//30),  municao_naves, 0, 5))
          if self.tipo_mun[self.mun_ativ]!='inf':
            self.tipo_mun[self.mun_ativ]-=1
      #tiro triplo
      elif self.mun_ativ==1:
        if self.ciclo%5==0 and self.tipo_mun[self.mun_ativ]!=0:
          for i in range(3):
            self.tiros.add(Arsenal((self.rect.centerx+screen.get_height()//60*(1-i), self.rect.top-screen.get_height()//30),  municao_aliens, 1, 5, -30+30*i ))
            if self.tipo_mun[self.mun_ativ]!='inf':
              self.tipo_mun[self.mun_ativ]-=1
      #tiro metralhadora
      elif self.mun_ativ==2:
        if self.ciclo%1==0 and self.tipo_mun[self.mun_ativ]!=0:
          self.tiros.add(Arsenal((self.rect.centerx, self.rect.top-screen.get_height()//30), municao_aliens, 1, 5, random.randint(-30,30) ))
          if self.tipo_mun[self.mun_ativ]!='inf':
            self.tipo_mun[self.mun_ativ]-=1
      #tiro duplo
      elif self.mun_ativ==3:
        if self.ciclo%3==0 and self.tipo_mun[self.mun_ativ]!=0:
          for i in range(2):
            self.tiros.add(Arsenal((self.rect.centerx+screen.get_height()//30*(1-i*2), self.rect.top-screen.get_height()//30), municao_aliens, 1, 5))
            if self.tipo_mun[self.mun_ativ]!='inf':
              self.tipo_mun[self.mun_ativ]-=1
    if self.tipo_mun[self.mun_ativ]==0:
      self.trocar_munição(1)

  def mover(self,velocidade:int)->None:
    #analisa se o jogador ta vivo e faz o movimento mudando a sprite conforme movimento
    if self.vida>0:
      #ajusta a animação dependendo do movimento
      if velocidade[0] < 0 and velocidade[1] < 0:
        self.image = pygame.transform.scale(self.img_anim[self.alternar_skin+9], tamanho_nave())
      if velocidade[0] > 0 and velocidade[1] < 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+8], tamanho_nave())
      if velocidade[0] == 0 and velocidade[1] < 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+7], tamanho_nave())
      if velocidade[0] < 0 and velocidade[1] == 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+6], tamanho_nave())
      if velocidade[0] > 0 and velocidade[1] == 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+5], tamanho_nave())
      if velocidade[0] == 0 and velocidade[1] == 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+4], tamanho_nave())
      if velocidade[0] < 0 and velocidade[1] > 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+3], tamanho_nave())
      if velocidade[0] > 0 and velocidade[1] > 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+2], tamanho_nave())
      if velocidade[0] == 0 and velocidade[1] > 0:
        self.image =  pygame.transform.scale(self.img_anim[self.alternar_skin+1], tamanho_nave())

      #ajusta hitbox
      self.rect.w=self.image.get_width()
      self.rect.h=self.image.get_height()

      #verifica se o jogador não ultrapassou os limites da tela
      if self.rect.top<0 and velocidade[1]<0 and self.rect.left<0 and velocidade[0]<0:
        self.rect.move_ip((0, 0))
      elif self.rect.bottom>screen.get_height() and velocidade[1]>0 and self.rect.left<0 and velocidade[0]<0:
        self.rect.move_ip((0, 0))
      elif self.rect.top<0 and velocidade[1]<0 and self.rect.right>screen.get_width()-2 and velocidade[0]>0:
        self.rect.move_ip((0, 0))
      elif self.rect.bottom>screen.get_height() and velocidade[1]>0 and self.rect.right>screen.get_width()-5  and velocidade[0]>0:
        self.rect.move_ip((0, 0))
      elif self.rect.left<0 and velocidade[0]<0:
        self.rect.move_ip((0,velocidade[1]))
      elif self.rect.right>screen.get_width()-5 and velocidade[0]>0:
        self.rect.move_ip((0,velocidade[1]))
      elif self.rect.top<0 and velocidade[1]<0:
        self.rect.move_ip((velocidade[0], 0))
      elif self.rect.bottom>screen.get_height() and velocidade[1]>0:
        self.rect.move_ip((velocidade[0], 0))
      else:
        self.rect.move_ip(velocidade)

  def reposicionar(self, dimensões_antigas, dimensões_novas):
    #reposiciona os sprites dos aliens e dos tiros
    self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
    self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])
    for lista_tiros in self.tiros.sprites():
        lista_tiros.reposicionar(dimensões_antigas,dimensões_novas)

  def receber_dano(self,dano:int)->None:
    #recebe dano, deixei pra mover pra tras so pra gente visualizar
    super().receber_dano(dano)

  def trocar_munição(self, rumo):
    self.mun_ativ=((self.mun_ativ+rumo))%4
    while self.tipo_mun[self.mun_ativ]==0:
      self.mun_ativ=((self.mun_ativ+rumo))%4

  def receber_drop(self, id_drop):
    if id_drop==100:
      self.vida += 30
      if self.vida > 100:
        self.vida = 100
        return None
    elif self.tipo_mun[id_drop]!='inf':
      self.tipo_mun[id_drop]+=60
          
  def update(self,aliens:pygame.sprite.Group)->None:
    self.ciclo+=1
    if self.ciclo>100:
      self.ciclo=0

    #mostra na tela a vida do jogador
    self.boxVida.update(barra_vida(self.tipo_player, self.vida))
    pygame.draw.rect(screen,(255,0,0),self.boxVida)

    #recupera a vida ate 40% mais ou menos, uma mamata
    if self.ciclo%10==5 and self.vida<40 and self.vida>0:
      self.vida += 1

    #desenha os tiros na tela e verifica se acertou um alien
    self.tiros.draw(screen)
    self.tiros.update(aliens,self)

    #imprime a pontuação e a arma usada, temporario
    fonte = pygame.font.SysFont("Monospace", screen.get_width()//45, True, True)
    mensagem1 = f"Pontuação: {self.pontos}"
    mensagem2 = f"Munição: {self.tipo_mun[self.mun_ativ]}"
    format_text = fonte.render(mensagem1, False, (255,255,255))
    format_text2 = fonte.render(mensagem2, False, (255,255,255))

    screen.blit(format_text,(self.boxVida.left,self.boxVida.bottom+10))
    screen.blit(format_text2,(self.boxVida.left,self.boxVida.bottom+50))

    screen.blit(self.tipo_mun_spr[self.mun_ativ], (self.boxVida.left,self.boxVida.bottom+80) )



    self.alternar_skin = 0
    #verifica se morreu e não tem o qque fazer quando morre, se pa voltar pro menu inicial
    if self.vida <= 0:
      self.index_morte+=0.37
      self.image=pygame.transform.scale(self.img_anim_morte[int(self.index_morte)], tamanho_nave())
      if self.index_morte>=3.6:
        self.kill()
    