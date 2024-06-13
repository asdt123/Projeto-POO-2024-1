import pygame
from modulos.personagens.Player import Player
from modulos.personagens.Alien import Alien
from modulos.janelas.Janelas import * 
from configurações.Config import *

#inicialização pygames
DIMENSÕES_TELA = screen.get_size()

janela = Janelas()

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
  if janela.janela_atual == 6:
    if key[pygame.K_1]:   # atacar
      janela.player2.atacar()
    
    if key[pygame.K_d] and key[pygame.K_w]:  # Andar para direita e pra cima
      janela.player2.mover((velocidade,-velocidade))
    elif key[pygame.K_d] and key[pygame.K_s]:  # Andar para direita e pra baixo
      janela.player2.mover((velocidade,velocidade))
    elif key[pygame.K_a] and key[pygame.K_w]:  # Andar para esquerda e pra cima
      janela.player2.mover((-velocidade,-velocidade))
    elif key[pygame.K_a] and key[pygame.K_s]:  # Andar para esquerda e pra baixo
      janela.player2.mover((-velocidade,velocidade))
    elif key[pygame.K_w]:     # Andar para cima
      janela.player2.mover((0,-velocidade))
    elif key[pygame.K_a]:   # Andar para esquerda
      janela.player2.mover((-velocidade,0))
    elif key[pygame.K_s]:   # Andar para baixo
      janela.player2.mover((0,velocidade))
    elif key[pygame.K_d]:  # Andar para direita
      janela.player2.mover((velocidade, 0))
    else:
      janela.player2.mover((0,0))

    if key[pygame.K_2] and not players.has(janela.player2):   # renascer
      janela.player2 = Player(1,17)
      players.add(janela.player2)


    if key[pygame.K_l]:   # atacar
      janela.player.atacar()

    if key[pygame.K_RIGHT] and key[pygame.K_UP]:  # Andar para direita e pra cima
      janela.player.mover((velocidade,-velocidade))
    elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:  # Andar para direita e pra baixo
      janela.player.mover((velocidade,velocidade))
    elif key[pygame.K_LEFT] and key[pygame.K_UP]:  # Andar para esquerda e pra cima
      janela.player.mover((-velocidade,-velocidade))
    elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:  # Andar para esquerda e pra baixo
      janela.player.mover((-velocidade,velocidade))
    elif key[pygame.K_UP]:     # Andar para cima
      janela.player.mover((0,-velocidade))
    elif key[pygame.K_LEFT]:   # Andar para esquerda
      janela.player.mover((-velocidade,0))
    elif key[pygame.K_DOWN]:   # Andar para baixo
      janela.player.mover((0,velocidade))
    elif key[pygame.K_RIGHT]:  # Andar para direita
      janela.player.mover((velocidade,0))
    else:
      janela.player.mover((0,0))

    if key[pygame.K_j] and not players.has(janela.player):   # renascer
      janela.player = Player(0, 0)
      players.add(janela.player)

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
      for lista_drops in drops.sprites():
        lista_drops.reposicionar(DIMENSÕES_TELA,DIMENSÕES_TELA_NOVA)
      DIMENSÕES_TELA=DIMENSÕES_TELA_NOVA
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_k:
        janela.player.trocar_munição(1)
      if event.key == pygame.K_TAB:
        janela.player.trocar_munição(-1)
        #melhora o tratamento de eventos pra janela.
        #usa os metodos de pegar tecla aqui ou la em cima no controle de personagem
      if event.key == pygame.K_SPACE and janela.janela_atual == 0:
        janela.janela_atual = 1
      if event.key == pygame.K_SPACE and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[0] = True
        TECLAS_APERTADAS[2] = pygame.K_SPACE
      if event.key == pygame.K_RIGHT and janela.janela_atual == 4:
        TECLAS_APERTADAS[0] = True
        TECLAS_APERTADAS[2] = pygame.K_RIGHT
      if event.key == pygame.K_LEFT and janela.janela_atual == 4:
        TECLAS_APERTADAS[0] = True
        TECLAS_APERTADAS[2] = pygame.K_LEFT
      if event.key == pygame.K_d and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[0] = True
        TECLAS_APERTADAS[2] = pygame.K_d
      if event.key == pygame.K_a and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[0] = True
        TECLAS_APERTADAS[2] = pygame.K_a

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_k:
        janela.player.trocar_munição(1)
      if event.key == pygame.K_TAB:
        janela.player.trocar_munição(-1)
      if event.key == pygame.K_SPACE and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[1] = True
      if event.key == pygame.K_RIGHT and janela.janela_atual == 4:
        TECLAS_APERTADAS[1] = True
      if event.key == pygame.K_LEFT and janela.janela_atual == 4:
        TECLAS_APERTADAS[1] = True
      if event.key == pygame.K_d and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[1] = True
      if event.key == pygame.K_a and (janela.janela_atual == 3 or janela.janela_atual == 4):
        TECLAS_APERTADAS[1] = True

    if event.type == pygame.MOUSEBUTTONDOWN and janela.janela_atual != 0:
      #alterar aqui
      if event.button == 1:
        MOUSE_APERTADO[0] = True
        pass
        
    if event.type == pygame.MOUSEBUTTONUP and janela.janela_atual != 0:
      if event.button == 1:
        MOUSE_APERTADO[1] = True
        pass
  
    if MOUSE_APERTADO[0] == True and MOUSE_APERTADO[1] == True:
      MOUSE_APERTADO = [False,False]

    if TECLAS_APERTADAS[0] == True and TECLAS_APERTADAS[1] == True:
      TECLAS_APERTADAS = [False,False,pygame.K_0]

  janela.atualizar_janela(MOUSE_POS)
  janela.pegar_mouse_click(MOUSE_APERTADO)
  janela.pegar_tecla_apertada(TECLAS_APERTADAS)

  pygame.display.flip()

pygame.quit()