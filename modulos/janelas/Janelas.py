import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player

pygame.init()

#criação do sprite do jogador e inimigos
player = Player(650, 0)
player2 = Player(25, 8)
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
aliens = pygame.sprite.Group() 

class Janelas:
    def __init__(self,screen:pygame.Surface,janela:str)->None:

        self.screen = screen
        self.janela_atual = janela
        
    def atualizar_janela(self):

        match self.janela_atual:
            case "Menu Inicial 1":

                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA_TÍTULO,2)
                mensagem = f"Precione \"espaço\""
                format_text = FONTE.render(mensagem,False,CORES["Preto"])
                self.screen.blit(format_text,MENSAGEM_POSIÇÃO[0])
            
            case "Menu Inicial 2":

                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA_TÍTULO,2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA_CAMPANHA,2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA_VERSUS,2)
                pygame.draw.rect(self.screen,CORES["Branco"],CAIXA_SAIR,2)

            case "Fase 1":

                if len(aliens) < random.randint(2,3) and pygame.time.get_ticks()%50 > 45:
                    aliens.add(Alien((random.randint(50,800),-30), random.randint(0,1)))
                
                self.screen.blit(pygame.transform.scale(BACKGROUND, (screen.get_width(),screen.get_height())),(0,0))

                players.draw(self.screen)
                players.update(self.screen,aliens)
                aliens.draw(self.screen)
                aliens.update(self.screen,players)

            case _:
                pass
    
    def mudar_janela(self,índice_janela:int,mouse_posição:tuple)->None:
        
        self.janela_atual = JANELAS[índice_janela]
        
