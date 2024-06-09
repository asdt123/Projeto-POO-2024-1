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
VIDA_ALIEN = [100, 75, 100, 50]
DANO_ALIEN = [2, 2, 2, 2]
imagens_aliens = "imagens/inimigos/inimigos.png"
morte_aliens = ""
municao_aliens = "imagens/armamento/munições.png"

#drops
drops = pygame.sprite.Group()

# backgorund 
background = "imagens/cenário/Cenarios.png"
background_altura, background_largura = 2500, 128

# função para atualização do tamanho e posicionamento dos sprites
def tamanho_nave():
  return (screen.get_height()//7,screen.get_height()//7)

def tamanho_alien():
  return (screen.get_height()//5,screen.get_height()//5)

def tamanho_municao():
  return (screen.get_height()//30,screen.get_height()//30)

def barra_vida(tipo_player, vida):
  #vida player 1
  if tipo_player==0:
    return (screen.get_width()//36,screen.get_height()//24,int((screen.get_width()/900)*vida*1.5), screen.get_height()//30)
  #vida player 2
  else:
    return (screen.get_width()//1.25,screen.get_height()//24,int((screen.get_width()/900)*vida*1.5), screen.get_height()//30)

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
           "Menu Seleção Skins",
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
      
      case "DIVISORIA":
        return (int(0.4989*screen.get_width()),int(0.0*screen.get_height()),int(0.01*screen.get_width()),int(1.0*screen.get_height()))
      
      case "JOGAR_PLAYER_1":
        return (int(0.1210*screen.get_width()),int(0.1277*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))

      case "JOGAR_PLAYER_2":
        return (int(0.6275*screen.get_width()),int(0.1277*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))

      case "BOTAO_A":
        return (int(0.0747*screen.get_width()),int(0.7475*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_D":
        return (int(0.3550*screen.get_width()),int(0.7475*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_<":
        return (int(0.5770*screen.get_width()),int(0.7475*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_>":
        return (int(0.8292*screen.get_width()),int(0.7475*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case _:
        # Retorno: (x,y,x_size,y_size)
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

    case "JOGADOR_1":

      size = int((0.1210*screen.get_width()+0.2547*screen.get_width()+0.1277*screen.get_height()+0.1080*screen.get_height())/10)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("Jogador A",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.1210*screen.get_width()+0.2547*screen.get_width()//2),int(0.1277*screen.get_height()+0.1080*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case "JOGADOR_2":

      size = int((0.6275*screen.get_width()+0.2547*screen.get_width()+0.1277*screen.get_height()+0.1080*screen.get_height())/20)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("Jogador B",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.6275*screen.get_width()+0.2547*screen.get_width()//2),int(0.1277*screen.get_height()+0.1080*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case "A":

      size = int((0.0747*screen.get_width()+0.0923*screen.get_width()+0.7475*screen.get_height()+0.1449*screen.get_height())/7)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("A",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.0747*screen.get_width()+0.0923*screen.get_width()//2),int(0.7475*screen.get_height()+0.1449*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case "D":

      size = int((0.3550*screen.get_width()+0.0923*screen.get_width()+0.7475*screen.get_height()+0.1449*screen.get_height())/7.5)
      fonte = pygame.font.Font("fontes/Star_figthers-Regular.ttf",size)
      texto = fonte.render("D",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.3550*screen.get_width()+0.0923*screen.get_width()//2),int(0.7475*screen.get_height()+0.1449*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case "<":

      size = int((0.5770*screen.get_width()+0.0923*screen.get_width()+0.7475*screen.get_height()+0.1449*screen.get_height())/7)
      fonte = pygame.font.Font(None,size)
      texto = fonte.render("<",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.5770*screen.get_width()+0.0923*screen.get_width()//2),int(0.7475*screen.get_height()+0.1449*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case ">":

      size = int((0.8292*screen.get_width()+0.0923*screen.get_width()+0.7475*screen.get_height()+0.1449*screen.get_height())/7)
      fonte = pygame.font.Font(None,size)
      texto = fonte.render(">",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(0.8292*screen.get_width()+0.0923*screen.get_width()//2),int(0.7475*screen.get_height()+0.1449*screen.get_height()//2)))

      return [texto,texto_rect]
    
    case _:
      pass
