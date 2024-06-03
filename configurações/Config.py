import pygame

pygame.init()
relogio = pygame.time.Clock()

# Definições da janela

LARGURA = 900
ALTURA = 600

DIMENSÕES_TELA = (LARGURA,ALTURA)

TÍTULO = "Space Fighters"

FPS = 30
pygame.display.set_caption(TÍTULO)
screen = pygame.display.set_mode(DIMENSÕES_TELA)


# Imagens
#essas variaveis não atualizam valor ao longo da compilação, não servindo pra atualizar proporção nem posição
#encontrar outra alternativa pegado a variavel screen diretamente
NAVE_TAMANHO = (int(0.1422*screen.get_width()),int(0.2133*screen.get_height()))

INIMIGO_TAMANHO = (int(0.2133*LARGURA),int(0.1813*ALTURA))


BARRA_VIDA_P1 = [int(0.0278*LARGURA),int(0.1111*LARGURA),int(0.0417*ALTURA),int(0.0167*ALTURA)]
BARRA_VIDA_P2 = [int(0.7222*LARGURA),int(0.1111*LARGURA),int(0.0417*ALTURA),int(0.0167*ALTURA)]



CORES = {"Preto":(0,0,0),"Branco":(255,255,255),"Azul":(0,0,255),"Vermelho":(255,0,0),"Verde":(0,255,0),"Azul Escuro":(0,0,139)}

## Janelas ##

JANELAS = ["Menu Inicial 1","Menu Inicial 2","Fase 1"]


MOUSE_POS = (0,0)

# Atualiza todos os botões
def CAIXA(nome_caixa:str):
    
    # Retorno: (x,y,x_size,y_size)
    match nome_caixa:
      case "TÍTULO":
        return (int(0.3132*screen.get_width()),int(0.1484*screen.get_height()),int(0.3699*screen.get_width()),int(0.2371*screen.get_height()))
      case "CAMPANHA":
        return (int(0.3854*screen.get_width()),int(0.6374*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      case "VERSUS":
        return (int(0.3854*screen.get_width()),int(0.7420*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      case "SAIR":
        return (int(0.3854*screen.get_width()),int(0.8480*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      case "VIDA1":
        return (int(0.0278*LARGURA),int(0.1111*LARGURA),int(0.0417*ALTURA),int(0.0167*ALTURA))
      case _:
        return (0,0,0,0)

# Atualiza todas as mensagens
def MENSAGEM(nome_mensagem:str):

   # Retorno: (x,y) e (x_size,y_size)
  match nome_mensagem:
    case "ESPAÇO":
      return [(int(0.3013*screen.get_width()),int(0.7398*screen.get_height())),int((0.05*screen.get_width()+0.05*screen.get_height())/2)]
    case _:
      return [(0,0),0]
