import pygame
from Player import Player
from Alien import Alien
import random

#inicialização pygames
pygame.init()
relogio = pygame.time.Clock()

#definiçao da tela
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Interestelar")

#criação do sprite do jogador
player = Player()
players = pygame.sprite.Group()
players.add(player)

#definição do background
background = pygame.image.load("images/stars.jpg") 
aliens = pygame.sprite.Group() 
#loop principal
running = True
while running:
  #frames
  relogio.tick(30)

  
  #criação dos inimigos, sujeito a alteração
  if len(aliens)<2:
    aliens.add(Alien((random.randint(50,800),-30)))
  screen.blit(background,(0,0))


  #analise do teclado para controle do personagem
  key=pygame.key.get_pressed()
  if key[pygame.K_UP]:     # Andar para cima
    player.mover((0,-10))
  if key[pygame.K_DOWN]:   # Andar para baixo
    player.mover((0,10))
  if key[pygame.K_RIGHT]:  # Andar para direita
    player.mover((10,0))
  if key[pygame.K_LEFT]:   # Andar para esquerda
    player.mover((-10,0))
  if key[pygame.K_SPACE]:   # Andar para esquerda
    player.atacar(screen)
  else:
    pass

  #analise dos demais eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
  
  #desenho dos sprites, da pra colocar numa função depois
  player.image
  players.draw(screen)
  players.update(screen, aliens)
  aliens.draw(screen)
  aliens.update(screen, players)
  pygame.display.flip()

pygame.quit()
