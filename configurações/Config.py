import pygame

pygame.init()
relogio = pygame.time.Clock()

# Definições da janela

TÍTULO = "Space Fighters"

FPS = 30
pygame.display.set_caption(TÍTULO)
screen = pygame.display.set_mode((900,600))

# Logo para a janela do jogo
#screen = pygame.display.set_icon()

#definições sprites
#players
players = pygame.sprite.Group()
VIDA_PLAYER = 100
imagens_naves = "imagens/jogadores/naves.png"
morte_naves = "imagens/morte/morte_naves.png"
municao_naves = "imagens/armamento/munições.png"
imagens_naves_selecao = "imagens/jogadores/naves_selecao.png"


#aliens
aliens = pygame.sprite.Group()
VIDA_ALIEN = [100, 75, 120, 50]
DANO_ALIEN = [2, 1, 4, 1]
imagens_aliens = "imagens/inimigos/inimigos.png"
morte_aliens = ""
municao_aliens = "imagens/armamento/munições.png"

#drops
drops = pygame.sprite.Group()

# backgorund 
background = "imagens/cenário/Cenarios.png"
background_altura, background_largura = 2500, 128

## Cores ##

CORES = {"Preto":(0,0,0),
         "Branco":(255,255,255),
         "Azul":(0,0,255),
         "Vermelho":(255,0,0),
         "Verde":(0,255,0),
         "Azul Escuro":(0,0,139),
         "Azul do ceu":(135,206,235)}
