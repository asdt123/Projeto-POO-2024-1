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

#definições sprites
#players
players = pygame.sprite.Group()
VIDA_PLAYER = 100
imagens_naves = "imagens/jogadores/naves.png"
morte_naves = "imagens/morte/morte_naves.png"
municao_naves = "imagens/armamento/munições.png"

#aliens
aliens = pygame.sprite.Group()
VIDA_ALIEN = [100, 50]
DANO_PLAYER = [20,20]
imagens_aliens = "imagens/inimigos/inimigos.png"
morte_aliens = ""
municao_aliens = "imagens/armamento/munições.png"
# Imagens
#essas variaveis não atualizam valor ao longo da compilação, não servindo pra atualizar proporção nem posição
#encontrar outra alternativa pegado a variavel screen diretamente

imagens_naves_selecao = "imagens/jogadores/naves_selecao.png"
background = "imagens/cenário/Cenarios.png"
background_altura, background_largura = 2500, 128

def tamanho_nave():
  return (screen.get_height()//6,screen.get_height()//6)

def tamanho_alien():
  return (screen.get_height()//4.6875,screen.get_height()//4.6875)

def tamanho_municao():
  return (screen.get_height()//25,screen.get_height()//25)

def barra_vida(tipo_player, vida):
  if tipo_player==0:
    return (screen.get_width()//36,screen.get_height()//24,(screen.get_width()//900)*vida, screen.get_height()//30)
  else:
    return (screen.get_width()//1.2,screen.get_height()//24,(screen.get_width()//900)*vida, screen.get_height()//30)




CORES = {"Preto":(0,0,0),
         "Branco":(255,255,255),
         "Azul":(0,0,255),
         "Vermelho":(255,0,0),
         "Verde":(0,255,0),
         "Azul Escuro":(0,0,139)}

## Janelas ##

JANELAS = ["Menu Inicial 1",
           "Menu Inicial 2",
           "Fase 1"]


MOUSE_POS = (0,0)

# Atualiza todos os botões
def CAIXA(nome_caixa:str):
    
    # Retorno: (x,y,x_size,y_size)
    match nome_caixa:
      case "TÍTULO":
        return (int(0.2453*screen.get_width()),int(0.0467*screen.get_height()),int(0.5193*screen.get_width()),int(0.3860*screen.get_height()))
      
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

  match nome_mensagem:
    case "ESPAÇO":

      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",16)
      texto = fonte.render("PRESSIONE ESPAÇO",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3013*screen.get_width()+0.4047*screen.get_width()//2),int(0.7398*screen.get_height()+0.1107*screen.get_height()//2)))

      return [texto,texto_rect]

    case "CAMPANHA":
      
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",36)
      texto = fonte.render("CAMPANHA",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3854*screen.get_width()+0.2295*screen.get_width()//2),int(0.6374*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case "VERSUS":

      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",36)
      texto = fonte.render("VERSUS",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3854*screen.get_width()+0.2295*screen.get_width()//2),int(0.7420*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case "SAIR":

      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",36)
      texto = fonte.render("SAIR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3854*screen.get_width()+0.2295*screen.get_width()//2),int(0.8480*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case _:
      pass
