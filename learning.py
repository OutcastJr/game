import pygame

pygame.init()

gamewindow = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("PyGame Tutorial")

gameActive = True
while gameActive:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameActive = False


    pygame.draw.rect(gamewindow, (255, 0, 0), (100, 100, 100, 100), 15)
    pygame.draw.rect(gamewindow, (255, 0, 0), (100, 300, 100, 100))

    surf = pygame.Surface((1000, 200))
    surf.fill((0, 255, 0))
    gamewindow.blit(surf, (0, 500))

    pygame.display.update()


pygame.quit()
quit()