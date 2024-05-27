import pygame
from modulos.personagens.Player import Player
from modulos.personagens.Alien import Alien
from modulos.janelas.Janelas import * 
from configurações.Config import *

#inicialização pygames
relogio = pygame.time.Clock()



janela = Janelas(screen,"Fase 1")

#definição do background
aliens = pygame.sprite.Group() 

#loop principal
running = True
while running:
  #frames
  relogio.tick(FPS)

  janela.atualizar_janela()

  #determinação da velocidade dependente do tamanho da tela(temporario)
  velocidade=15

  #analise do teclado para controle do personagem
  key = pygame.key.get_pressed()

  if key[pygame.K_1]:   # atacar
    player2.atacar()
  
  if key[pygame.K_d] and key[pygame.K_w]:  # Andar para direita e pra cima
    player2.mover((velocidade,-1*velocidade))
  elif key[pygame.K_d] and key[pygame.K_s]:  # Andar para direita e pra baixo
    player2.mover((velocidade,velocidade))
  elif key[pygame.K_a] and key[pygame.K_w]:  # Andar para esquerda e pra cima
    player2.mover((-1*velocidade,-1*velocidade))
  elif key[pygame.K_a] and key[pygame.K_s]:  # Andar para esquerda e pra baixo
    player2.mover((-1*velocidade,velocidade))
  elif key[pygame.K_w]:     # Andar para cima
    player2.mover((0,-1*velocidade))
  elif key[pygame.K_a]:   # Andar para esquerda
    player2.mover((-1*velocidade,0))
  elif key[pygame.K_s]:   # Andar para baixo
    player2.mover((0,velocidade))
  elif key[pygame.K_d]:  # Andar para direita
    player2.mover((velocidade, 0))
  else:
    player2.mover((0,0))

  if key[pygame.K_2] and not players.has(player2):   # renascer
    player2 = Player(25,0)
    players.add(player2)

  if key[pygame.K_l]:   # atacar
    player.atacar()

  if key[pygame.K_RIGHT] and key[pygame.K_UP]:  # Andar para direita e pra cima
    player.mover((10,-10))
  elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:  # Andar para direita e pra baixo
    player.mover((10,10))
  elif key[pygame.K_LEFT] and key[pygame.K_UP]:  # Andar para esquerda e pra cima
    player.mover((-10,-10))
  elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:  # Andar para esquerda e pra baixo
    player.mover((-10,10))
  elif key[pygame.K_UP]:     # Andar para cima
    player.mover((0,-10))
  elif key[pygame.K_LEFT]:   # Andar para esquerda
    player.mover((-10,0))
  elif key[pygame.K_DOWN]:   # Andar para baixo
    player.mover((0,10))
  elif key[pygame.K_RIGHT]:  # Andar para direita
    player.mover((10,0))
  else:
    player.mover((0,0))

  if key[pygame.K_j] and not players.has(player):   # renascer
    player = Player(650, 1)
    players.add(player)

  #analise dos demais eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_k:
        player.index_mun += 1
      if event.key == pygame.K_TAB:
        player2.index_mun += 1
      if event.key == pygame.K_SPACE:
        ESCOLHE_JANELA += 1
  
  janela.mudar_janela(ESCOLHE_JANELA,(0,0))
  pygame.display.flip()

pygame.quit()