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

        self.screen = screen
        self.janela_atual = JANELAS[0]
        self.scroll = 0
        
    def atualizar_janela(self)->None:

        match self.janela_atual:
            case "Menu Inicial 1":
                
                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])

            case "Menu Inicial 2":

                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("CAMPANHA"),2)
                screen.blit(MENSAGEM("CAMPANHA")[0],MENSAGEM("CAMPANHA")[1])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("VERSUS"),2)
                screen.blit(MENSAGEM("VERSUS")[0],MENSAGEM("VERSUS")[1])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("SAIR"),2)
                screen.blit(MENSAGEM("SAIR")[0],MENSAGEM("SAIR")[1])

            case "Fase 1":
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.
                if self.scroll < background_altura-background_largura-1:
                    self.scroll += 1
                else:
                    self.scroll = 0
                BACKGROUND = pygame.image.load(background).subsurface((0,background_altura-background_largura-self.scroll),(128,128)).convert_alpha()

                self.screen.blit(pygame.transform.scale(BACKGROUND,(self.screen.get_width(),self.screen.get_height())),(0,0))
                
                #gera os aliens
                if len(aliens) < random.randint(2,3) and pygame.time.get_ticks()%50 > 45:
                    aliens.add(Alien((random.randint(150,screen.get_width()-150),-30), random.randint(0,1)))

                players.draw(screen)
                players.update(aliens)
                aliens.draw(screen)
                aliens.update(players)

            case _:
                pass

    def mudar_janela(self,mouse:tuple)->None:

        if self.janela_atual == JANELAS[1]:    
            if (mouse[0] >= CAIXA("CAMPANHA")[0] and mouse[0] <= (CAIXA("CAMPANHA")[0]+CAIXA("CAMPANHA")[2])) and (mouse[1] >= CAIXA("CAMPANHA")[1] and mouse[1] <= (CAIXA("CAMPANHA")[1]+CAIXA("CAMPANHA")[3])):
                pygame.draw.rect(self.screen,CORES["Vermelho"],CAIXA("CAMPANHA"),2)
                if pygame.mouse.get_pressed()[0]:
                    self.janela_atual = JANELAS[2]
            if (mouse[0] >= CAIXA("VERSUS")[0] and mouse[0] <= (CAIXA("VERSUS")[0]+CAIXA("VERSUS")[2])) and (mouse[1] >= CAIXA("VERSUS")[1] and mouse[1] <= (CAIXA("VERSUS")[1]+CAIXA("VERSUS")[3])):
                pygame.draw.rect(self.screen,CORES["Vermelho"],CAIXA("VERSUS"),2)

            elif (mouse[0] >= CAIXA("SAIR")[0] and mouse[0] <= (CAIXA("SAIR")[0]+CAIXA("SAIR")[2])) and (mouse[1] >= CAIXA("SAIR")[1] and mouse[1] <= (CAIXA("SAIR")[1]+CAIXA("SAIR")[3])):
                pygame.draw.rect(self.screen,CORES["Vermelho"],CAIXA("SAIR"),2)
                if pygame.mouse.get_pressed()[0]:
                    self.janela_atual = JANELAS[0]
        else:
            pass
