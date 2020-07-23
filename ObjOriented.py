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

"""
x = 50
y = 420
width = 5
height = 5
vel = 5
isJump = False
jumpCount = 10
left = False
righ = False
walkCount = 0

"""
clock = pygame.time.Clock()

#Variables que nos idicarán la posición de nuestro monito en clases

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:  # If we are facing left
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))  # If the character is standing still


#Función para dibujar los elementos de nuestro juego
def redraw():
    win.blit(bg, (0, 0))
    man.draw(win)
    pygame.display.update()

man = player(200, 410, 64,64)
run = True

while run:

    clock.tick(27)
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            man.run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x >= 0:
        man.x = man.x - man.vel
        man.left = True
        man.right = False

    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:
        man.x += man.vel
        #Seteamos la posición de nuestro monito (derecha)
        man.left = False
        man.right = True
    else:
        #Si está parado lo mandamos alv y reseteamos el walkCount
        man.left = False
        man.right = False
        man.walkCount = 0

    if not (man.isJump):  #Mientras no salte
        if keys[pygame.K_UP] and man.y > man.vel:
            man.y -= man.vel

        if keys[pygame.K_DOWN] and man.y < 480 - char.get_height():
            man.y += man.vel

        if keys[pygame.K_SPACE]:
            man.isJump = True
            # Si está saltando lo mandamos alv y reseteamos el walkCount
            man.left = False
            man.right = False
            man.walkCount = 0
    else:   #Esto es lo que pasa cuando salta
        if man.jumpCount >= -10:
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1

        else:
            man.jumpCount = 10
            man.isJump = False

    redraw()

pygame.quit()
