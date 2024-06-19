from configurações.Config import *
import pygame



class Animação(pygame.sprite.Sprite):
  def __init__(self,posição_inicial:int,tipo_animação:int)->None:
    pygame.sprite.Sprite.__init__(self)

    #definição da animação e qual animação vai ser gerado(0 pra ufo e 1 pro roxo)
    self.tipo_animação = tipo_animação
    self.index = 0

    #self.img_anim = []
    #for i in range(2):
      #self.img_anim.append(pygame.transform.scale(, (64*2,64*2)))

    self.image = pygame.image.load('imagens/animacao/nuvens.png').subsurface((0,self.tipo_animação*64),(64,64)).convert_alpha()
    self.image = pygame.transform.scale(self.image, self.tamanho_animação())
    self.rect = self.image.get_rect()
    self.rect.left = posição_inicial
    self.rect.bottom = -30
    if self.rect.left+self.rect.w>screen.get_width() - screen.get_width()//6: 
      self.rect.left = screen.get_width() - screen.get_width()//6 - self.rect.w

  #metodo para definir movimento a partir do tipo de animação (em construção)  
  def mover(self)->None:
    #movimenta pra baixo
    if self.tipo_animação<4:
        self.rect.move_ip(0,screen.get_height()//100)

  #metodo para ajustar tamanho do sprite apos mudança de tela
  def tamanho_animação(self)->tuple[int,int]:
    return (screen.get_height()//5,screen.get_height()//5)
  
  #metodo para reposicionar apos mudança de tela
  def reposicionar(self, dimensões_antigas, dimensões_novas)->None:
    #reposiciona os sprites dos animaçãos e dos tiros
    self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
    self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])

  #metodo para atualizar sprite ao longo da compilação
  def update(self)->None:
    
    self.image = pygame.transform.scale(self.image, self.tamanho_animação())
    self.rect.w, self.rect.h = self.tamanho_animação()

    self.mover()

    #ajusta hitbox
    self.rect.w = self.image.get_width()
    self.rect.h = self.image.get_height()

    #morre se sair da tela ou se perder a vida, colocar animação de explosão aqui
    if self.rect.top > screen.get_height():
        self.kill()
