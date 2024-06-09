from configurações.Config import *
import pygame

class Drops(pygame.sprite.Sprite):
    def __init__(self, endereço_tiro, posição_alien, id_tiro ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.id_tiro = id_tiro
        self.index=0
        self.img_anim=[]
        for i in range(4):
            self.img_anim.append(pygame.transform.scale(pygame.image.load(endereço_tiro).subsurface((i*64,self.id_tiro*64),(64,64)).convert_alpha(), tamanho_municao()))
        self.image = self.img_anim[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = posição_alien
    
    def reposicionar(self, dimensões_antigas, dimensões_novas):
        self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
        self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])

    def update(self, player):
        self.rect.move_ip(0,screen.get_height()//150)

        self.index+=0.7
        if self.index > 3:
            self.index=0
        self.image = pygame.transform.scale(self.img_anim[int(self.index)], tamanho_municao())

        player_atingidos = pygame.sprite.spritecollide(self,player,0)
        for player in player_atingidos:
            self.kill()
            player.adicionar_munição(self.id_tiro)

        if self.rect.top>screen.get_height():
            self.kill()