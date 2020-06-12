import pygame

from pygame.locals import *
pygame.init()

#Ajustamos los FPS y el reloj interno  para controlar los Frames

FPS      = 90 # Frames Per Second
fpsClock = pygame.time.Clock()

#Creamos la ventana principal
DISPLAYSURF = pygame.display.set_mode((500,500))
pygame.display.set_caption("Key Press")

#Variables con cordenadas
x      = 50
y      = 50
width  = 10
height = 10
vel    = 5

#Inicio del ciclo principal del juego
while True:

    #Obtenemos que tecla presionamos
    keys = pygame.key.get_pressed()

    #Lógica para manejo de teclas
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
        
    #Color de la pantalla
    DISPLAYSURF.fill((0,0,255))  # Fills the screen with black

    #Dibulamos el rectangulo y lo colocamos en las cordenadas correspondientes
    pygame.draw.rect(DISPLAYSURF, (0,255,0), (x, y, width, height)) 

    #Manejador de eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Actualizamos la pantalla
    pygame.display.update() 

    fpsClock.tick(FPS)
    
