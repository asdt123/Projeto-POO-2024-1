import pygame
import random
from configurações.Config import *
from modulos.personagens.Conta import *
from modulos.personagens.Player import Player
from modulos.personagens.Alien import Alien
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
        self.num_players = 0
        self.player = Player(0,0)
        self.player2 = Player(1,0)

        #botoes utilizados
        self.botoes = []
        for i in range(25):
            self.botoes.append(Botões(i))

        # Guarda todas as skins disponíveis para seleção
        self.imgs = []
        for i in range(14):
            self.imgs.append(pygame.image.load(imagens_naves_selecao).subsurface((i*64,0),(64,64)).convert_alpha())


        self.text = ""
        self.id_contas = 0
        self.conta = Conta()
        self.cadastro = Cadastro()


        # Carregar a imagem lateral
        self.informacao_bg = []
        for i in range(2):
            self.informacao_bg.append(pygame.image.load("imagens/cenario/informacao.png").convert_alpha())

        #carrega o backgorund
        self.background = []
        for i in range(4):
            self.background.append(pygame.image.load("imagens/cenario/menu_inicial.png").subsurface((0,600*i), (900, 600)).convert_alpha())
        self.index_b = 0
        
        # Carrega as imagens do título
        self.titulo_img_id = 0
        self.titulo_img = []
        for i in range(3):
            self.titulo_img.append(pygame.image.load(imagem_titulo).subsurface((512*i,0,512,256)).convert_alpha())


    def desenhar_info_jogadores(self)->None:
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
        self.botoes[15].alterar_texto("<")
        self.botoes[16].alterar_texto(">")
        self.botoes[17].alterar_texto("Pressione", 'ESTATICO')
        self.botoes[18].alterar_texto("Voltar")
        self.botoes[19].alterar_texto("", 'BOX')   
        self.botoes[20].alterar_texto("| |")
        self.botoes[21].alterar_texto("Confirmar")
        self.botoes[22].alterar_texto(self.text)
        self.botoes[23].alterar_texto("Nome:",'NORMAL')
        self.botoes[24].alterar_texto("Rank")

        #contagem de ciclos, a cada 30 frames conta um
        self.ciclo += 1
        if self.ciclo > 100:
            self.ciclo = 0
        
        #atualização do fundo
        self.index_b += 0.11
        if self.index_b > len(self.background):
            self.index_b = 0    
        
        #mudar imagens do título
        if self.ciclo%20 == 1:
            self.titulo_img_id += 1
        if self.titulo_img_id > 2:
            self.titulo_img_id = 0
        #impressão da janela
        match self.janela_atual:

            case 0: # Menu inical

                self.background.clear()
                for i in range(4):
                    self.background.append(pygame.image.load("imagens/cenario/menu_inicial.png").subsurface((0,600*i), (900, 600)).convert_alpha())
                tempo_oscilação = 30
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                screen.blit(pygame.transform.scale(self.titulo_img[self.titulo_img_id],(int(0.6*screen.get_width()),int(0.45*screen.get_height()))),(int(0.26*screen.get_width()),int(0.038*screen.get_height())))
                #self.botoes[1].update()

                #texto oscila de 15 em 15 ciclos
                if self.ciclo%tempo_oscilação<(tempo_oscilação//2):
                  self.botoes[0].update()
                else:
                  pass
                

            case 1: # Menu Principal

                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                screen.blit(pygame.transform.scale(self.titulo_img[self.titulo_img_id],(int(0.6*screen.get_width()),int(0.45*screen.get_height()))),(int(0.26*screen.get_width()),int(0.038*screen.get_height())))
                self.botoes[2].update()
                self.botoes[3].update()
                self.botoes[4].update()
                self.botoes[24].update()              

            case 2: # Menu número de jogadores
                self.skin1=20
                self.skin2=20
                
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                self.botoes[2].alterar_texto("1 jogador")
                self.botoes[3].alterar_texto("2 jogadores")
                screen.blit(pygame.transform.scale(self.titulo_img[self.titulo_img_id],(int(0.6*screen.get_width()),int(0.45*screen.get_height()))),(int(0.26*screen.get_width()),int(0.038*screen.get_height())))
                self.botoes[2].update()
                self.botoes[3].update()
                self.botoes[4].update()       

            case 3: # Definir nick do jogador solo
                self.num_players = 1
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                screen.blit(pygame.transform.scale(self.titulo_img[self.titulo_img_id],(int(0.6*screen.get_width()),int(0.45*screen.get_height()))),(int(0.26*screen.get_width()),int(0.038*screen.get_height())))
                
                if self.tecla_pres[0] == True:
    
                    if self.tecla_pres[2] == pygame.K_BACKSPACE:
                        self.text = self.text[:-1] 

                    else:

                        if len(self.text) != 3:
                            self.text += (chr(self.tecla_pres[2])).upper()

                        else:
                            pass
                
                self.botoes[4].update()
                self.botoes[21].update()
                self.botoes[22].update()
                self.botoes[23].update()

            case 4: # Definir nick da dupla
                self.num_players = 2
                
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                screen.blit(pygame.transform.scale(self.titulo_img[self.titulo_img_id],(int(0.6*screen.get_width()),int(0.45*screen.get_height()))),(int(0.26*screen.get_width()),int(0.038*screen.get_height())))
                
                if self.tecla_pres[0] == True:
    
                    if self.tecla_pres[2] == pygame.K_BACKSPACE:
                        self.text = self.text[:-1] 
                    
                    else:

                        if len(self.text) != 6:
                            self.text += (chr(self.tecla_pres[2])).upper()

                        else:
                            pass
                
                self.botoes[4].update()
                self.botoes[21].update()
                self.botoes[22].update()
                self.botoes[23].update()

            case 5: # Menu seleção de jogador unico
                
                screen.blit(pygame.transform.scale(self.background[int(self.index_b)], (screen.get_width(), screen.get_height())), (0,0))
                #jogador
                self.botoes[5].update()
                self.botoes[6].update()
                self.botoes[7].update()
                self.botoes[8].update()
                self.botoes[9].update()
                #invalidar skin 2
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
            
            case 6: # Menu selseção de dois jogadores
                
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
                    self.janela_atual = 7
                    self.jogadores_prontos = [False,False]

            case 7: # Criar jogadores
                self.botoes[13].ressaltado=False
                self.botoes[17].ressaltado=False

                self.scroll = 0
                screen.fill(CORES["Preto"])
                players.empty()
                if self.skin1 < 4:
                    self.player = Player(0,self.skin1*2)
                else:
                    self.player = Player(0,self.skin1+4)
                players.add(self.player)
                
                if self.skin2 != 20:
                    if self.skin2 < 4:
                        self.player2 = Player(1,self.skin2*2)
                    else:
                        self.player2 = Player(1,self.skin2+4)
                    players.add(self.player2)

                self.janela_atual = 8
                self.scroll = 0

                aliens.empty()
                self.animações.empty()

                self.background.clear()
                self.background.append(pygame.image.load("imagens/cenario/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha())

            case 8: # Fases do jogo
                
                if self.scroll < background_altura-background_largura-1:
                    self.scroll += 0.5
                else:
                    self.janela_atual = 11
                if self.janela_atual == 8:
                    # Calcular áreas dinâmicas
                    
                    info_width = screen.get_width()//6
                    cenario_width = screen.get_width() - 2 * info_width
                    
                    self.background[0] = pygame.image.load("imagens/cenario/Cenarios.png").subsurface((0, 2500 - 128 - int(self.scroll)), (128, 128)).convert_alpha()


                    if len(self.animações) < random.randint(2, 3) and self.ciclo%3==0 and self.scroll<1500:
                        self.animações.add(Animação(random.randint(info_width, info_width+cenario_width), random.randint(0, 1)))

                    if len(aliens) < random.randint(2,3) and self.ciclo%5==0:
                        aliens.add(Alien(random.randint(info_width, info_width+cenario_width), random.randint(self.scroll//1100, self.scroll//600)))
                    
                    if len(players) == 0:
                        self.janela_atual = 9
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
                    self.botoes[20].update()

            case 9: # Perdeu o jogo  
                
                info_width = screen.get_width()//6
                cenario_width = screen.get_width() - 2 * info_width
                screen.blit(pygame.transform.scale(self.background[0], (cenario_width, screen.get_height())), (info_width, 0))
                self.botoes[1].alterar_texto("GAME OVER", 'TITULO')
                self.botoes[2].alterar_texto("De Novo")
                self.botoes[3].alterar_texto("Voltar")
                self.botoes[1].update()
                self.botoes[2].update()
                self.botoes[3].update()

            case 10: # Pause

                info_width = screen.get_width()//6
                cenario_width = screen.get_width() - 2 * info_width
                screen.blit(pygame.transform.scale(self.background[0], (cenario_width, screen.get_height())), (info_width, 0))
                self.botoes[1].alterar_texto("PAUSE", 'TITULO')
                self.botoes[2].alterar_texto("CONTINUAR")
                self.botoes[3].alterar_texto("MENU")
                self.botoes[1].update()
                self.botoes[2].update()
                self.botoes[3].update()
            
            case 11: # Venceu o jogo   
                info_width = screen.get_width()//6
                cenario_width = screen.get_width() - 2 * info_width
                screen.blit(pygame.transform.scale(self.background[0], (cenario_width, screen.get_height())), (info_width, 0))
                self.botoes[1].alterar_texto("PARABENS", 'TITULO')
                self.botoes[2].alterar_texto("De Novo")
                self.botoes[3].alterar_texto("MENU")
                self.botoes[1].update()
                self.botoes[2].update()
                self.botoes[3].update()
                
            case 12: # Tabela dos 7 melhores solo e dupla

                screen.fill(CORES["Preto"])
                self.botoes[10].alterar_texto("Solo",'NORMAL')
                self.botoes[14].alterar_texto("Dupla",'NORMAL')
                self.botoes[10].update()
                self.botoes[14].update()
                self.botoes[18].update()
                self.botoes[19].update()

                conn = sqlite3.connect('database/jogadores.db')
                cursor = conn.cursor()
                #solo
                cursor.execute('SELECT nome, pontuacao FROM solo ORDER BY pontuacao DESC limit 7')
                dados = cursor.fetchall()
                
                offset = screen.get_height()//10;
                for nome, pontuacao in dados:
                    texto = self.botoes[10].fonte.render(f"{nome}    {pontuacao}", True, CORES["Branco"])
                    screen.blit(texto, (self.botoes[10].rect.x, self.botoes[10].rect.y+offset))
                    offset += screen.get_height()//10  # Espaçamento entre as linhas
                cursor.execute('SELECT nome, pontuacao FROM solo ORDER BY pontuacao DESC')
                dados = cursor.fetchall()
                
                #solo
                cursor.execute('SELECT nome, pontuacao FROM dupla ORDER BY pontuacao DESC limit 7')
                dados = cursor.fetchall()
                offset = screen.get_height()//10;
                for nome, pontuacao in dados:
                    texto = self.botoes[14].fonte.render(f"{nome}     {pontuacao}", True, CORES["Branco"])
                    screen.blit(texto, (self.botoes[14].rect.x, self.botoes[14].rect.y+offset))
                    offset += screen.get_height()//10  # Espaçamento entre as linhas

        # "Limpa" o mouse e o teclado para evitar clicks indevidos
        if self.tecla_pres[0:2] == [True,True]:
            self.tecla_pres = [False,False,pygame.K_0]
        elif self.tecla_pres[0] == True and (self.janela_atual == 3 or self.janela_atual == 4):
            self.tecla_pres = [False,False,pygame.K_0]
        else:
            pass
    
    def pegar_mouse(self, pos:tuple[int,int,int,int], botão=None)->None:
        for botões in self.botoes:
            if botões.mouse_porCima(pos):
                if botões.mouse_click(botão):
                    if botões.id == 2: 
                        if self.janela_atual == 1 or self.janela_atual == 2:
                            self.janela_atual += 1
                            break
                        if self.janela_atual == 9:
                            if self.num_players == 1:
                                self.conta.set_pontos(0.95*self.player.pontos)
                            elif self.num_players == 2:
                                self.conta.set_pontos(0.95*(self.player.pontos+self.player2.pontos)//2) 
                            self.cadastro.registrar(self.conta)
                            self.cadastro.salvar_banco_dados(self.num_players)
                            self.janela_atual = 7
                            break
                        if self.janela_atual == 11:
                            if self.num_players == 1:
                                self.conta.set_pontos(self.player.vidas*200+self.player.pontos*1.05)
                            elif self.num_players == 2:
                                self.conta.set_pontos((self.player.vidas*200+self.player.pontos+self.player2.vidas*200+self.player2.pontos)//2)
                            
                            self.cadastro.registrar(self.conta)
                            self.cadastro.salvar_banco_dados(self.num_players)              
                            self.janela_atual = 7
                            break
                        if self.janela_atual == 10:
                            self.janela_atual = 8
                            break
                    if botões.id == 3:
                        if self.janela_atual == 2:
                            self.janela_atual += 2
                            break

                        if self.janela_atual == 9:
                            if self.num_players == 1:
                                self.conta.set_pontos(0.95*self.player.pontos)
                            elif self.num_players == 2:
                                self.conta.set_pontos(0.95*(self.player.pontos+self.player2.pontos)//2) 
                            self.cadastro.registrar(self.conta)
                            self.cadastro.salvar_banco_dados(self.num_players)
                            self.janela_atual = 0
                            break
                        if self.janela_atual == 11:
                            if self.num_players == 1:
                                self.conta.set_pontos(self.player.vidas*200+self.player.pontos*1.05)
                            elif self.num_players == 2:
                                self.conta.set_pontos((self.player.vidas*200+self.player.pontos+self.player2.vidas*200+self.player2.pontos)//2)
                            
                            self.cadastro.registrar(self.conta)
                            self.cadastro.salvar_banco_dados(self.num_players)              
                            self.janela_atual = 0
                            break
                        elif self.janela_atual == 10:
                            self.janela_atual = 0
                            
                            break

                    if botões.id == 4 and (self.janela_atual == 1 or self.janela_atual == 2 or self.janela_atual == 3):
                        
                        self.janela_atual -= 1
                        while len(self.text) != 0:
                            self.text = self.text[:-1]
                        break

                    if botões.id == 4 and self.janela_atual == 4:
                        
                        self.janela_atual -= 2
                        while len(self.text) != 0:
                            self.text = self.text[:-1]
                        break
                    
                    if botões.id == 4 and self.janela_atual == 12:
                        
                        self.janela_atual = 1
                        break

                    if botões.id == 21:
                        if self.janela_atual == 3: 
                        
                            self.conta.set_nome(self.text)
                        
                            if len(self.text) == 3:
                                self.janela_atual += 2
                                while len(self.text) != 0:
                                    self.text = self.text[:-1]
                            else:
                                pass
                            break
                        if self.janela_atual == 4:
                            self.conta.set_nome(self.text)
                        
                            if len(self.text) == 6:
                                self.janela_atual += 2
                                while len(self.text) != 0:
                                    self.text = self.text[:-1]
                            else:
                                pass
                            break
                    if self.janela_atual == 12:
                        if botões.id == 24:
                            self.janela_atual=1
                            break
                    if botões.id == 24 and self.janela_atual == 1:
                        self.janela_atual = 12
                        break
                    elif self.janela_atual == 5:
                        if botões.id == 6:
                            self.skin1 -= 1
                            break
                        if botões.id == 7:
                            self.skin1 += 1
                            break
                        if botões.id == 8:
                            self.janela_atual += 2
                            break
                        if botões.id == 9:
                            self.janela_atual -= 2
                            break
                    elif self.janela_atual == 6:
                        if botões.id == 11:
                            self.skin1 -= 1
                            break
                        if botões.id == 12:
                            self.skin1 += 1
                            break
                        if botões.id == 13:
                            self.jogadores_prontos[0] = not self.jogadores_prontos[0]
                            break
                        if botões.id == 15:
                            self.skin2 -= 1
                            break
                        if botões.id == 16:
                            self.skin2 += 1
                            break
                        if botões.id == 17:
                            self.jogadores_prontos[1] = not self.jogadores_prontos[1]
                            break
                        if botões.id == 18:
                            self.janela_atual -= 2
                            break
                    elif self.janela_atual == 8:
                        if botões.id == 20:
                            self.janela_atual = 10
                            break
                    

    def pegar_tecla_apertada(self,TECLAS_APERTADAS)->None:
        self.tecla_pres = TECLAS_APERTADAS


    def selecionar_skin(self)->int:
        return self.skin1 
    
    def get_janela_atual(self)->int:
        return self.janela_atual 
