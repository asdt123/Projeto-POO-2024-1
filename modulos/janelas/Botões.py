import pygame
from modulos.janelas.Janelas import * 
from configurações.Config import *


class Botões():
  def __init__(self, id_box, texto=None, flag=None):
    #define como vai ser impresso na tela
    self.flag = flag

    #o id para verificar colisão
    self.id = id_box

    #informações de aparencia
    self.ressaltado = False
    self.rect= pygame.Rect(self.caixa())
    self.size = self.tamanho_letra()
    self.fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",self.size)
    self.texto= texto
    self.texto_imp = self.fonte.render(self.texto,True,CORES["Branco"])

  # Atualiza os tamanhos de todos os botões
  def caixa(self)->tuple[int,int,int,int]:
    #espaço
    if self.id == 0:
      return (screen.get_width()//2-screen.get_width()//5,screen.get_height()*0.6,screen.get_width()//2.5,screen.get_height()//15)
    
    #titulo
    if self.id == 1:
      return (screen.get_width()//4,screen.get_height()//5,screen.get_width()//2,screen.get_height()//6)
    
    #botão 1
    if self.id == 2 and not self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
    
    #botão 1
    elif self.id == 2 and self.ressaltado :
      return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
    
    #botão 2 
    if self.id == 3 and not self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
    
    #botão 2  
    elif self.id == 3 and self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
    
    #botão 3   
    if self.id == 4 and not self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//8,int(0.8*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
    
    #botão 3  
    if self.id == 4 and self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//8,int(0.8*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
    
    #jogador centro  
    if self.id == 5:
      return (screen.get_width()//2-screen.get_width()//8,screen.get_height()//20,screen.get_width()//4,screen.get_height()//10)
    
    #tecla A centro 
    if self.id == 6:
      return (screen.get_width()//4-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)
    
    #tecla D centro 
    if self.id == 7:
      return (3*screen.get_width()//4-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)    
    
    #pressione 
    if self.id == 8 and not self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)
    
    #pressione  
    elif self.id == 8 and self.ressaltado:
      return (screen.get_width()//2-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)
    
    #voltar
    if self.id == 9 and not self.ressaltado:
      return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height()),screen.get_width()//8,screen.get_height()//15)

    #voltar
    elif self.id == 9 and self.ressaltado:
      return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height())-screen.get_height()//60,screen.get_width()//8,screen.get_height()//10)

    #jogador 1 
    if self.id == 10:
      return (screen.get_width()//4-screen.get_width()//8,screen.get_height()//20,screen.get_width()//4,screen.get_height()//10)

    #tecla A canto 
    if self.id == 11:
      return (screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

    #tecla D canto 
    if self.id == 12:
      return (3*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)
    
    #pressionado player 1
    if self.id == 13 and not self.ressaltado:
      return (screen.get_width()//4-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)

    #pressionado player 1
    elif self.id == 13 and self.ressaltado:
      return (screen.get_width()//4-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)

    #jogador 2
    if self.id == 14:
      return (3*screen.get_width()//4-screen.get_width()//8,screen.get_height()//20,screen.get_width()//4,screen.get_height()//10)
    
    #tecla < 
    if self.id == 15:
      return (5*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

    #tecla > 
    if self.id == 16:
      return (7*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

    #pressionado player 2
    if self.id == 17 and not self.ressaltado:
      return (3*screen.get_width()//4-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)

    #pressionado player 2
    elif self.id == 17 and self.ressaltado:
      return (3*screen.get_width()//4-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)
    
    #voltar
    if self.id == 18 and not self.ressaltado:
      return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height()),screen.get_width()//8,screen.get_height()//15)

    #voltar
    elif self.id == 18 and self.ressaltado:
      return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height())-screen.get_height()//60,screen.get_width()//8,screen.get_height()//10)
    
    #divisoria
    if self.id == 19:
      return (screen.get_width()//2-screen.get_width()//200,-10,screen.get_width()//100 ,screen.get_height()+10)
    
    #pause
    if self.id == 20:
      return (5*screen.get_width()//6-screen.get_width()//18,int(0.1*screen.get_height()),screen.get_width()//20 ,screen.get_width()//20)

  def tamanho_letra(self):
     return int(6+3*(self.rect.h-8)//4)

  def mouse_porCima(self,pos):
    if self.rect.collidepoint(pos):
      if self.flag!='NORMAL' and self.flag!='ESTATICO':
        self.ressaltado=True
      return True
    if self.flag!='ESTATICO':
      self.ressaltado=False
      return False
    

  def mouse_click(self,botão):
    if self.flag=='ESTATICO' and botão == 1:
      self.ressaltado = not self.ressaltado
      return True
    elif self.ressaltado and botão == 1:
      return True 
    return False
 
  def alterar_texto(self, texto, flag=None):
     self.flag=flag
     self.texto=texto

  def update(self):
    self.rect.update(self.caixa())
    self.size = self.tamanho_letra()
    self.fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",self.size)
    if self.flag=='NORMAL':
      self.texto_imp = self.fonte.render(self.texto,True,CORES["Branco"])
    elif self.flag=='TITULO':
      self.texto_imp = self.fonte.render(self.texto,True,CORES["Verde"])
    elif self.flag=='ESPAÇO':
      self.texto_imp = self.fonte.render(self.texto,True,CORES["Vermelho"])
    elif self.flag=='BOX':
      pygame.draw.rect(screen,CORES["Branco"],self.rect,2)  
    else:
      if not self.ressaltado:
        pygame.draw.rect(screen,CORES["Branco"],self.rect,2)
        self.texto_imp = self.fonte.render(self.texto,True,CORES["Branco"])
      else:
        pygame.draw.rect(screen,CORES["Vermelho"],self.rect,2)
        self.texto_imp = self.fonte.render(self.texto,True,CORES["Vermelho"])

    texto_rect = self.texto_imp.get_rect(center = self.rect.center)
    screen.blit(self.texto_imp,texto_rect)