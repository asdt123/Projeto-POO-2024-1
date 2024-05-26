import pygame

pygame.init()

# Tela

MEDIDAS_TELA = pygame.display.Info()
#LARGURA = MEDIDAS_TELA.current_w
#ALTURA = MEDIDAS_TELA.current_h

LARGURA = 900
ALTURA = 600

DIMENSÕES_TELA = (LARGURA,ALTURA)

TÍTULO = "Space Fighters"

FPS = 30

BACKGROUND = pygame.image.load("imagens/cenário/stars.jpg")

# Imagens

NAVE_POSIÇÃO = (int(0.4270*LARGURA),int(0.7473*ALTURA))
NAVE_TAMANHO = (int(0.1422*LARGURA),int(0.2133*ALTURA))

INIMIGO_TAMANHO = (int(0.2133*LARGURA),int(0.1813*ALTURA))

MUNIÇÃO_TAMANHO = (int(0.0267*LARGURA),int(0.04*ALTURA))

BARRA_VIDA_P1 = [int(0.0278*LARGURA),int(0.1111*LARGURA),int(0.0417*ALTURA),int(0.0167*ALTURA)]
BARRA_VIDA_P2 = [int(0.7222*LARGURA),int(0.1111*LARGURA),int(0.0417*ALTURA),int(0.0167*ALTURA)]

# Janela 1

CAIXA_TÍTULO = (int(0.3132*LARGURA),int(0.1484*ALTURA),int(0.3699*LARGURA),int(0.2371*ALTURA))

MENSAGEM_POSIÇÃO = [(int(0.37*LARGURA),int(0.8105*ALTURA))]

CORES = {"Preto":(0,0,0),"Branco":(255,255,255),"Azul Escuro":(0,0,139)}

FONTE = pygame.font.SysFont("Monospace",38,True,True)

JANELAS = ["Menu Inicial 1","Menu Inicial 2","Fase 1"]

ESCOLHE_JANELA = 0

# Janela 2

CAIXA_CAMPANHA = (int(0.3854*LARGURA),int(0.6374*ALTURA),int(0.2295*LARGURA),int(0.0715*ALTURA))
CAIXA_VERSUS = (int(0.3854*LARGURA),int(0.7420*ALTURA),int(0.2295*LARGURA),int(0.0715*ALTURA))
CAIXA_SAIR = (int(0.3854*LARGURA),int(0.8480*ALTURA),int(0.2295*LARGURA),int(0.0715*ALTURA))

