import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
img = pygame.image.load('Android.png')
imgx = 10
imgy = 10
direction = 'right'

while True: # the main game loop

    DISPLAYSURF.fill(WHITE)
    
    if direction == 'right':
        imgx += 5
        if imgx == 280:
            direction = 'down'
    elif direction == 'down':
        imgy += 5
        if imgy == 220:
            direction = 'left'
    elif direction == 'left':
        imgx -= 5
        if imgx == 10:
            direction = 'up'
    elif direction == 'up':
        imgy -= 5
        if imgy == 10:
            direction = 'right'
            
    DISPLAYSURF.blit(img, (imgx, imgy))
    
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()

    fpsClock.tick(FPS)
