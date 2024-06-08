import pygame

pygame.init()
relogio = pygame.time.Clock()

# Definições da janela

TÍTULO = "Space Fighters"

FPS = 30
pygame.display.set_caption(TÍTULO)
screen = pygame.display.set_mode((900,600))


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
VIDA_ALIEN = [100, 50]
DANO_PLAYER = [20,20]
imagens_aliens = "imagens/inimigos/inimigos.png"
morte_aliens = ""
municao_aliens = "imagens/armamento/munições.png"

# backgorund 
background = "imagens/cenário/Cenarios.png"
background_altura, background_largura = 2500, 128

# função para atualização do tamanho e posicionamento dos sprites
def tamanho_nave():
  return (screen.get_height()//6,screen.get_height()//6)

def tamanho_alien():
  return (screen.get_height()//4.6875,screen.get_height()//4.6875)

def tamanho_municao():
  return (screen.get_height()//25,screen.get_height()//25)

def barra_vida(tipo_player, vida):
  #vida player 1
  if tipo_player==0:
    return (screen.get_width()//36,screen.get_height()//24,(screen.get_width()//900)*vida, screen.get_height()//30)
  #vida player 2
  else:
    return (screen.get_width()//1.2,screen.get_height()//24,(screen.get_width()//900)*vida, screen.get_height()//30)

## Cores ##

CORES = {"Preto":(0,0,0),
         "Branco":(255,255,255),
         "Azul":(0,0,255),
         "Vermelho":(255,0,0),
         "Verde":(0,255,0),
         "Azul Escuro":(0,0,139),
         "Azul do ceu":(135,206,235)}

## Janelas ##

JANELAS = ["Menu Inicial 1",
           "Menu Inicial 2",
           "Fase 1"]

MOUSE_POS = (0,0)

# Atualiza os tamanhos de todos os botões
def CAIXA(nome_caixa:str):
    
    # Retorno: (x,y,x_size,y_size)
    match nome_caixa:
      case "TÍTULO":
        return (int(0.2453*screen.get_width()),int(0.0467*screen.get_height()),int(0.5193*screen.get_width()),int(0.3860*screen.get_height()))
      
      case "CAMPANHA:Branco":
        return (int(0.3898*screen.get_width()),int(0.6374*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "CAMPANHA:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.6192*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case "VERSUS:Branco":
        return (int(0.3898*screen.get_width()),int(0.7420*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "VERSUS:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.7241*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case "SAIR:Branco":
        return (int(0.3898*screen.get_width()),int(0.8503*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "SAIR:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.8328*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case _:
        return (0,0,0,0)

# Atualiza os tamanhos de todas as mensagens
def MENSAGEM(nome_mensagem:str):

  match nome_mensagem:
    case "ESPAÇO":
      
      size = int((0.3013*screen.get_width()+0.4047*screen.get_width()+0.7398*screen.get_height()+0.1107*screen.get_height())/30)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("PRESSIONE ESPAÇO",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3013*screen.get_width()+0.4047*screen.get_width()//2),int(0.7398*screen.get_height()+0.1107*screen.get_height()//2)))

      return [texto,texto_rect]

    case "CAMPANHA:Branco":

      size = int((0.3898*screen.get_width()+0.2295*screen.get_width()+0.6374*screen.get_height()+0.0715*screen.get_height())/30)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("CAMPANHA",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3898*screen.get_width()+0.2295*screen.get_width()//2),int(0.6374*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case "CAMPANHA:Vermelho":

      size = int((0.3770*screen.get_width()+0.2547*screen.get_width()+0.6192*screen.get_height()+0.1080*screen.get_height())/20)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("CAMPANHA",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3770*screen.get_width()+0.2547*screen.get_width()//2),int(0.6192*screen.get_height()+0.1080*screen.get_height()//2)))

      return [texto,texto_rect]

    case "VERSUS:Branco":

      size = int((0.3898*screen.get_width()+0.2295*screen.get_width()+0.7420*screen.get_height()+0.0715*screen.get_height())/30)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("VERSUS",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3898*screen.get_width()+0.2295*screen.get_width()//2),int(0.7420*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case "VERSUS:Vermelho":

      size = int((0.3770*screen.get_width()+0.2547*screen.get_width()+0.7241*screen.get_height()+0.1080*screen.get_height())/20)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("VERSUS",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3770*screen.get_width()+0.2547*screen.get_width()//2),int(0.7241*screen.get_height()+0.1080*screen.get_height()//2)))

      return [texto,texto_rect]

    case "SAIR:Branco":

      size = int((0.3898*screen.get_width()+0.2295*screen.get_width()+0.8503*screen.get_height()+0.0715*screen.get_height())/30)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("SAIR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(0.3898*screen.get_width()+0.2295*screen.get_width()//2),int(0.8503*screen.get_height()+0.0715*screen.get_height()//2)))

      return [texto,texto_rect]

    case "SAIR:Vermelho":

      size = int((0.3770*screen.get_width()+0.2547*screen.get_width()+0.8328*screen.get_height()+0.1080*screen.get_height())/20)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("SAIR",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3770*screen.get_width()+0.2547*screen.get_width()//2),int(0.8328*screen.get_height()+0.1080*screen.get_height()//2)))

      return [texto,texto_rect]

    case _:
      pass
