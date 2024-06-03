import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player
import math

#criação do sprite do jogador e inimigos
player = Player(screen.get_width()-150, 17)
player2 = Player(25, 16)
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
aliens = pygame.sprite.Group() 

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
                
                fonte = pygame.font.SysFont("fontes/Star_fighters-Regular.ttf",MENSAGEM("ESPAÇO")[1], True, True)
                mensagem = f"PRECIONE ESPAÇO"
                format_text = fonte.render(mensagem, False, (255,255,255))

                self.screen.blit(format_text,MENSAGEM("ESPAÇO")[0])

            case "Menu Inicial 2":

                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("CAMPANHA"),2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("VERSUS"),2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA("SAIR"),2)

            case "Fase 1":
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.
                BACKGROUND = pygame.image.load("imagens/cenário/cenario.png").subsurface((0,3000-128-self.scroll),(128,128)).convert_alpha()
                if self.scroll < 3000:
                    self.scroll += 2 *math.ceil(screen.get_height()/600)
                else:
                    self.scroll = 0
                self.screen.blit(pygame.transform.scale(BACKGROUND,(self.screen.get_width(),self.screen.get_height())),(0,0))
                
                #gera os aliens
                if len(aliens) < random.randint(2,3) and pygame.time.get_ticks()%50 > 45:
                    aliens.add(Alien((random.randint(50,800),-30), random.randint(0,1)))
                screen.fill(CORES["Azul Escuro"])
                #screen.blit(pygame.transform.scale(BACKGROUND, (screen.get_width(),screen.get_height())),(0,0))
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
