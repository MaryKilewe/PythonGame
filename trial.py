import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither's tale")

swampGreen = (65, 104, 37) # hexColor -> #416825
red = (255, 0, 0)

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        # moving left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
        # if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #        lead_x_change = 0

        # moving up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lead_y_change = -10
            if event.key == pygame.K_DOWN:
                lead_y_change = 10
        # if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #        lead_y_change = 0

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(swampGreen)
    pygame.draw.rect(gameDisplay, red, [lead_x, lead_y, 100, 10])

    pygame.display.update()

    clock.tick(30) # 30 frames per second

pygame.quit()
quit()
