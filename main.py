import pygame

# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
x = 0
y = 0
z = screen.get_height()
f = 0
k = 0
pulo = False
relogio = pygame.time.Clock()
frames = 30
sr=100
while running:
    relogio.tick(frames)
    pygame.key.set_repeat(10)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False;
        
        if event.type == KEYDOWN:
            if event.key == K_UP and z==screen.get_height():
                pulo = True
            if event.key == K_DOWN:
                pygame.time.wait(300)
            if event.key == K_LEFT and f>(screen.get_width()//2*-1)+sr:
                f=f-10
            elif event.key == K_RIGHT and f<(screen.get_width()//2):
                f=f+10
            if event.key == K_a and x>1:
                x=x-1
            elif event.key == K_d and x<254:
                x=x+1
            if event.key == K_s and y>1:
                y=y-1
            elif event.key == K_w and y<254:
                y=y+1  
            if event.key == K_f and k>0:
                k=k-1
            elif event.key == K_e and k<254:
                k=k+1 
    if pulo:
        if z>screen.get_height()//2:
            z=z-int(10*60/frames)
        else:
            pulo = False
    else:
        if z<screen.get_height():
            z=z+int(10*60/frames)
    if z>screen.get_height(): 
        z=screen.get_height()

    print(z)
    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    retangulo = pygame.draw.rect(screen, (x,y,k), (screen.get_width()//2+f-sr,z-sr,sr,sr))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()