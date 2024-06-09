import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player

#criação do sprite do jogador e inimigos
#trocar isso pra uma condicional antes da fase 1 e dps da seleceção de modelo
player = Player(0, 17)
player2 = Player(1, 16)
players.add(player)
players.add(player2)

class Janelas:
    def __init__(self)->None:
        #atributos para acompanhamento dos eventos
        self.ciclo = 0
        self.janela_atual = JANELAS[0]
        self.scroll = 0
        
    def atualizar_janela(self,mouse:tuple,key)->None:

        self.ciclo+=1
        if self.ciclo>100:
            self.ciclo=0
        match self.janela_atual:
            case "Menu Inicial 1":
                tempo_oscilação = 30
                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])
                else:
                  pass

            case "Menu Inicial 2":

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)

                if(mouse[0] >= CAIXA("CAMPANHA:Branco")[0] and mouse[0] <= (CAIXA("CAMPANHA:Branco")[0]+CAIXA("CAMPANHA:Branco")[2])) and (mouse[1] >= CAIXA("CAMPANHA:Branco")[1] and mouse[1] <= (CAIXA("CAMPANHA:Branco")[1]+CAIXA("CAMPANHA:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("CAMPANHA:Vermelho"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Vermelho")[0],MENSAGEM("CAMPANHA:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = JANELAS[2]
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("CAMPANHA:Branco"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Branco")[0],MENSAGEM("CAMPANHA:Branco")[1])

                if(mouse[0] >= CAIXA("VERSUS:Branco")[0] and mouse[0] <= (CAIXA("VERSUS:Branco")[0]+CAIXA("VERSUS:Branco")[2])) and (mouse[1] >= CAIXA("VERSUS:Branco")[1] and mouse[1] <= (CAIXA("VERSUS:Branco")[1]+CAIXA("VERSUS:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VERSUS:Vermelho"),2)
                    screen.blit(MENSAGEM("VERSUS:Vermelho")[0],MENSAGEM("VERSUS:Vermelho")[1])
                
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VERSUS:Branco"),2)
                    screen.blit(MENSAGEM("VERSUS:Branco")[0],MENSAGEM("VERSUS:Branco")[1])

                if(mouse[0] >= CAIXA("SAIR:Branco")[0] and mouse[0] <= (CAIXA("SAIR:Branco")[0]+CAIXA("SAIR:Branco")[2])) and (mouse[1] >= CAIXA("SAIR:Branco")[1] and mouse[1] <= (CAIXA("SAIR:Branco")[1]+CAIXA("SAIR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("SAIR:Vermelho"),2)
                    screen.blit(MENSAGEM("SAIR:Vermelho")[0],MENSAGEM("SAIR:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = JANELAS[0]

                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("SAIR:Branco"),2)
                    screen.blit(MENSAGEM("SAIR:Branco")[0],MENSAGEM("SAIR:Branco")[1])
            
            case "Menu Seleção Skins":

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("DIVISORIA"))
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("JOGAR_PLAYER_1"),2)
                screen.blit(MENSAGEM("JOGADOR_1")[0],MENSAGEM("JOGADOR_1")[1])

                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("JOGAR_PLAYER_2"),2)
                screen.blit(MENSAGEM("JOGADOR_2")[0],MENSAGEM("JOGADOR_2")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A"),2)
                screen.blit(MENSAGEM("A")[0],MENSAGEM("A")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D"),2)
                screen.blit(MENSAGEM("D")[0],MENSAGEM("D")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_<"),2)
                screen.blit(MENSAGEM("<")[0],MENSAGEM("<")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_>"),2)
                screen.blit(MENSAGEM(">")[0],MENSAGEM(">")[1])

                screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])
                if key[pygame.K_SPACE]:
                    self.janela_atual = JANELAS[3]

            case "Fase 1":
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.
                if self.scroll < background_altura-background_largura-1:
                    self.scroll += 1
                else:
                    self.scroll = 0
                BACKGROUND = pygame.image.load(background).subsurface((0,background_altura-background_largura-self.scroll),(128,128)).convert_alpha()

                screen.blit(pygame.transform.scale(BACKGROUND,(screen.get_width(),screen.get_height())),(0,0))
                
                #gera os aliens
                if len(aliens) < random.randint(2,3) and pygame.time.get_ticks()%50 > 45:
                    aliens.add(Alien((random.randint(150,screen.get_width()-150),-30), random.randint(0,3)))

                players.draw(screen)
                players.update(aliens)
                aliens.draw(screen)
                aliens.update(players)
                drops.draw(screen)
                drops.update(players)

            case _:
                pass
