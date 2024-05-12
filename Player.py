from Nave import Nave
from Arsenal import Arsenal
import pygame

VIDA_PLAYER = 100

class Player(Nave):
  def __init__(self):
    self.img_anim=[]
    for i in range(10):
      self.img_anim.append(pygame.transform.scale(pygame.image.load("images/navezinha.png").subsurface((i*64,0),(64,64)),(64*2,64*2)))
    super().__init__(VIDA_PLAYER, (250,250),self.img_anim[0])
    self.tiros = pygame.sprite.Group()
    self.boxVida = pygame.Rect(25,25,self.vida, 10)
    

  def atacar(self, screen):
    self.tiros.add(Arsenal((self.rect.centerx, self.rect.top), "images/bullet.png", 5))

  def mover(self,velocidade):
    if self.rect.left<0 and velocidade[0]<0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.right>900 and velocidade[0]>0:
      self.rect.move_ip((0,velocidade[1]))
    elif self.rect.top<0 and velocidade[1]<0:
      self.rect.move_ip((velocidade[0], 0))
    elif self.rect.bottom>=600 and velocidade[1]>0:
      self.rect.move_ip((velocidade[0], 0))
    else:
      self.rect.move_ip(velocidade)

    if velocidade==(-10,-10):
      self.image=self.img_anim[9]
    if velocidade==(10,-10):
      self.image=self.img_anim[8]
    if velocidade==(0,-10):
      self.image=self.img_anim[7]
    if velocidade==(-10,0):
      self.image=self.img_anim[6]
    if velocidade==(10,0):
      self.image=self.img_anim[5]
    if velocidade==(0,0):
      self.image=self.img_anim[4]
    if velocidade==(-10,10):
      self.image=self.img_anim[3]
    if velocidade==(10,10):
      self.image=self.img_anim[2]
    if velocidade==(0,10):
      self.image=self.img_anim[1]
    



  def limite(self):
    pass
    
  def update(self,screen, aliens):
    self.boxVida.update(25,25,self.vida*2, 20)
    if pygame.time.get_ticks()%30==0 and self.vida<40:
      self.vida+=3
    pygame.draw.rect(screen, (255,0,0),self.boxVida)
    self.tiros.draw(screen);
    self.tiros.update(aliens) 
    if self.vida <= 0:
      self.kill()
      pygame.quit()
    