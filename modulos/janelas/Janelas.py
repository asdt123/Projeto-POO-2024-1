import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player
from .Animação import Animação
from .Botões import Botões

#criação do sprite do jogador e inimigos
#trocar isso pra uma condicional antes da fase 1 e dps da seleceção de modelo

#acho que as caixas de mensagens poderiam ser classes e objetos da janelas. seria mais facil de modular elas e comparar atributos

class Janelas:
    def __init__(self)->None:
        #atributos para acompanhamento dos eventos
        self.animações = pygame.sprite.Group()
        self.ciclo = 0
        self.janela_atual = 0

        #atirbuto para atualização do cenario
        self.scroll = 0

        #atirbuto para escolha de skins
        self.skin1 = 20
        self.skin2 = 20

        #verificação da tecla
        self.tecla_pres = [False,False,pygame.K_0]

        #jogadores
        self.jogadores_prontos = [False,False]
        self.player = Player(0,0)
        self.player2 = Player(1,0)

        #botoes utilizados
        self.botoes = []
        for i in range(20):
            self.botoes.append(Botões(i))

        # Guarda todas as skins disponíveis para seleção
        self.imgs = []
        for i in range(14):
            self.imgs.append(pygame.image.load(imagens_naves_selecao).subsurface((i*64,0),(64,64)).convert_alpha())


        # Carregar a imagem lateral
        self.informacao_bg = []
        for i in range(2):
            self.informacao_bg.append(pygame.image.load("imagens/cenário/informacao.png").convert_alpha())

        #carrega o backgorund
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
        #definição de botões
        self.botoes[0].alterar_texto("Pressione Espaço", 'ESPAÇO')
        self.botoes[1].alterar_texto("Star Fighters", 'TITULO')
        self.botoes[2].alterar_texto("Campanha")
        self.botoes[3].alterar_texto("Versus")
        self.botoes[4].alterar_texto("Voltar")
        self.botoes[5].alterar_texto("JOGADOR", 'NORMAL')
        self.botoes[6].alterar_texto("A")
        self.botoes[7].alterar_texto("D")
        self.botoes[8].alterar_texto("Pressione")
        self.botoes[9].alterar_texto("Voltar")
        self.botoes[10].alterar_texto("JOGADOR 1", 'NORMAL')
        self.botoes[11].alterar_texto("A")
        self.botoes[12].alterar_texto("D")
        self.botoes[13].alterar_texto("Pressione", 'ESTATICO')
        self.botoes[14].alterar_texto("JOGADOR 2", 'NORMAL')
        self.botoes[15].alterar_texto("!")
        self.botoes[16].alterar_texto("?")
        self.botoes[17].alterar_texto("Pressione", 'ESTATICO')
        self.botoes[18].alterar_texto("Voltar")
        self.botoes[19].alterar_texto("", 'BOX')     

        #contagem de ciclos, a cada 30 frames conta um
        self.ciclo += 1
        if self.ciclo > 100:
            self.ciclo = 0
        
        #atualização do fundo
        self.index_b += 0.05
        if self.index_b > len(self.background):
            self.index_b = 0    
        
        #impressão da janela
        match self.janela_atual:
            case 0: # Menu inical
                tempo_oscilação = 30
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                self.botoes[1].update()

                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  self.botoes[0].update()
                else:
                  pass

            case 1: # Menu Principal
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                self.botoes[1].update()
                self.botoes[2].update()
                self.botoes[3].update()
                self.botoes[4].update()               

            case 2: # Menu número de jogadores
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                self.botoes[2].alterar_texto("1 jogador")
                self.botoes[3].alterar_texto("2 jogadores")
                self.botoes[1].update()
                self.botoes[2].update()
                self.botoes[3].update()
                self.botoes[4].update()       

            case 3: # Menu seleção de jogador unico
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                #jogador
                self.botoes[5].update()
                self.botoes[6].update()
                self.botoes[7].update()
                self.botoes[8].update()
                self.botoes[9].update()
                
                if self.skin1 < 0:
                    self.skin1 = len(self.imgs)-1
                elif self.skin1 > len(self.imgs)-1:
                    self.skin1 = 0

                # Guarda todas as skins disponíveis para seleção
                screen.blit(pygame.transform.scale(self.imgs[self.skin1],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(screen.get_width()//2-screen.get_height()//3.5,screen.get_height()//6))
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_d:
                    self.skin1 += 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_a:
                    self.skin1 -= 1
            
            case 4: # Menu selseção de dois jogadores
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                #jogador 1
                self.botoes[10].update()
                self.botoes[11].update()
                self.botoes[12].update()
                self.botoes[13].update()
                #jogador 2
                self.botoes[14].update()
                self.botoes[15].update()
                self.botoes[16].update()
                self.botoes[17].update()
                #voltar
                self.botoes[18].update()
                #divisoria
                self.botoes[19].update()

                if self.skin1 < 0:
                    self.skin1 = len(self.imgs)-1
                elif self.skin1 > len(self.imgs)-1:
                    self.skin1 = 0
                
                if self.skin2 < 0:
                    self.skin2 = len(self.imgs)-1
                elif self.skin2 > len(self.imgs)-1:
                    self.skin2 = 0

                # Guarda todas as skins disponíveis para seleção
                screen.blit(pygame.transform.scale(self.imgs[self.skin1],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(screen.get_width()//4-screen.get_height()//3.5,screen.get_height()//6))
                screen.blit(pygame.transform.scale(self.imgs[self.skin2],tuple(a*b for a,b in zip((4,4),(screen.get_height()//7,screen.get_height()//7)))),(3*screen.get_width()//4-screen.get_height()//3.5,screen.get_height()//6))

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_LEFT:
                    self.skin2 -= 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_RIGHT:
                    self.skin2 += 1

                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_d:
                    self.skin1 += 1
                
                if self.tecla_pres[0] == True and self.tecla_pres[1] == True and self.tecla_pres[2] == pygame.K_a:
                    self.skin1 -= 1
                
                if self.jogadores_prontos == [True,True]:
                    self.janela_atual = 5
                    self.jogadores_prontos = [False,False]

            case 5:
                screen.fill(CORES["Preto"])
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

    def pegar_mouse(self, pos, botão=None):
        for botões in self.botoes:
            if botões.mouse_porCima(pos):
                if botões.mouse_click(botão):
                    if botões.id==2 and (self.janela_atual==1 or self.janela_atual==2):
                        self.janela_atual+=1
                        break
                    if botões.id==3 and self.janela_atual==2:
                        self.janela_atual+=2
                        break
                    if botões.id==4 and (self.janela_atual==1 or self.janela_atual==2):
                        self.janela_atual-=1
                        break
                    elif self.janela_atual==3:
                        if botões.id==6:
                            self.skin1 -= 1
                            break
                        if botões.id==7:
                            self.skin1 += 1
                            break
                        if botões.id==8:
                            self.janela_atual+=2
                            break
                        if botões.id==9:
                            self.janela_atual-=1
                            break
                    elif self.janela_atual==4:
                        if botões.id==11:
                            self.skin1 -= 1
                            break
                        if botões.id==12:
                            self.skin1 += 1
                            break
                        if botões.id==13:
                            self.jogadores_prontos[0]= not self.jogadores_prontos[0]
                            break
                        if botões.id==15:
                            self.skin1 -= 1
                            break
                        if botões.id==16:
                            self.skin1 += 1
                            break
                        if botões.id==17:
                            self.jogadores_prontos[1]= not self.jogadores_prontos[1]
                            break
                        if botões.id==18:
                            self.janela_atual-=2
                            break
                    

    def pegar_tecla_apertada(self,TECLAS_APERTADAS):
        self.tecla_pres = TECLAS_APERTADAS

    def selecionar_skin(self):
        return self.skin1    