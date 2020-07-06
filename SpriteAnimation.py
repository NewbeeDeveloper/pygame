import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Jumping")

# Cargamos listas y variables con la referencia a nuestros sprites
walkRight = [pygame.image.load('venv/Assets/R1.png'),
             pygame.image.load('venv/Assets/R2.png'),
             pygame.image.load('venv/Assets/R3.png'),
             pygame.image.load('venv/Assets/R4.png'),
             pygame.image.load('venv/Assets/R5.png'),
             pygame.image.load('venv/Assets/R6.png'),
             pygame.image.load('venv/Assets/R7.png'),
             pygame.image.load('venv/Assets/R8.png'),
             pygame.image.load('venv/Assets/R9.png')]

walkLeft = [pygame.image.load('venv/Assets/L1.png'),
            pygame.image.load('venv/Assets/L2.png'),
            pygame.image.load('venv/Assets/L3.png'),
            pygame.image.load('venv/Assets/L4.png'),
            pygame.image.load('venv/Assets/L5.png'),
            pygame.image.load('venv/Assets/L6.png'),
            pygame.image.load('venv/Assets/L7.png'),
            pygame.image.load('venv/Assets/L8.png'),
            pygame.image.load('venv/Assets/L9.png')]

char = pygame.image.load('venv/Assets/standing.png')

bg = pygame.image.load('venv/Assets/bg.jpg')

x = 50
y = 420
width = 5
height = 5
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

#Variables que nos idicarán la posición de nuestro monito
left = False
righ = False
walkCount = 0

#Función para dibujar los elementos de nuestro juego
def redraw():

    global walkCount

    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:  #If we are facing left
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still

    pygame.display.update()

run = True

while run:

    clock.tick(27)

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= 0:
        print("CHAR:",char.get_width(),"X:",x)
        x = x - vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        #Seteamos la posición de nuestro monito (derecha)
        left = False
        right = True
    else:
        #Si está parado lo mandamos alv y reseteamos el walkCount
        left = False
        right = False
        walkCount = 0

    if not (isJump):  #Mientras no salte
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 480 - char.get_height():
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
            # Si está saltando lo mandamos alv y reseteamos el walkCount
            left = False
            right = False
            walkCount = 0
    else:   #Esto es lo que pasa cuando salta
        if jumpCount >= -10:
            print(y, "=", y, "- (", jumpCount, " * ", abs(jumpCount), " )*0.5")
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1

        else:
            print("Y:", y)
            print("Jump Count:", jumpCount)

            jumpCount = 10
            isJump = False

    redraw()

pygame.quit()
