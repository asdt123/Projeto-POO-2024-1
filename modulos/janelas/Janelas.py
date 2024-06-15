import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player
from .Animação import Animação

#criação do sprite do jogador e inimigos
#trocar isso pra uma condicional antes da fase 1 e dps da seleceção de modelo

#acho que as caixas de mensagens poderiam ser classes e objetos da janelas. seria mais facil de modular elas e comparar atributos

class Janelas:
    def __init__(self)->None:
        #atributos para acompanhamento dos eventos
        self.animações = pygame.sprite.Group()
        self.ciclo = 0
        self.janela_atual = 0 #definir metodo para setar e pegar essa variavel no game.py. a partir dela verificar quais 
                                #controles funcionam em cada janela, definindo a função de cada em cada caso
        self.scroll = 0
        self.skin1 = 20
        self.skin2 = 20
        self.mouse_pres = [False,False]
        self.tecla_pres = [False,False,pygame.K_0]
        self.jogadores_prontos = [False,False]
        self.player = Player(0,0)
        self.player2 = Player(1,0)

        # Guarda todas as skins disponíveis para seleção
        self.imgs = []
        for i in range(14):
            self.imgs.append(pygame.image.load(imagens_naves_selecao).subsurface((i*64,0),(64,64)).convert_alpha())


        # Carregar a imagem de fundo
        self.informacao_bg = []
        for i in range(2):
            self.informacao_bg.append(pygame.image.load("imagens/cenário/informacao.png").convert_alpha())

        self.background = []
        for i in range(4):
            self.background.append(pygame.image.load("imagens/cenário/menu_inicial.png").subsurface((0,600*i), (900, 600)).convert_alpha())
        self.index_b = 0
        
    def desenhar_info_jogadores(self):
        #deixa a largura da informação baseada na largura do jogo
        #assim ela não varia se mudar o tamanho da tela

        # Calcular áreas dinâmicas
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        info_width = screen.get_width()//6

        # Desenha a imagem de fundo nas áreas de informações dos jogadores
        self.informacao_bg[0] = pygame.transform.scale(self.informacao_bg[0], (info_width, screen_height))
        self.informacao_bg[1] = pygame.transform.scale(self.informacao_bg[1], (info_width, screen_height))
        screen.blit(self.informacao_bg[0], (0, 0))
        screen.blit(self.informacao_bg[1], ((screen_width - info_width), 0))

           

    def atualizar_janela(self)->None:

        self.ciclo += 1
        if self.ciclo > 100:
            self.ciclo = 0
        
        self.index_b += 0.05
        if self.index_b > len(self.background):
            self.index_b = 0    
        match self.janela_atual:

            case 0: # Menu inical

                tempo_oscilação = 30
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])

                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])
                else:
                  pass

            case 1: # Menu Principal
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))

                ##screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])
                
                #para mudar de cor, pode usar o evento pygame.MOUSEMOTION
                if(pygame.mouse.get_pos()[0] >= CAIXA("CAMPANHA:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("CAMPANHA:Branco")[0]+CAIXA("CAMPANHA:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("CAMPANHA:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("CAMPANHA:Branco")[1]+CAIXA("CAMPANHA:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("CAMPANHA:Vermelho"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Vermelho")[0],MENSAGEM("CAMPANHA:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 2

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("CAMPANHA:Branco"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Branco")[0],MENSAGEM("CAMPANHA:Branco")[1])

                if(pygame.mouse.get_pos()[0] >= CAIXA("VERSUS:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("VERSUS:Branco")[0]+CAIXA("VERSUS:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("VERSUS:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("VERSUS:Branco")[1]+CAIXA("VERSUS:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VERSUS:Vermelho"),2)
                    screen.blit(MENSAGEM("VERSUS:Vermelho")[0],MENSAGEM("VERSUS:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        pass
                
                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VERSUS:Branco"),2)
                    screen.blit(MENSAGEM("VERSUS:Branco")[0],MENSAGEM("VERSUS:Branco")[1])

                if(pygame.mouse.get_pos()[0] >= CAIXA("VOLTAR:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("VOLTAR:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 0

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR:Branco")[0],MENSAGEM("VOLTAR:Branco")[1])
            

            case 2: # Menu número de jogadores
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))

                ##screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("TÍTULO")[0],MENSAGEM("TÍTULO")[1])
                
                if(pygame.mouse.get_pos()[0] >= CAIXA("1_JOGADOR:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("1_JOGADOR:Branco")[0]+CAIXA("1_JOGADOR:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("1_JOGADOR:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("1_JOGADOR:Branco")[1]+CAIXA("1_JOGADOR:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("1_JOGADOR:Vermelho"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Vermelho")[0],MENSAGEM("1_JOGADOR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 3
                
                else:

                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("1_JOGADOR:Branco"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Branco")[0],MENSAGEM("1_JOGADOR:Branco")[1])

                if(pygame.mouse.get_pos()[0] >= CAIXA("2_JOGADORES:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("2_JOGADORES:Branco")[0]+CAIXA("2_JOGADORES:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("2_JOGADORES:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("2_JOGADORES:Branco")[1]+CAIXA("2_JOGADORES:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("2_JOGADORES:Vermelho"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Vermelho")[0],MENSAGEM("2_JOGADORES:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 4
                
                else:

                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("2_JOGADORES:Branco"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Branco")[0],MENSAGEM("2_JOGADORES:Branco")[1])

                if(pygame.mouse.get_pos()[0] >= CAIXA("VOLTAR:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("VOLTAR:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 1

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR:Branco")[0],MENSAGEM("VOLTAR:Branco")[1])

            #alem disso, as 4 primeiras skins tem o dobro de sprites do resto. olhar esses casos. #adicionar 4 se o valor da variavel
            #self.skin1 for maior que 3

            #vai rolar apenas uma vez. serve pro caso 4 tbm

            case 3: # Menu seleção de jogador unico
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                
                ##screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("JOGADOR_CENTRO"),2)
                screen.blit(MENSAGEM("JOGADOR_CENTRO")[0],MENSAGEM("JOGADOR_CENTRO")[1])

                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_A_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_A_CENTRO")[0],MENSAGEM("BOTAO_A_CENTRO")[1])
                
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_D_CENTRO")[0],MENSAGEM("BOTAO_D_CENTRO")[1])

                if(pygame.mouse.get_pos()[0] >= CAIXA("VOLTAR_SELECAO:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("VOLTAR_SELECAO:Branco")[0]+CAIXA("VOLTAR_SELECAO:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("VOLTAR_SELECAO:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("VOLTAR_SELECAO:Branco")[1]+CAIXA("VOLTAR_SELECAO:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR_SELECAO:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR_SELECAO:Vermelho")[0],MENSAGEM("VOLTAR_SELECAO:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 2

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR_SELECAO:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR_SELECAO:Branco")[0],MENSAGEM("VOLTAR_SELECAO:Branco")[1])


                if(pygame.mouse.get_pos()[0] >= CAIXA("PRESSIONE_SELECAO:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("PRESSIONE_SELECAO:Branco")[0]+CAIXA("PRESSIONE_SELECAO:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("PRESSIONE_SELECAO:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("PRESSIONE_SELECAO:Branco")[1]+CAIXA("PRESSIONE_SELECAO:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_SELECAO:Vermelho"),2)
                    screen.blit(MENSAGEM("PRESSIONE_SELECAO:Vermelho")[0],MENSAGEM("PRESSIONE_SELECAO:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 5

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_SELECAO:Branco"),2)
                    screen.blit(MENSAGEM("PRESSIONE_SELECAO:Branco")[0],MENSAGEM("PRESSIONE_SELECAO:Branco")[1])


                if self.skin1 < 0:
                    self.skin1 = len(self.imgs)-1
                elif self.skin1 > len(self.imgs)-1:
                    self.skin1 = 0

                # Guarda todas as skins disponíveis para seleção
                screen.blit(pygame.transform.scale(self.imgs[self.skin1],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(CAIXA("NAVE_SELECAO_CENTRO")))
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_d:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D_CENTRO"),2)
                    self.skin1 += 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_a:
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A_CENTRO"),2)
                    self.skin1 -= 1
            
            case 4: # Menu selseção de dois jogadores
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))

                #screen.fill(CORES["Azul do ceu"])
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

                if(pygame.mouse.get_pos()[0] >= CAIXA("VOLTAR_SELECAO:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("VOLTAR_SELECAO:Branco")[0]+CAIXA("VOLTAR_SELECAO:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("VOLTAR_SELECAO:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("VOLTAR_SELECAO:Branco")[1]+CAIXA("VOLTAR_SELECAO:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR_SELECAO:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR_SELECAO:Vermelho")[0],MENSAGEM("VOLTAR_SELECAO:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.janela_atual = 2

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR_SELECAO:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR_SELECAO:Branco")[0],MENSAGEM("VOLTAR_SELECAO:Branco")[1])


                if(pygame.mouse.get_pos()[0] >= CAIXA("PRESSIONE_1_SELECAO:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("PRESSIONE_1_SELECAO:Branco")[0]+CAIXA("PRESSIONE_1_SELECAO:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("PRESSIONE_1_SELECAO:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("PRESSIONE_1_SELECAO:Branco")[1]+CAIXA("PRESSIONE_1_SELECAO:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_1_SELECAO:Vermelho"),2)
                    screen.blit(MENSAGEM("PRESSIONE_1_SELECAO:Vermelho")[0],MENSAGEM("PRESSIONE_1_SELECAO:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.jogadores_prontos[0] = True

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_1_SELECAO:Branco"),2)
                    screen.blit(MENSAGEM("PRESSIONE_1_SELECAO:Branco")[0],MENSAGEM("PRESSIONE_1_SELECAO:Branco")[1])

                
                if(pygame.mouse.get_pos()[0] >= CAIXA("PRESSIONE_2_SELECAO:Branco")[0] and pygame.mouse.get_pos()[0] <= (CAIXA("PRESSIONE_2_SELECAO:Branco")[0]+CAIXA("PRESSIONE_2_SELECAO:Branco")[2])) and (pygame.mouse.get_pos()[1] >= CAIXA("PRESSIONE_2_SELECAO:Branco")[1] and pygame.mouse.get_pos()[1] <= (CAIXA("PRESSIONE_2_SELECAO:Branco")[1]+CAIXA("PRESSIONE_2_SELECAO:Branco")[3])):
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_2_SELECAO:Vermelho"),2)
                    screen.blit(MENSAGEM("PRESSIONE_2_SELECAO:Vermelho")[0],MENSAGEM("PRESSIONE_2_SELECAO:Vermelho")[1])
                    if self.mouse_pres[0] == True and self.mouse_pres[1] == True:
                        self.jogadores_prontos[1] = True

                else:
                    
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("PRESSIONE_2_SELECAO:Branco"),2)
                    screen.blit(MENSAGEM("PRESSIONE_2_SELECAO:Branco")[0],MENSAGEM("PRESSIONE_2_SELECAO:Branco")[1])


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
                
                if self.jogadores_prontos == [True,True]:
                    self.janela_atual = 5
                    self.jogadores_prontos = [False,False]

            case 5:
                
                # Criação da nave com a skin selecionada. Pode ser bom tirar o selecionador de skins do construtor
                # da classe Player e colocá-lo em um método para que seja possível mudar após o construtor ser 
                # instanciado pela primeira vez
                screen.fill(CORES["Azul do ceu"])
                if self.skin1<4:
                    self.player = Player(0,self.skin1*2)
                else:
                    self.player = Player(0,self.skin1+4)
                players.add(self.player)

                if self.skin2!=20:
                    if self.skin2<4:
                        self.player2 = Player(1,self.skin2*2)
                    else:
                        self.player2 = Player(1,self.skin2+4)
                    players.add(self.player2)

                self.janela_atual = 6
                
                self.background.clear()
                self.background.append(pygame.image.load("imagens/cenário/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha())

            case 6: # Fases do jogo

                if self.scroll < background_altura-background_largura-1:
                    self.scroll += 1
                else:
                    self.scroll = 0
                
                # Calcular áreas dinâmicas
                
                info_width = screen.get_width()//6
                cenario_width = screen.get_width() - 2 * info_width
                
                self.background[0]=pygame.image.load("imagens/cenário/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha()


                if len(self.animações) < random.randint(2, 3) and self.ciclo%3==0:
                    self.animações.add(Animação(random.randint(info_width, info_width+cenario_width), random.randint(0, 1)))

                if len(aliens) < random.randint(2, 3) and self.ciclo%5==0:
                    aliens.add(Alien(random.randint(info_width, info_width+cenario_width), random.randint(0, 1)))
                
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.

                screen.blit(pygame.transform.scale(self.background[0], (cenario_width, screen.get_height())), (info_width, 0))
                self.desenhar_info_jogadores()

                self.animações.draw(screen)
                self.animações.update()
                players.draw(screen)
                players.update(aliens)
                aliens.draw(screen)
                aliens.update(players)
                drops.draw(screen)
                drops.update(players)


            case _:
                pass
        
        # "Limpa" o mouse e o teclado para evitar clicks indevidos
        if self.tecla_pres[0:2] == [True,True]:
            self.tecla_pres = [False,False,pygame.K_0]

        if self.mouse_pres == [True,True]:
            self.mouse_pres = [False,False]
        

    def pegar_mouse_click(self,MOUSE_APERTADO:list[bool,bool]):
        self.mouse_pres = MOUSE_APERTADO

    def pegar_tecla_apertada(self,TECLAS_APERTADAS):
        self.tecla_pres = TECLAS_APERTADAS

    def selecionar_skin(self):
        return self.skin1    
    
"""    # getter
    @property
    def janela_atual(self)->int:
        return self.janela_atual
    
    @janela_atual.setter
    def janela_atual(self,id:int)->None:
        self.janela_atual = id  
"""