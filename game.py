import pygame
from modulos.personagens.Player import Player
from modulos.personagens.Alien import Alien
from modulos.janelas.Janelas import * 
from configurações.Config import *

#inicialização pygames
DIMENSÕES_TELA = screen.get_size()

janela = Janelas()

#definição do background

#loop principal
running = True
while running:
  #frames
  relogio.tick(FPS)

  #determinação da velocidade dependente do tamanho da tela(temporario)
  velocidade = screen.get_height()//46.15

  #analise do teclado para controle do personagem
  key = pygame.key.get_pressed()
  MOUSE_POS = pygame.mouse.get_pos()

  if key[pygame.K_1]:   # atacar
    player2.vida=0
  
  if key[pygame.K_d] and key[pygame.K_w]:  # Andar para direita e pra cima
    player2.mover((velocidade,-velocidade))
  elif key[pygame.K_d] and key[pygame.K_s]:  # Andar para direita e pra baixo
    player2.mover((velocidade,velocidade))
  elif key[pygame.K_a] and key[pygame.K_w]:  # Andar para esquerda e pra cima
    player2.mover((-velocidade,-velocidade))
  elif key[pygame.K_a] and key[pygame.K_s]:  # Andar para esquerda e pra baixo
    player2.mover((-velocidade,velocidade))
  elif key[pygame.K_w]:     # Andar para cima
    player2.mover((0,-velocidade))
  elif key[pygame.K_a]:   # Andar para esquerda
    player2.mover((-velocidade,0))
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
    player.mover((velocidade,-velocidade))
  elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:  # Andar para direita e pra baixo
    player.mover((velocidade,velocidade))
  elif key[pygame.K_LEFT] and key[pygame.K_UP]:  # Andar para esquerda e pra cima
    player.mover((-velocidade,-velocidade))
  elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:  # Andar para esquerda e pra baixo
    player.mover((-velocidade,velocidade))
  elif key[pygame.K_UP]:     # Andar para cima
    player.mover((0,-velocidade))
  elif key[pygame.K_LEFT]:   # Andar para esquerda
    player.mover((-velocidade,0))
  elif key[pygame.K_DOWN]:   # Andar para baixo
    player.mover((0,velocidade))
  elif key[pygame.K_RIGHT]:  # Andar para direita
    player.mover((velocidade,0))
  else:
    player.mover((0,0))

  if key[pygame.K_j] and not players.has(player):   # renascer
    player = Player(650, 1)
    players.add(player)

  #analise dos demais eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.WINDOWSIZECHANGED: #verfica se a tela mudou de tamanho
      DIMENSÕES_TELA_NOVA = (event.x, event.y)
      for lista_player in players.sprites():
        lista_player.reposicionar(DIMENSÕES_TELA,DIMENSÕES_TELA_NOVA)
      for lista_aliens in aliens.sprites():
        lista_aliens.reposicionar(DIMENSÕES_TELA,DIMENSÕES_TELA_NOVA)
      DIMENSÕES_TELA=DIMENSÕES_TELA_NOVA
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_k:
        player.index_mun += 1
      if event.key == pygame.K_TAB:
        player2.index_mun += 1
      if event.key == pygame.K_SPACE and janela.janela_atual == JANELAS[0]:
        janela.janela_atual = JANELAS[1]
    if event.type == pygame.MOUSEBUTTONDOWN and janela.janela_atual != JANELAS[0]:
      if event.button == 1:
        pass
  
  janela.atualizar_janela(MOUSE_POS,key)
  pygame.display.flip()

pygame.quit()