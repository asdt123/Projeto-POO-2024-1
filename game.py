import pygame
from modulos.janelas.Janelas import Janelas
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

  if janela.janela_atual == 8:
    
    if key[pygame.K_r]:   # atacar
      janela.player.atacar()
    
    if key[pygame.K_d] and key[pygame.K_w]:  # Andar para direita e pra cima
      janela.player.mover((velocidade,-velocidade))
    elif key[pygame.K_d] and key[pygame.K_s]:  # Andar para direita e pra baixo
      janela.player.mover((velocidade,velocidade))
    elif key[pygame.K_a] and key[pygame.K_w]:  # Andar para esquerda e pra cima
      janela.player.mover((-velocidade,-velocidade))
    elif key[pygame.K_a] and key[pygame.K_s]:  # Andar para esquerda e pra baixo
      janela.player.mover((-velocidade,velocidade))
    elif key[pygame.K_w]:     # Andar para cima
      janela.player.mover((0,-velocidade))
    elif key[pygame.K_a]:   # Andar para esquerda
      janela.player.mover((-velocidade,0))
    elif key[pygame.K_s]:   # Andar para baixo
      janela.player.mover((0,velocidade))
    elif key[pygame.K_d]:  # Andar para direita
      janela.player.mover((velocidade, 0))
    else:
      janela.player.mover((0,0))


    if key[pygame.K_l]:   # atacar
      janela.player2.atacar()

    if key[pygame.K_RIGHT] and key[pygame.K_UP]:  # Andar para direita e pra cima
      janela.player2.mover((velocidade,-velocidade))
    elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:  # Andar para direita e pra baixo
      janela.player2.mover((velocidade,velocidade))
    elif key[pygame.K_LEFT] and key[pygame.K_UP]:  # Andar para esquerda e pra cima
      janela.player2.mover((-velocidade,-velocidade))
    elif key[pygame.K_LEFT] and key[pygame.K_DOWN]:  # Andar para esquerda e pra baixo
      janela.player2.mover((-velocidade,velocidade))
    elif key[pygame.K_UP]:     # Andar para cima
      janela.player2.mover((0,-velocidade))
    elif key[pygame.K_LEFT]:   # Andar para esquerda
      janela.player2.mover((-velocidade,0))
    elif key[pygame.K_DOWN]:   # Andar para baixo
      janela.player2.mover((0,velocidade))
    elif key[pygame.K_RIGHT]:  # Andar para direita
      janela.player2.mover((velocidade,0))
    else:
      janela.player2.mover((0,0))

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
      for lista_animações in janela.animações.sprites():
        lista_animações.reposicionar(DIMENSÕES_TELA,DIMENSÕES_TELA_NOVA)

      DIMENSÕES_TELA = DIMENSÕES_TELA_NOVA
    
    if event.type == pygame.KEYDOWN:

      if janela.get_janela_atual() == 3 or janela.get_janela_atual() == 4:

        if event.key == pygame.K_a:
          janela.pegar_tecla_apertada([True,False,pygame.K_a])

        if event.key == pygame.K_b:
          janela.pegar_tecla_apertada([True,False,pygame.K_b])

        if event.key == pygame.K_c:
          janela.pegar_tecla_apertada([True,False,pygame.K_c])

        if event.key == pygame.K_d:
          janela.pegar_tecla_apertada([True,False,pygame.K_d])

        if event.key == pygame.K_e:
          janela.pegar_tecla_apertada([True,False,pygame.K_e])

        if event.key == pygame.K_f:
          janela.pegar_tecla_apertada([True,False,pygame.K_f])

        if event.key == pygame.K_g:
          janela.pegar_tecla_apertada([True,False,pygame.K_g])

        if event.key == pygame.K_h:
          janela.pegar_tecla_apertada([True,False,pygame.K_h])

        if event.key == pygame.K_i:
          janela.pegar_tecla_apertada([True,False,pygame.K_i])

        if event.key == pygame.K_j:
          janela.pegar_tecla_apertada([True,False,pygame.K_j])

        if event.key == pygame.K_k:
          janela.pegar_tecla_apertada([True,False,pygame.K_k])

        if event.key == pygame.K_l:
          janela.pegar_tecla_apertada([True,False,pygame.K_l])

        if event.key == pygame.K_m:
          janela.pegar_tecla_apertada([True,False,pygame.K_m])

        if event.key == pygame.K_n:
          janela.pegar_tecla_apertada([True,False,pygame.K_n])

        if event.key == pygame.K_o:
          janela.pegar_tecla_apertada([True,False,pygame.K_o])

        if event.key == pygame.K_p:
          janela.pegar_tecla_apertada([True,False,pygame.K_p])

        if event.key == pygame.K_q:
          janela.pegar_tecla_apertada([True,False,pygame.K_q])

        if event.key == pygame.K_r:
          janela.pegar_tecla_apertada([True,False,pygame.K_r])

        if event.key == pygame.K_s:
          janela.pegar_tecla_apertada([True,False,pygame.K_s])

        if event.key == pygame.K_t:
          janela.pegar_tecla_apertada([True,False,pygame.K_t])

        if event.key == pygame.K_u:
          janela.pegar_tecla_apertada([True,False,pygame.K_u])

        if event.key == pygame.K_v:
          janela.pegar_tecla_apertada([True,False,pygame.K_v])

        if event.key == pygame.K_w:
          janela.pegar_tecla_apertada([True,False,pygame.K_w])

        if event.key == pygame.K_x:
          janela.pegar_tecla_apertada([True,False,pygame.K_x])

        if event.key == pygame.K_y:
          janela.pegar_tecla_apertada([True,False,pygame.K_y])

        if event.key == pygame.K_z:
          janela.pegar_tecla_apertada([True,False,pygame.K_z])

        if event.key == pygame.K_BACKSPACE:
          janela.pegar_tecla_apertada([True,False,pygame.K_BACKSPACE])

        if event.key == pygame.K_SPACE:
          janela.pegar_tecla_apertada([True,False,pygame.K_SPACE])

        if event.key == pygame.K_RETURN:
          janela.pegar_tecla_apertada([True,False,pygame.K_RETURN])

      if event.key == pygame.K_k:
        janela.player2.trocar_munição(1)
      if event.key == pygame.K_j:
        janela.player2.trocar_munição(-1)
      if event.key == pygame.K_1:
        janela.player.trocar_munição(1)
      if event.key == pygame.K_2:
        janela.player.trocar_munição(-1)

      if event.key == pygame.K_SPACE and janela.janela_atual == 0:
        janela.janela_atual = 1

      if event.key == pygame.K_SPACE and (janela.janela_atual == 3 or janela.janela_atual == 4):
        janela.pegar_tecla_apertada([True,False,pygame.K_SPACE])

      if event.key == pygame.K_RIGHT and janela.janela_atual == 4:
        janela.pegar_tecla_apertada([True,False,pygame.K_RIGHT])

      if event.key == pygame.K_LEFT and janela.janela_atual == 4:
        janela.pegar_tecla_apertada([True,False,pygame.K_LEFT])

      if event.key == pygame.K_d and (janela.janela_atual == 3 or janela.janela_atual == 4):
        janela.pegar_tecla_apertada([True,False,pygame.K_d])

      if event.key == pygame.K_a and (janela.janela_atual == 3 or janela.janela_atual == 4):
        janela.pegar_tecla_apertada([True,False,pygame.K_a])

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_SPACE and (janela.janela_atual == 3 or janela.janela_atual == 4):
        janela.pegar_tecla_apertada([True,True,pygame.K_SPACE])

      if event.key == pygame.K_RIGHT and janela.janela_atual == 6:
        janela.pegar_tecla_apertada([True,True,pygame.K_RIGHT])

      if event.key == pygame.K_LEFT and janela.janela_atual == 6:
        janela.pegar_tecla_apertada([True,True,pygame.K_LEFT])

      if event.key == pygame.K_d and (janela.janela_atual == 5 or janela.janela_atual == 6):
        janela.pegar_tecla_apertada([True,True,pygame.K_d])

      if event.key == pygame.K_a and (janela.janela_atual == 5 or janela.janela_atual == 6):
        janela.pegar_tecla_apertada([True,True,pygame.K_a])

    if event.type == pygame.MOUSEMOTION and janela.janela_atual != 0:
      janela.pegar_mouse(event.pos)
    if event.type == pygame.MOUSEBUTTONDOWN:
      janela.pegar_mouse(event.pos, event.button)
  

  janela.atualizar_janela()

  pygame.display.flip()

pygame.quit()