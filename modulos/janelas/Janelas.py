import pygame
import random
from configurações.Config import *
from modulos.personagens.Alien import Alien
from modulos.personagens.Player import Player

# criação do sprite do jogador e inimigos
player = Player(25, 16)  # Player 1 na esquerda
player2 = Player(screen.get_width() - 150, 17)  # Player 2 na direita
players = pygame.sprite.Group()
players.add(player)
players.add(player2)
aliens = pygame.sprite.Group()

class Janelas:
    def __init__(self) -> None:
        self.screen = screen
        self.janela_atual = JANELAS[0]
        self.scroll = 0

        # Carregar a imagem de fundo
        self.informacao_bg = pygame.image.load("imagens/cenário/informacao.png").convert_alpha()

    def desenhar_info_jogadores(self):
        # Calcular áreas dinâmicas
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        info_width = 150
        cenario_width = screen_width - 2 * info_width

        # Desenha a imagem de fundo nas áreas de informações dos jogadores
        info_bg_left = pygame.transform.scale(self.informacao_bg, (info_width, screen_height))
        info_bg_right = pygame.transform.scale(self.informacao_bg, (info_width, screen_height))
        self.screen.blit(info_bg_left, (0, 0))
        self.screen.blit(info_bg_right, (screen_width - info_width, 0))

        # Informações do jogador 1 (esquerda)
        font = pygame.font.Font(None, 25)
        player1_info = font.render("Jogador 1", True, CORES["Branco"])
        self.screen.blit(player1_info, (20, 50))

        # Retângulos para representar as informações do jogador 1
        vida_rect = pygame.Rect(40, 100, 50, 50)  # Vida
        pygame.draw.rect(self.screen, CORES["Branco"], vida_rect, 2)

        score_rect = pygame.Rect(40, 170, 50, 50)  # Score
        pygame.draw.rect(self.screen, CORES["Branco"], score_rect, 2)

        nave_rect = pygame.Rect(40, 380, 50, 50)  # Nave Atual
        pygame.draw.rect(self.screen, CORES["Branco"], nave_rect, 2)

        municao_rect = pygame.Rect(40, 450, 50, 50)  # Munição Atual
        pygame.draw.rect(self.screen, CORES["Branco"], municao_rect, 2)

        # Informações do jogador 2 (direita)
        player2_info = font.render("Jogador 2", True, CORES["Branco"])
        self.screen.blit(player2_info, (screen_width - info_width + 20, 50))

        # Retângulos para representar as informações do jogador 2
        vida2_rect = pygame.Rect(screen_width - info_width + 40, 100, 50, 50)  # Vida
        pygame.draw.rect(self.screen, CORES["Branco"], vida2_rect, 2)

        score2_rect = pygame.Rect(screen_width - info_width + 40, 170, 50, 50)  # Score
        pygame.draw.rect(self.screen, CORES["Branco"], score2_rect, 2)

        nave2_rect = pygame.Rect(screen_width - info_width + 40, 380, 50, 50)  # Nave Atual
        pygame.draw.rect(self.screen, CORES["Branco"], nave2_rect, 2)

        municao2_rect = pygame.Rect(screen_width - info_width + 40, 450, 50, 50)  # Munição Atual
        pygame.draw.rect(self.screen, CORES["Branco"], municao2_rect, 2)

    def atualizar_janela(self) -> None:
        match self.janela_atual:
            case "Menu Inicial 1":
                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen, CORES["Branco"], CAIXA("TÍTULO"), 2)
                screen.blit(MENSAGEM("ESPAÇO")[0], MENSAGEM("ESPAÇO")[1])
            case "Menu Inicial 2":
                self.screen.fill(CORES["Azul Escuro"])
                pygame.draw.rect(self.screen, CORES["Branco"], CAIXA("TÍTULO"), 2)
                pygame.draw.rect(self.screen, CORES["Branco"], CAIXA("CAMPANHA"), 2)
                screen.blit(MENSAGEM("CAMPANHA")[0], MENSAGEM("CAMPANHA")[1])
                pygame.draw.rect(self.screen, CORES["Branco"], CAIXA("VERSUS"), 2)
                screen.blit(MENSAGEM("VERSUS")[0], MENSAGEM("VERSUS")[1])
                pygame.draw.rect(self.screen, CORES["Branco"], CAIXA("SAIR"), 2)
                screen.blit(MENSAGEM("SAIR")[0], MENSAGEM("SAIR")[1])
            case "Fase 1":
                if self.scroll < 2500 - 129:
                    self.scroll += 1
                else:
                    self.scroll = 0
                screen_width = self.screen.get_width()
                screen_height = self.screen.get_height()
                info_width = 150
                cenario_width = screen_width - 2 * info_width

                BACKGROUND = pygame.image.load("imagens/cenário/Cenarios.png").subsurface((0, 2500 - 128 - self.scroll), (128, 128)).convert_alpha()
                self.screen.blit(pygame.transform.scale(BACKGROUND, (cenario_width, screen_height)), (info_width, 0))

                if len(aliens) < random.randint(2, 3) and pygame.time.get_ticks() % 50 > 45:
                    aliens.add(Alien((random.randint(info_width + 50, info_width + cenario_width - 50), -30), random.randint(0, 1)))

                # Atualizar a posição dos jogadores para que fiquem dentro do cenário
                for player in players:
                    if player.rect.left < info_width:
                        player.rect.left = info_width
                    if player.rect.right > info_width + cenario_width:
                        player.rect.right = info_width + cenario_width
                    if player.rect.top < 0:
                        player.rect.top = 0
                    if player.rect.bottom > screen_height:
                        player.rect.bottom = screen_height

                players.draw(screen)
                players.update(aliens)
                aliens.draw(screen)
                aliens.update(players)

                self.desenhar_info_jogadores()

            case _:
                pass

    def mudar_janela(self, mouse: tuple) -> None:
        if self.janela_atual == JANELAS[1]:
            if (mouse[0] >= CAIXA("CAMPANHA")[0] and mouse[0] <= (CAIXA("CAMPANHA")[0] + CAIXA("CAMPANHA")[2])) and (mouse[1] >= CAIXA("CAMPANHA")[1] and mouse[1] <= (CAIXA("CAMPANHA")[1] + CAIXA("CAMPANHA")[3])):
                pygame.draw.rect(self.screen, CORES["Vermelho"], CAIXA("CAMPANHA"), 2)
                if pygame.mouse.get_pressed()[0]:
                    self.janela_atual = JANELAS[2]
            if (mouse[0] >= CAIXA("VERSUS")[0] and mouse[0] <= (CAIXA("VERSUS")[0] + CAIXA("VERSUS")[2])) and (mouse[1] >= CAIXA("VERSUS")[1] and mouse[1] <= (CAIXA("VERSUS")[1] + CAIXA("VERSUS")[3])):
                pygame.draw.rect(self.screen, CORES["Vermelho"], CAIXA("VERSUS"), 2)
            elif (mouse[0] >= CAIXA("SAIR")[0] and mouse[0] <= (CAIXA("SAIR")[0] + CAIXA("SAIR")[2])) and (mouse[1] >= CAIXA("SAIR")[1] and mouse[1] <= (CAIXA("SAIR")[1] + CAIXA("SAIR")[3])):
                pygame.draw.rect(self.screen, CORES["Vermelho"], CAIXA("SAIR"), 2)
                if pygame.mouse.get_pressed()[0]:
                    self.janela_atual = JANELAS[0]
        else:
            pass
