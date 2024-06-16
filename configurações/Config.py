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

## Cores ##

CORES = {"Preto":(0,0,0),
         "Branco":(255,255,255),
         "Azul":(0,0,255),
         "Vermelho":(255,0,0),
         "Verde":(0,255,0),
         "Azul Escuro":(0,0,139),
         "Azul do ceu":(135,206,235)}

## Janelas ##

# Atualiza os tamanhos de todos os botões
def CAIXA(nome_caixa:str)->tuple[int,int,int,int]:
    
    # Retorno: (x,y,x_size,y_size)
    match nome_caixa:

      case "ESPAÇO":
        return (screen.get_width()//2-screen.get_width()//5,screen.get_height()*0.6,screen.get_width()//2.5,screen.get_height()//15)

      case "TÍTULO":
        return (screen.get_width()//4,screen.get_height()//10,screen.get_width()//2,screen.get_height()//6)
      
      case "CAMPANHA:Branco":
        return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
      
      case "CAMPANHA:Vermelho":
        return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
      
      case "VERSUS:Branco":
        return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
      
      case "VERSUS:Vermelho":
        return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
      
      case "VOLTAR:Branco":
        return (screen.get_width()//2-screen.get_width()//8,int(0.8*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
      
      case "VOLTAR:Vermelho":
        return (screen.get_width()//2-screen.get_width()//8,int(0.8*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
      
      case "1_JOGADOR:Branco":
        return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
      
      case "1_JOGADOR:Vermelho":
        return (screen.get_width()//2-screen.get_width()//8,int(0.6*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
      
      case "2_JOGADORES:Branco":
        return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()),screen.get_width()//4,screen.get_height()//15)
      
      case "2_JOGADORES:Vermelho":
        return (screen.get_width()//2-screen.get_width()//8,int(0.7*screen.get_height()-screen.get_height()//60),screen.get_width()//4,screen.get_height()//10)
      
      case "JOGADOR_CENTRO":
        return (screen.get_width()//2-screen.get_width()//8,screen.get_height()//20,screen.get_width()//4,screen.get_height()//10)

      case "NAVE_SELECAO_CENTRO":
        return (screen.get_width()//2-screen.get_height()//3.5,0.17*screen.get_height())
                
      case "DIVISORIA":
        return (screen.get_width()//2-screen.get_width()//200,0,screen.get_width()/100 ,screen.get_height())
      
      case "JOGADOR_1_ESQUERDA":
        return (screen.get_width()//4-screen.get_width()//8,screen.get_height()//20,screen.get_width()//4,screen.get_height()//10)

      case "JOGADOR_2_DIREITA":
        return (3*screen.get_width()//4-screen.get_width()//8,screen.get_height()/20,screen.get_width()//4,screen.get_height()//10)

      case "NAVE_SELECAO_1":
        return (screen.get_width()//4-screen.get_height()//3.5,int(0.17*screen.get_height()))
      
      case "NAVE_SELECAO_2":
        return (3*screen.get_width()//4-screen.get_height()//3.5,int(0.17*screen.get_height()))
      
      case "BOTAO_A":
        return (screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "BOTAO_D":
        return (3*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "BOTAO_A_CENTRO":
        return (screen.get_width()//4-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "BOTAO_D_CENTRO":
        return (3*screen.get_width()//4-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "BOTAO_<":
        return (5*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "BOTAO_>":
        return (7*screen.get_width()//8-screen.get_width()//20,int(0.65*screen.get_height()),screen.get_width()//10,screen.get_height()//6)

      case "VOLTAR_SELECAO:Branco":
        return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height()),screen.get_width()//8,screen.get_height()//15)

      case "VOLTAR_SELECAO:Vermelho":
        return (screen.get_width()//10-screen.get_width()//16,int(0.9*screen.get_height())-screen.get_height()//60,screen.get_width()//8,screen.get_height()//10)

      case "PRESSIONE_SELECAO:Branco":
        return (screen.get_width()//2-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)

      case "PRESSIONE_SELECAO:Vermelho":
        return (screen.get_width()//2-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)

      case "PRESSIONE_1_SELECAO:Branco":
        return (screen.get_width()//4-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)

      case "PRESSIONE_1_SELECAO:Vermelho":
        return (screen.get_width()//4-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)

      case "PRESSIONE_2_SELECAO:Branco":
        return (3*screen.get_width()//4-screen.get_width()//16,int(0.85*screen.get_height()),screen.get_width()//8,screen.get_height()//20)

      case "PRESSIONE_2_SELECAO:Vermelho":
        return (3*screen.get_width()//4-screen.get_width()//16-screen.get_width()//120,int(0.85*screen.get_height())-screen.get_height()//120,screen.get_width()//7,screen.get_height()//15)

      case _:
        # Retorno: (x,y,x_size,y_size)
        return (0,0,0,0)

# Atualiza os tamanhos de todas as mensagens
def MENSAGEM(nome_mensagem:str)->list:

  box = CAIXA(nome_mensagem)
  size = int(6+3*(box[3]-8)//4)
  fonte = pygame.font.Font("fontes/Star_fonte_completa-Regular.ttf",size)
  
  match nome_mensagem:


    case "ESPAÇO":
      
      
      texto = fonte.render("PRESSIONE ESPAÇO",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "TÍTULO":
      
      
      texto = fonte.render("Space Fighters",True,CORES["Verde"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "CAMPANHA:Branco":

      
      texto = fonte.render("CAMPANHA",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "CAMPANHA:Vermelho":

      
      texto = fonte.render("CAMPANHA",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VERSUS:Branco":

      
      texto = fonte.render("VERSUS",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VERSUS:Vermelho":

      
      texto = fonte.render("VERSUS",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VOLTAR:Branco":

      
      texto = fonte.render("VOLTAR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VOLTAR:Vermelho":

      
      texto = fonte.render("VOLTAR",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "1_JOGADOR:Branco":

      
      texto = fonte.render("1 JOGADOR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))
      print(texto_rect)
      return [texto,texto_rect]

    case "1_JOGADOR:Vermelho":

      
      texto = fonte.render("1 JOGADOR",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "2_JOGADORES:Branco":

      
      texto = fonte.render("2 JOGADORES",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "2_JOGADORES:Vermelho":

      
      texto = fonte.render("2 JOGADORES",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "JOGADOR_CENTRO":

      
      texto = fonte.render("JOGADOR",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "JOGADOR_1_ESQUERDA":

      
      texto = fonte.render("JOGADOR 1",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "JOGADOR_2_DIREITA":

      
      texto = fonte.render("JOGADOR 2",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_A":

      
      texto = fonte.render("A",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_D":

      
      texto = fonte.render("D",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_A_CENTRO":

      
      
      texto = fonte.render("A",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_D_CENTRO":

      
      texto = fonte.render("D",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_<":

      
      texto = fonte.render("!",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "BOTAO_>":

      
      texto = fonte.render("?",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "VOLTAR_SELECAO:Branco":

      
      texto = fonte.render("Voltar",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "VOLTAR_SELECAO:Vermelho":
    
      
      texto = fonte.render("Voltar",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "PRESSIONE_SELECAO:Branco":

      
      texto = fonte.render("Pressione",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "PRESSIONE_SELECAO:Vermelho":
    
      
      texto = fonte.render("Pressione",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "PRESSIONE_1_SELECAO:Branco":

      
      texto = fonte.render("Pressione",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "PRESSIONE_1_SELECAO:Vermelho":
    
      
      texto = fonte.render("Pressione",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    
    case "PRESSIONE_2_SELECAO:Branco":

      
      texto = fonte.render("Pressione",True,CORES["Branco"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]

    case "PRESSIONE_2_SELECAO:Vermelho":
    
      
      texto = fonte.render("Pressione",True,CORES["Vermelho"])
      texto_rect = texto.get_rect(center=(int(box[0]+box[2]//2),int(box[1]+box[3]//2)))

      return [texto,texto_rect]
    case _:
      pass
