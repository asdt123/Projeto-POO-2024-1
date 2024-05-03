from Nave import Nave
import pygame

VIDA_PLAYER = 100
DANO_PLAYER = 20
PLAYER_TAMANHO = 64
TIRO_TAMANHO = 8
X_INICIAL_NAVE = 430-PLAYER_TAMANHO
Y_INICIAL_NAVE = 550-PLAYER_TAMANHO
X_INICIAL_TIRO = X_INICIAL_NAVE + 2*TIRO_TAMANHO + 4
Y_INICIAL_TIRO = Y_INICIAL_NAVE

class Player(Nave):
  def __init__(self):
    super().__init__(VIDA_PLAYER,DANO_PLAYER,[X_INICIAL_NAVE,Y_INICIAL_NAVE],
                     [X_INICIAL_TIRO,Y_INICIAL_TIRO],"images/rocket.png","images/bullet.png")

  def atacar(self,event):
    pass
      
  def mover(self,event):

    delta_x, delta_y = 0,0

    if event.type == pygame.KEYDOWN:   # Verifica se uma tecla foi aprtada
      if event.key == pygame.K_UP:     # Andar para cima
        delta_y = -10
      if event.key == pygame.K_DOWN:   # Andar para baixo
        delta_y = 10
      if event.key == pygame.K_RIGHT:  # Andar para direita
        delta_x = 10
      if event.key == pygame.K_LEFT:   # Andar para esquerda
        delta_x = -10
      else:
        pass

    if event.type == pygame.KEYUP:   # Parar após soltar a tecla
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        delta_x = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        delta_y = 0
      else:
        pass
      
    return [delta_x,delta_y]
    
  def limite(self):

    if self.posição_nave[0] >= 800 - PLAYER_TAMANHO: # Verifica se está no limite direito
      self.posição_nave[0] = 800 - PLAYER_TAMANHO
    elif self.posição_nave[0] < 0: # Verifica se está no limite esquerdo
      self.posição_nave[0] = 0
    else:
      pass
    if self.posição_nave[1] >= 600 - PLAYER_TAMANHO: # Verifica se está no limite inferior
      self.posição_nave[1] = 600 - PLAYER_TAMANHO
    elif self.posição_nave[1] < 0: # Verifica se está no limite superior
      self.posição_nave[1] = 0 
    else:
      pass

  def show(self,screen):
    player_img = pygame.image.load(self.imagem_nave)
    screen.blit(player_img,(self.posição_nave[0],self.posição_nave[1]))     
    