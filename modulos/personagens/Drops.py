from configurações.Config import *
import pygame

class Drops(pygame.sprite.Sprite):
    def __init__(self, posição_alien : tuple[int,int], id_drop : int ) -> None:
        pygame.sprite.Sprite.__init__(self)
        #id para determinar o drop, sendo 1-x munição e 100 vida
        self.id_drop = id_drop
        self.index=0
        self.img_anim=[]
        if self.id_drop!=100:
            for i in range(4):
                self.img_anim.append(pygame.transform.scale(pygame.image.load(endereço_tiro).subsurface((i*64,self.id_drop*64),(64,64)).convert_alpha(), self.tamanho_drop()))
        else:
            for i in range(4):
                self.img_anim.append(pygame.transform.scale(pygame.image.load(endereço_tiro).subsurface((i*64,len(VIDA_ALIEN)*64),(64,64)).convert_alpha(), self.tamanho_drop()))
        self.image = self.img_anim[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = posição_alien
    
    def reposicionar(self, dimensões_antigas, dimensões_novas) ->None:
        self.rect.x = round(self.rect.x / dimensões_antigas[0] * dimensões_novas[0])
        self.rect.y = round(self.rect.y / dimensões_antigas[1] * dimensões_novas[1])

    def tamanho_drop(self)->tuple[int,int]:
        return (screen.get_height()//27,screen.get_height()//27)

    def update(self, player)->None:
        #movimenta o longo da tela para não ficar disponivel eternamente
        self.rect.move_ip(0,screen.get_height()//150)

        #animação
        self.index+=0.7
        if self.index > 3:
            self.index=0
        self.image = pygame.transform.scale(self.img_anim[int(self.index)], self.tamanho_drop())

        #verifica colisão com player ou com fim da tela
        player_atingidos = pygame.sprite.spritecollide(self,player,0)
        for player in player_atingidos:
            self.kill()
            player.receber_drop(self.id_drop)

        if self.rect.top>screen.get_height():
            self.kill()