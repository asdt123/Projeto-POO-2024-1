import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player

#criação do sprite do jogador e inimigos
#trocar isso pra uma condicional antes da fase 1 e dps da seleceção de modelo

#acho que as caixas de mensagens poderiam ser classes e objetos da janelas. seria mais facil de modular elas e comparar atributos

class Janelas:
    def __init__(self)->None:
        #atributos para acompanhamento dos eventos
        self.ciclo = 0
        self.janela_atual = 0 #definir metodo para setar e pegar essa variavel no game.py. a partir dela verificar quais 
                                #controles funcionam em cada janela, definindo a função de cada em cada caso
        self.scroll = 0
        self.skin1 = 0
        self.skin2 = 0
        self.mouse_pres = [False,False]
        self.tecla_pres = [False,False,pygame.K_0]
        
        self.player = Player(0,0)
        self.player2 = Player(1,0)
        # Guarda todas as skins disponíveis para seleção
        self.imgs = []
        for i in range(14):
            self.imgs.append(pygame.image.load(imagens_naves_selecao).subsurface((i*64,0),(64,64)).convert_alpha())


        # Carregar a imagem de fundo
        self.informacao_bg = pygame.image.load("imagens/cenário/informacao.png").convert_alpha()
        self.background = pygame.image.load("imagens/cenário/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha()
    

    def desenhar_info_jogadores(self):
        # Calcular áreas dinâmicas
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        info_width = 150
        cenario_width = screen_width - 2 * info_width

        # Desenha a imagem de fundo nas áreas de informações dos jogadores
        info_bg_left = pygame.transform.scale(self.informacao_bg, (info_width, screen_height))
        info_bg_right = pygame.transform.scale(self.informacao_bg, (info_width, screen_height))
        screen.blit(info_bg_left, (0, 0))
        screen.blit(info_bg_right, (screen_width - info_width, 0))

        # Informações do jogador 1 (esquerda)
        font = pygame.font.Font(None, 25)
        player1_info = font.render("Jogador 1", True, CORES["Branco"])
        screen.blit(player1_info, (20, 50))

        # Retângulos para representar as informações do jogador 1
        vida_rect = pygame.Rect(40, 100, 50, 50)  # Vida
        pygame.draw.rect(screen, CORES["Branco"], vida_rect, 2)

        score_rect = pygame.Rect(40, 170, 50, 50)  # Score
        pygame.draw.rect(screen, CORES["Branco"], score_rect, 2)

        nave_rect = pygame.Rect(40, 380, 50, 50)  # Nave Atual
        pygame.draw.rect(screen, CORES["Branco"], nave_rect, 2)

        municao_rect = pygame.Rect(40, 450, 50, 50)  # Munição Atual
        pygame.draw.rect(screen, CORES["Branco"], municao_rect, 2)

        # Informações do jogador 2 (direita)
        player2_info = font.render("Jogador 2", True, CORES["Branco"])
        screen.blit(player2_info, (screen_width - info_width + 20, 50))

        # Retângulos para representar as informações do jogador 2
        vida2_rect = pygame.Rect(screen_width - info_width + 40, 100, 50, 50)  # Vida
        pygame.draw.rect(screen, CORES["Branco"], vida2_rect, 2)

        score2_rect = pygame.Rect(screen_width - info_width + 40, 170, 50, 50)  # Score
        pygame.draw.rect(screen, CORES["Branco"], score2_rect, 2)

        nave2_rect = pygame.Rect(screen_width - info_width + 40, 380, 50, 50)  # Nave Atual
        pygame.draw.rect(screen, CORES["Branco"], nave2_rect, 2)

        municao2_rect = pygame.Rect(screen_width - info_width + 40, 450, 50, 50)  # Munição Atual
        pygame.draw.rect(screen, CORES["Branco"], municao2_rect, 2)                

    def atualizar_janela(self,mouse:tuple)->None:

        self.ciclo += 1
        if self.ciclo > 100:
            self.ciclo = 0
            
        match self.janela_atual:

            case 0: # Menu inical

                tempo_oscilação = 30
                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])

                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])
                else:
                  pass

            case 1: # Menu Principal

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])

                
                #isso tem que passar na game mas so receber o valor do mouse quando rolar um evento de click
                #pega as coordenadas e o botão usado. Ai´verifica as condições aqui
                #deve impedir o click duplo

                #para mudar de cor, pode usar o evento pygame.MOUSEMOTION

                #mas pygame.mouse.get_pressed é so para eventos que se repetem
                if(mouse[0] >= CAIXA("CAMPANHA:Branco")[0] and mouse[0] <= (CAIXA("CAMPANHA:Branco")[0]+CAIXA("CAMPANHA:Branco")[2])) and (mouse[1] >= CAIXA("CAMPANHA:Branco")[1] and mouse[1] <= (CAIXA("CAMPANHA:Branco")[1]+CAIXA("CAMPANHA:Branco")[3])):

                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("CAMPANHA:Vermelho"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Vermelho")[0],MENSAGEM("CAMPANHA:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 2
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("CAMPANHA:Branco"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Branco")[0],MENSAGEM("CAMPANHA:Branco")[1])

                if(mouse[0] >= CAIXA("VERSUS:Branco")[0] and mouse[0] <= (CAIXA("VERSUS:Branco")[0]+CAIXA("VERSUS:Branco")[2])) and (mouse[1] >= CAIXA("VERSUS:Branco")[1] and mouse[1] <= (CAIXA("VERSUS:Branco")[1]+CAIXA("VERSUS:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VERSUS:Vermelho"),2)
                    screen.blit(MENSAGEM("VERSUS:Vermelho")[0],MENSAGEM("VERSUS:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        pass
                
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VERSUS:Branco"),2)
                    screen.blit(MENSAGEM("VERSUS:Branco")[0],MENSAGEM("VERSUS:Branco")[1])

                if(mouse[0] >= CAIXA("VOLTAR:Branco")[0] and mouse[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (mouse[1] >= CAIXA("VOLTAR:Branco")[1] and mouse[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 0

                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR:Branco")[0],MENSAGEM("VOLTAR:Branco")[1])
            
            #mesmo ponto acima
            case 2: # Menu número de jogadores

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])
                
                if(mouse[0] >= CAIXA("1_JOGADOR:Branco")[0] and mouse[0] <= (CAIXA("1_JOGADOR:Branco")[0]+CAIXA("1_JOGADOR:Branco")[2])) and (mouse[1] >= CAIXA("1_JOGADOR:Branco")[1] and mouse[1] <= (CAIXA("1_JOGADOR:Branco")[1]+CAIXA("1_JOGADOR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("1_JOGADOR:Vermelho"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Vermelho")[0],MENSAGEM("1_JOGADOR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 3
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("1_JOGADOR:Branco"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Branco")[0],MENSAGEM("1_JOGADOR:Branco")[1])

                if(mouse[0] >= CAIXA("2_JOGADORES:Branco")[0] and mouse[0] <= (CAIXA("2_JOGADORES:Branco")[0]+CAIXA("2_JOGADORES:Branco")[2])) and (mouse[1] >= CAIXA("2_JOGADORES:Branco")[1] and mouse[1] <= (CAIXA("2_JOGADORES:Branco")[1]+CAIXA("2_JOGADORES:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("2_JOGADORES:Vermelho"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Vermelho")[0],MENSAGEM("2_JOGADORES:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 4
                
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("2_JOGADORES:Branco"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Branco")[0],MENSAGEM("2_JOGADORES:Branco")[1])

                if(mouse[0] >= CAIXA("VOLTAR:Branco")[0] and mouse[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (mouse[1] >= CAIXA("VOLTAR:Branco")[1] and mouse[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 1

                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR:Branco")[0],MENSAGEM("VOLTAR:Branco")[1])

            #olhar o uso do pygame.key, novamente so pra quando se repete. criar evento que verifica buttonDown

            #alem disso, as 4 primeiras skins tem o dobro de sprites do resto. olhar esses casos. #adicionar 4 se o valor da variavel
            #self.skin1 for maior que 3

            #vai rolar apenas uma vez. serve pro caso 4 tbm
            case 3: # Menu seleção de jogador unico

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("JOGADOR_CENTRO"),2)
                screen.blit(MENSAGEM("JOGADOR_CENTRO")[0],MENSAGEM("JOGADOR_CENTRO")[1])

                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_A_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_A_CENTRO")[0],MENSAGEM("BOTAO_A_CENTRO")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_D_CENTRO")[0],MENSAGEM("BOTAO_D_CENTRO")[1])

                if self.skin1 < 0:
                    self.skin1 = len(self.imgs)-1
                elif self.skin1 > len(self.imgs)-1:
                    self.skin1 = 0
                self.imgs[self.skin1].fill((100,0,0,70),special_flags=pygame.BLEND_RGBA_ADD)
                # Guarda todas as skins disponíveis para seleção
                screen.blit(pygame.transform.scale(self.imgs[self.skin1],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(CAIXA("NAVE_SELECAO_CENTRO")))
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_d:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D_CENTRO"),2)
                    self.skin1 += 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_a:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A_CENTRO"),2)
                    self.skin1 -= 1

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_SPACE:
                    self.janela_atual = 5
            
            case 4: # Menu selseção de dois jogadores

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("DIVISORIA"))
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("JOGADOR_1_ESQUERDA"),2)
                screen.blit(MENSAGEM("JOGADOR_1_ESQUERDA")[0],MENSAGEM("JOGADOR_1_ESQUERDA")[1])

                pygame.draw.rect(screen,CORES["Branco"],CAIXA("JOGADOR_2_DIREITA"),2)
                screen.blit(MENSAGEM("JOGADOR_2_DIREITA")[0],MENSAGEM("JOGADOR_2_DIREITA")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_A"),2)
                screen.blit(MENSAGEM("BOTAO_A")[0],MENSAGEM("BOTAO_A")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D"),2)
                screen.blit(MENSAGEM("BOTAO_D")[0],MENSAGEM("BOTAO_D")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_<"),2)
                screen.blit(MENSAGEM("BOTAO_<")[0],MENSAGEM("BOTAO_<")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_>"),2)
                screen.blit(MENSAGEM("BOTAO_>")[0],MENSAGEM("BOTAO_>")[1])

                if self.skin1 < 0:
                    self.skin1 = len(self.imgs)-1
                elif self.skin1 > len(self.imgs)-1:
                    self.skin1 = 0
                
                if self.skin2 < 0:
                    self.skin2 = len(self.imgs)-1
                elif self.skin2 > len(self.imgs)-1:
                    self.skin2 = 0

                # Guarda todas as skins disponíveis para seleção
                screen.blit(pygame.transform.scale(self.imgs[self.skin1],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(CAIXA("NAVE_SELECAO_1")[0],CAIXA("NAVE_SELECAO_1")[1]))
                screen.blit(pygame.transform.scale(self.imgs[self.skin2],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(CAIXA("NAVE_SELECAO_2")[0],CAIXA("NAVE_SELECAO_2")[1]))

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_LEFT:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_<"),2)
                    self.skin2 -= 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_RIGHT:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_>"),2)
                    self.skin2 += 1

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_d:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D"),2)
                    self.skin1 += 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_a:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A"),2)
                    self.skin1 -= 1

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_SPACE:
                    self.janela_atual = 5
               
            case 5:
                
                # Criação da nave com a skin selecionada. Pode ser bom tirar o selecionador de skins do construtor
                # da classe Player e colocá-lo em um método para que seja possível mudar após o construtor ser 
                # instanciado pela primeira vez
                self.player = Player(0,self.skin1)
                players.add(self.player)
                self.janela_atual = 6

            case 6: # Fases do jogo
                if self.scroll < background_altura-background_largura-1:
                    self.scroll += 1
                else:
                    self.scroll = 0
                info_width = 150
                cenario_width = screen.get_width() - 2 * info_width
                
                self.background = pygame.image.load("imagens/cenário/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha()
                screen.blit(pygame.transform.scale(self.background, (cenario_width, screen.get_height())), (info_width, 0))

                if len(aliens) < random.randint(2, 3) and pygame.time.get_ticks() % 50 > 45:
                    aliens.add(Alien((random.randint(info_width + 50, info_width + cenario_width - 50), -30), random.randint(0, 1)))
                '''
                # Atualizar a posição dos jogadores para que fiquem dentro do cenário
                for player in players:
                    if player.rect.left < info_width:
                        player.rect.left = info_width
                    if player.rect.right > info_width + cenario_width:
                        player.rect.right = info_width + cenario_width
                    if player.rect.top < 0:
                        player.rect.top = 0
                    if player.rect.bottom > screen_height:
                        player.rect.bottom = screen_height '''
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.
                
                #gera os aliens
                if len(aliens) < random.randint(2,3) and pygame.time.get_ticks()%50 > 45:
                    aliens.add(Alien((random.randint(150,screen.get_width()-150),-30), random.randint(0,3)))

                players.draw(screen)
                players.update(aliens)
                aliens.draw(screen)
                aliens.update(players)
                drops.draw(screen)
                drops.update(players)

                self.desenhar_info_jogadores()

            case _:
                pass

    def pegar_mouse_click(self,MOUSE_APERTADO:list[bool,bool]):
        self.mouse_pres = MOUSE_APERTADO

    def pegar_tecla_apertada(self,TECLAS_APERTADAS):
        self.tecla_pres = TECLAS_APERTADAS

    def selecionar_skin(self):
        
        return self.skin1    
