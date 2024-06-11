import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player


#criação do sprite do jogador e inimigos
#trocar isso pra uma condicional antes da fase 1 e dps da seleceção de modelo
player = Player(0, 0)
player2 = Player(1, 17)
players.add(player)
players.add(player2)

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
        
    def atualizar_janela(self,mouse:tuple,key)->None:

        self.ciclo += 1
        if self.ciclo > 100:
            self.ciclo = 0
            
        match self.janela_atual:

            case 0: # Menu inical

                tempo_oscilação = 30
                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  screen.blit(MENSAGEM("ESPAÇO")[0],MENSAGEM("ESPAÇO")[1])
                else:
                  pass

            case 1: # Menu Principal

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)
                
                #isso tem que passar na game mas so receber o valor do mouse quando rolar um evento de click
                #pega as coordenadas e o botão usado. Ai´verifica as condições aqui
                #deve impedir o click duplo

                #para mudar de cor, pode usar o evento pygame.MOUSEMOTION

                #mas pygame.mouse.get_pressed é so para eventos que se repetem
                if(mouse[0] >= CAIXA("CAMPANHA:Branco")[0] and mouse[0] <= (CAIXA("CAMPANHA:Branco")[0]+CAIXA("CAMPANHA:Branco")[2])) and (mouse[1] >= CAIXA("CAMPANHA:Branco")[1] and mouse[1] <= (CAIXA("CAMPANHA:Branco")[1]+CAIXA("CAMPANHA:Branco")[3])):

                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("CAMPANHA:Vermelho"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Vermelho")[0],MENSAGEM("CAMPANHA:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = 2
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("CAMPANHA:Branco"),2)
                    screen.blit(MENSAGEM("CAMPANHA:Branco")[0],MENSAGEM("CAMPANHA:Branco")[1])

                if(mouse[0] >= CAIXA("VERSUS:Branco")[0] and mouse[0] <= (CAIXA("VERSUS:Branco")[0]+CAIXA("VERSUS:Branco")[2])) and (mouse[1] >= CAIXA("VERSUS:Branco")[1] and mouse[1] <= (CAIXA("VERSUS:Branco")[1]+CAIXA("VERSUS:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VERSUS:Vermelho"),2)
                    screen.blit(MENSAGEM("VERSUS:Vermelho")[0],MENSAGEM("VERSUS:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        print("Apertei2")
                
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VERSUS:Branco"),2)
                    screen.blit(MENSAGEM("VERSUS:Branco")[0],MENSAGEM("VERSUS:Branco")[1])

                if(mouse[0] >= CAIXA("VOLTAR:Branco")[0] and mouse[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (mouse[1] >= CAIXA("VOLTAR:Branco")[1] and mouse[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = 0

                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("VOLTAR:Branco"),2)
                    screen.blit(MENSAGEM("VOLTAR:Branco")[0],MENSAGEM("VOLTAR:Branco")[1])
            
            #mesmo ponto acima
            case 2: # Menu número de jogadores

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Branco"],CAIXA("TÍTULO"),2)

                if(mouse[0] >= CAIXA("1_JOGADOR:Branco")[0] and mouse[0] <= (CAIXA("1_JOGADOR:Branco")[0]+CAIXA("1_JOGADOR:Branco")[2])) and (mouse[1] >= CAIXA("1_JOGADOR:Branco")[1] and mouse[1] <= (CAIXA("1_JOGADOR:Branco")[1]+CAIXA("1_JOGADOR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("1_JOGADOR:Vermelho"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Vermelho")[0],MENSAGEM("1_JOGADOR:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = 5
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("1_JOGADOR:Branco"),2)
                    screen.blit(MENSAGEM("1_JOGADOR:Branco")[0],MENSAGEM("1_JOGADOR:Branco")[1])

                if(mouse[0] >= CAIXA("2_JOGADORES:Branco")[0] and mouse[0] <= (CAIXA("2_JOGADORES:Branco")[0]+CAIXA("2_JOGADORES:Branco")[2])) and (mouse[1] >= CAIXA("2_JOGADORES:Branco")[1] and mouse[1] <= (CAIXA("2_JOGADORES:Branco")[1]+CAIXA("2_JOGADORES:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("2_JOGADORES:Vermelho"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Vermelho")[0],MENSAGEM("2_JOGADORES:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
                        self.janela_atual = 5
                
                else:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("2_JOGADORES:Branco"),2)
                    screen.blit(MENSAGEM("2_JOGADORES:Branco")[0],MENSAGEM("2_JOGADORES:Branco")[1])

                if(mouse[0] >= CAIXA("VOLTAR:Branco")[0] and mouse[0] <= (CAIXA("VOLTAR:Branco")[0]+CAIXA("VOLTAR:Branco")[2])) and (mouse[1] >= CAIXA("VOLTAR:Branco")[1] and mouse[1] <= (CAIXA("VOLTAR:Branco")[1]+CAIXA("VOLTAR:Branco")[3])):
                    pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("VOLTAR:Vermelho"),2)
                    screen.blit(MENSAGEM("VOLTAR:Vermelho")[0],MENSAGEM("VOLTAR:Vermelho")[1])
                    if pygame.mouse.get_pressed()[0]:
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
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("JOGADOR_CENTRO"),2)
                screen.blit(MENSAGEM("JOGADOR_CENTRO")[0],MENSAGEM("JOGADOR_CENTRO")[1])

                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_A_CENTRO")[0],MENSAGEM("BOTAO_A_CENTRO")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D_CENTRO"),2)
                screen.blit(MENSAGEM("BOTAO_D_CENTRO")[0],MENSAGEM("BOTAO_D_CENTRO")[1])

                if self.skin1 < 0 or self.skin1 > 13:
                    self.skin1 = 0
                
                # Guarda todas as skins disponíveis para seleção
                self.imgs = []
                #for i in range(14):
                    #self.imgs.append(pygame.transform.scale(pygame.image.load(imagens_naves_selecao).subsurface((i%10*64,0),(64,64)).convert_alpha(),tuple(a*b for a,b in zip((4,4),tamanho_nave()))))
                
                screen.blit(self.imgs[self.skin1],(CAIXA("NAVE_SELECAO_CENTRO")[0],CAIXA("NAVE_SELECAO_CENTRO")[1]))
    
                if key[pygame.K_d]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D_CENTRO"),2)
                    self.skin1 += 1
                
                if key[pygame.K_a]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D_CENTRO"),2)
                    self.skin1 -= 1

                if key[pygame.K_SPACE]:
                    self.janela_atual = 5
            
            case 4: # Menu selseção de dois jogadores

                screen.fill(CORES["Azul do ceu"])
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("DIVISORIA"))
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("JOGADOR_1_ESQUERDA"),2)
                screen.blit(MENSAGEM("JOGADOR_1_ESQUERDA")[0],MENSAGEM("JOGADOR_1_ESQUERDA")[1])

                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("JOGADOR_2_DIREITA"),2)
                screen.blit(MENSAGEM("JOGADOR_2_DIREITA")[0],MENSAGEM("JOGADOR_2_DIREITA")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_A"),2)
                screen.blit(MENSAGEM("BOTAO_A")[0],MENSAGEM("BOTAO_A")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_D"),2)
                screen.blit(MENSAGEM("BOTAO_D")[0],MENSAGEM("BOTAO_D")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_<"),2)
                screen.blit(MENSAGEM("BOTAO_<")[0],MENSAGEM("BOTAO_<")[1])
                
                pygame.draw.rect(screen,CORES["Vermelho"],CAIXA("BOTAO_>"),2)
                screen.blit(MENSAGEM("BOTAO_>")[0],MENSAGEM("BOTAO_>")[1])

                if self.skin1 < 0 or self.skin1 > 13:
                    self.skin1 = 0
                
                if self.skin2 < 0 or self.skin2 > 13:
                    self.skin2 = 0

                # Guarda todas as skins disponíveis para seleção
                self.imgs = []
                for i in range(14):
                    self.imgs.append(pygame.transform.scale(pygame.image.load(imagens_naves_selecao).subsurface((i%10*64,0),(64,64)).convert_alpha(), tuple(a*b for a,b in zip((3,3),tamanho_nave()))))
                
                screen.blit(self.imgs[self.skin1],(CAIXA("NAVE_SELECAO_1")[0],CAIXA("NAVE_SELECAO_1")[1]))
                screen.blit(self.imgs[self.skin2],(CAIXA("NAVE_SELECAO_2")[0],CAIXA("NAVE_SELECAO_2")[1]))
                
                if key[pygame.K_LEFT]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_<"),2)
                    self.skin2 += 1
                
                if key[pygame.K_RIGHT]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_>"),2)
                    self.skin2 -= 1

                if key[pygame.K_d]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_D"),2)
                    self.skin1 += 1
                
                if key[pygame.K_a]:
                    pygame.draw.rect(screen,CORES["Branco"],CAIXA("BOTAO_A"),2)
                    self.skin1 -= 1

                if key[pygame.K_SPACE]:
                    self.janela_atual = 5

            #criar os players aqui para não ser possivel criar antes. alem disso, ver a criação de um menu pause para retornar
            #ao menu inicial por exemplo mas pode voltar pra menus diferentes
            case 5: # Fases do jogo
           
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
