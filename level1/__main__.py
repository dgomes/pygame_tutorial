import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
           event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    color = (0, 128, 255) 
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
