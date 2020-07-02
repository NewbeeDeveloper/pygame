import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jumping")

x = 50
y = 490
width = 5
height = 5
vel = 5

isJump = False
jumpCount = 10

run = True

while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel - width:
        x = x - vel

    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel

    if not (isJump):  #Mientras no salte
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
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

    win.fill((0, 0, 255))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
