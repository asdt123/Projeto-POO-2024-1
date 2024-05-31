import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player
import math

#criação do sprite do jogador e inimigos
player = Player(screen.get_width()-150, 0)
player2 = Player(25, 2)
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
aliens = pygame.sprite.Group() 

class Janelas:
    def __init__(self,janela:str)->None:

        self.janela_atual = janela
        self.scroll = 0
        
    def atualizar_janela(self):

        match self.janela_atual:
            case "Menu Inicial 1":

                screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA_TÍTULO,2)
                mensagem = f"Precione \"espaço\""
                format_text = FONTE.render(mensagem,False,CORES["Preto"])
                screen.blit(format_text,MENSAGEM_POSIÇÃO[0])
            
            case "Menu Inicial 2":

                screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA_TÍTULO,2)
                pygame.draw.rect(screen,CORES["Branco"],CAIXA_CAMPANHA,2)
                pygame.draw.rect(screen,CORES["Branco"],CAIXA_VERSUS,2)
                pygame.draw.rect(screen,CORES["Branco"],CAIXA_SAIR,2)

            case "Fase 1":
                #codigo para atualização do cenario, carrega so a parte que aparece na tela de baixo pra cima
                #logica basica da basica, tem que melhorar e alterar pro nosso cenario.
                BACKGROUND = pygame.image.load("imagens/cenário/cenario.png").subsurface((0,3000-128-self.scroll),(128,128)).convert_alpha()
                if self.scroll<3000:
                    self.scroll+=2*math.ceil(screen.get_height()/600)
                else:
                    self.scroll=0                
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
    
    def mudar_janela(self,índice_janela:int,mouse_posição:tuple)->None:
        
        self.janela_atual = JANELAS[índice_janela]
        
