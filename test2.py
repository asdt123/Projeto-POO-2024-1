import pygame

pygame.init()
relogio = pygame.time.Clock()

FPS = 30
pygame.display.set_caption("TÍTULO")
screen = pygame.display.set_mode((900,600))

ciclo = 0

def tamanho_letra(y_size)->int:
     return int(6+3*(y_size-8)//4)

textos = []
texto_imp = []
texto_rect = []
caixas = []
for i in range(2):
    for j in range(8):
      caixas.append((screen.get_width()//2-screen.get_width()//4+i*screen.get_width()//8,int(0.3*screen.get_height())+j*screen.get_height()//15,screen.get_width()//8,screen.get_height()//15))
      rect = pygame.Rect(caixas[len(caixas)-1])
      font = pygame.font.Font(None,tamanho_letra(screen.get_height()//15))
      textos.append("Oba")
      texto_imp.append(font.render(textos[len(textos)-1],True,(0,0,0)))
      texto_rect.append(texto_imp[len(texto_imp)-1].get_rect(center = rect.center))
      


run = True
while run:

  ciclo += 1
  if ciclo > 100:
      ciclo = 0

  relogio.tick(FPS)

  screen.fill((255,255,255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[0]),2)
  screen.blit(texto_imp[0],texto_rect[0])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[1]),2)
  screen.blit(texto_imp[1],texto_rect[1])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[2]),2)
  screen.blit(texto_imp[2],texto_rect[2])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[3]),2)
  screen.blit(texto_imp[3],texto_rect[3])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[4]),2)
  screen.blit(texto_imp[4],texto_rect[4])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[5]),2)
  screen.blit(texto_imp[5],texto_rect[5])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[6]),2)
  screen.blit(texto_imp[6],texto_rect[6])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[7]),2)
  screen.blit(texto_imp[7],texto_rect[7])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[8]),2)
  screen.blit(texto_imp[8],texto_rect[8])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[9]),2)
  screen.blit(texto_imp[9],texto_rect[9])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[10]),2)
  screen.blit(texto_imp[10],texto_rect[10])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[11]),2)
  screen.blit(texto_imp[11],texto_rect[11])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[12]),2)
  screen.blit(texto_imp[12],texto_rect[12])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[13]),2)
  screen.blit(texto_imp[13],texto_rect[13])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[14]),2)
  screen.blit(texto_imp[14],texto_rect[14])
  pygame.draw.rect(screen,(0,0,0),pygame.rect.Rect(caixas[15]),2)
  screen.blit(texto_imp[15],texto_rect[15])

  pygame.display.flip()

pygame.quit()