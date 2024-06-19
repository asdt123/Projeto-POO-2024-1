import pygame
import mysql.connector

# Inicializa o mysql e conecta com 
# um server criado previamente
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "ELE078TTTEC",
  database = "testdb"
)

# Faz a ponte python-mysql
# É onde os comandos são escritos
mycursor = mydb.cursor()

# Cria uma nova base de dados. Só é executado uma vez
mycursor.execute("DELETE DATABASE testdb")

# Mostra todas as bases de dados
mycursor.execute("SHOW DATABASES")

for db in mycursor:
  print(db)

# Criando uma tabela de dados para a base "rankdb"
#mycursor.execute("CREATE TABLE players (nome VARCHAR(3),pontos INTEGER(10))")

#sqlFormula = "INSERT INTO players (nome,pontos) VALUES (%s,%s)"

pygame.init()
relogio = pygame.time.Clock()

FPS = 30
pygame.display.set_caption("TÍTULO")
screen = pygame.display.set_mode((900,600))

fonte = pygame.font.Font(None,40)
text = ""

# press, tecla, caps
tecla_press = [False,pygame.K_POWER,False]

run = True
while run:

  relogio.tick(FPS)

  screen.fill((255,255,255))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_a:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_a
      if event.key == pygame.K_b:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_b
      if event.key == pygame.K_c:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_c
      if event.key == pygame.K_d:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_d
      if event.key == pygame.K_e:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_e
      if event.key == pygame.K_f:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_f
      if event.key == pygame.K_g:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_g
      if event.key == pygame.K_h:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_h
      if event.key == pygame.K_i:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_i
      if event.key == pygame.K_j:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_j
      if event.key == pygame.K_k:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_k
      if event.key == pygame.K_l:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_l
      if event.key == pygame.K_m:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_m
      if event.key == pygame.K_n:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_n
      if event.key == pygame.K_o:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_o
      if event.key == pygame.K_p:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_p
      if event.key == pygame.K_q:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_q
      if event.key == pygame.K_r:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_r
      if event.key == pygame.K_s:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_s
      if event.key == pygame.K_t:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_t
      if event.key == pygame.K_u:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_u
      if event.key == pygame.K_v:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_v    
      if event.key == pygame.K_w:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_w
      if event.key == pygame.K_x:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_x
      if event.key == pygame.K_y:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_y
      if event.key == pygame.K_z:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_z
      if event.key == pygame.K_BACKSPACE:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_BACKSPACE
      if event.key == pygame.K_SPACE:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_SPACE
      if event.key == pygame.K_0:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_0
      if event.key == pygame.K_1:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_1
      if event.key == pygame.K_2:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_2
      if event.key == pygame.K_3:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_3
      if event.key == pygame.K_4:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_4
      if event.key == pygame.K_5:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_5
      if event.key == pygame.K_6:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_6
      if event.key == pygame.K_7:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_7
      if event.key == pygame.K_8:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_8
      if event.key == pygame.K_9:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_9
      if event.key == pygame.K_RETURN:
        tecla_press[0] = True
        tecla_press[1] = pygame.K_RETURN


  if tecla_press[0] == True:
    
    if tecla_press[1] == pygame.K_BACKSPACE:
      text = text[:-1] 
      
    elif tecla_press[1] == pygame.K_RETURN:
      
      pass

    else:
      print(tecla_press[1])
      text += chr(tecla_press[1])

    tecla_press = [False,False,pygame.K_POWER]


  texto = fonte.render(text,True,(0,0,0))
  screen.blit(texto,(30,300))

  pygame.display.flip()

pygame.quit()