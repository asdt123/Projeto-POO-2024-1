import pygame
from Player import Player
from Nave import WIDTH
from Nave import HEIGHT

relogio = pygame.time.Clock()

X_INICIAL_NAVE = 430-64
Y_INICIAL_NAVE = 550-64
X_INICIAL_TIRO = X_INICIAL_NAVE + 2*8 + 4
Y_INICIAL_TIRO = Y_INICIAL_NAVE

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Interestelar")
player = Player()

# Tiro
tiro_img = pygame.image.load("images/bullet.png")
posição_inicial = [X_INICIAL_TIRO,Y_INICIAL_TIRO]

player_tiro_img = [tiro_img]
posição_tiro = [posição_inicial]
posição_tiro_mov = [X_INICIAL_TIRO,Y_INICIAL_TIRO]
delta_Y = [0]
x = [0]
y = [0]

aux = 0
running = True
while running:

  relogio.tick(30)
  backgraound = pygame.image.load("images/stars.jpg") 
  screen.blit(backgraound,(0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running == False

    deltas_nave = player.mover(event)

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        delta_Y[aux] = -5
        delta_Y.append(0)
        posição_tiro.append(posição_inicial)
        x[aux] = player.posição_nave[0] + deltas_nave[0] + 2*8 + 4
        y[aux] = player.posição_nave[1] + deltas_nave[1]
        x.append(0)
        y.append(0) 
        aux += 1

  player.posição_nave[0] += deltas_nave[0]
  player.posição_nave[1] += deltas_nave[1]

  posição_tiro_mov[0] += deltas_nave[0]
  posição_tiro_mov[1] += deltas_nave[1]    

  for i in range(0,aux+1):
    
    posição_tiro[i][0] = x[i]
    posição_tiro[i][1] += delta_Y[i]

    ''' 
    posição_tiro[i][0] = posição_tiro_mov[0] 
    posição_tiro[i][1] = posição_tiro_mov[1]
    '''

    screen.blit(player_tiro_img[i],(posição_tiro[i][0],posição_tiro[i][1]))
    player_tiro_img.append(tiro_img)

  for i in range(0,aux+1):
    if posição_tiro[i][1] <= 0:
      posição_tiro[i] = [X_INICIAL_TIRO,Y_INICIAL_TIRO]
      delta_Y[i] = 0
  
  player.show(screen)
  player.limite()
  pygame.display.update()

pygame.quit()
