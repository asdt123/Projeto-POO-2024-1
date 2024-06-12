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




## Cores ##

CORES = {"Preto":(0,0,0),
         "Branco":(255,255,255),
         "Azul":(0,0,255),
         "Vermelho":(255,0,0),
         "Verde":(0,255,0),
         "Azul Escuro":(0,0,139),
         "Azul do ceu":(135,206,235)}

## Janelas ##

#definição de parâmetros que definem quando o mouse ou uma tecla estão 
#apertados (para a classe Janela)

MOUSE_APERTADO = [False,False]
TECLAS_APERTADAS = [False,False,pygame.K_0]

# Atualiza os tamanhos de todos os botões
def CAIXA(nome_caixa:str)->tuple[int,int,int,int]:
    
    # Retorno: (x,y,x_size,y_size)
    match nome_caixa:

      case "ESPAÇO":
        return (int(0.3013*screen.get_width()),int(0.7398*screen.get_height()),int(0.4047*screen.get_width()),int(0.1107*screen.get_height()))

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
      
      case "VOLTAR:Branco":
        return (int(0.3898*screen.get_width()),int(0.8503*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "VOLTAR:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.8328*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case "1_JOGADOR:Branco":
        return (int(0.3898*screen.get_width()),int(0.6374*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "1_JOGADOR:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.6192*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case "2_JOGADORES:Branco":
        return (int(0.3898*screen.get_width()),int(0.7420*screen.get_height()),int(0.2295*screen.get_width()),int(0.0715*screen.get_height()))
      
      case "2_JOGADORES:Vermelho":
        return (int(0.3770*screen.get_width()),int(0.7241*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))
      
      case "JOGADOR_CENTRO":
        return (int(0.3724*screen.get_width()),int(0.0320*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))

      case "NAVE_SELECAO_CENTRO":
        return (int(0.3381*screen.get_width()),int(0.1851*screen.get_height()),int(0.3556*screen.get_width()),int(0.5333*screen.get_height()))
      
      case "DIVISORIA":
        return (int(0.4989*screen.get_width()),int(0.0*screen.get_height()),int(0.01*screen.get_width()),int(1.0*screen.get_height()))
      
      case "JOGADOR_1_ESQUERDA":
        return (int(0.1254*screen.get_width()),int(0.0320*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))

      case "JOGADOR_2_DIREITA":
        return (int(0.6208*screen.get_width()),int(0.0320*screen.get_height()),int(0.2547*screen.get_width()),int(0.1080*screen.get_height()))

      case "NAVE_SELECAO_1":
        return (int(0.1441*screen.get_width()),int(0.1851*screen.get_height()),int(0.2133*screen.get_width()),int(0.3200*screen.get_height()))
      
      case "NAVE_SELECAO_2":
        return (int(0.6399*screen.get_width()),int(0.1851*screen.get_height()),int(0.2133*screen.get_width()),int(0.3200*screen.get_height()))
      
      case "BOTAO_A":
        return (int(0.0570*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_D":
        return (int(0.3528*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_A_CENTRO":
        return (int(0.2094*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_D_CENTRO":
        return (int(0.6917*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_<":
        return (int(0.5615*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case "BOTAO_>":
        return (int(0.8448*screen.get_width()),int(0.6609*screen.get_height()),int(0.0923*screen.get_width()),int(0.1449*screen.get_height()))

      case _:
        # Retorno: (x,y,x_size,y_size)
        return (0,0,0,0)

# Atualiza os tamanhos de todas as mensagens
def MENSAGEM(nome_mensagem:str)->list:

  box = CAIXA(nome_mensagem)
  
  match nome_mensagem:

    case "ESPAÇO":
      
      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("PRESSIONE ESPAÇO",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "TÍTULO":
      
      size = int((box[0]+box[2]+box[1]+box[3])/12)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("Space Fighters",True,CORES["Verde"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "CAMPANHA:Branco":

      
      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("CAMPANHA",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "CAMPANHA:Vermelho":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("CAMPANHA",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VERSUS:Branco":

      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("VERSUS",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VERSUS:Vermelho":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("VERSUS",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VOLTAR:Branco":

      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("VOLTAR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VOLTAR:Vermelho":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("VOLTAR",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "1_JOGADOR:Branco":

      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("1 JOGADOR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "1_JOGADOR:Vermelho":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("1 JOGADOR",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "2_JOGADORES:Branco":

      size = int((box[0]+box[2]+box[1]+box[3])/30)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("2 JOGADORES",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "2_JOGADORES:Vermelho":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("2 JOGADORES",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "JOGADOR_CENTRO":

      size = int((box[0]+box[2]+box[1]+box[3])/10)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("JOGADOR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "JOGADOR_1_ESQUERDA":

      size = int((box[0]+box[2]+box[1]+box[3])/10)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("JOGADOR 1",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "JOGADOR_2_DIREITA":

      size = int((box[0]+box[2]+box[1]+box[3])/20)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("JOGADOR 2",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_A":

      size = int((box[0]+box[2]+box[1]+box[3])/7)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("A",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_D":

      size = int((box[0]+box[2]+box[1]+box[3])/7.5)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("D",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_A_CENTRO":

      size = int((box[0]+box[2]+box[1]+box[3])/7)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("A",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_D_CENTRO":

      size = int((box[0]+box[2]+box[1]+box[3])/7.5)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("D",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_<":

      size = int((box[0]+box[2]+box[1]+box[3])/7)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("!",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_>":

      size = int((box[0]+box[2]+box[1]+box[3])/7)
      fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
      texto = fonte.render("?",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case _:
      pass
