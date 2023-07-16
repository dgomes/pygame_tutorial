import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

done = False
anchor_x, anchor_y = 30, 30

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        anchor_y -= 3
    if pressed[pygame.K_DOWN]:
        anchor_y += 3
    if pressed[pygame.K_LEFT]:
        anchor_x -= 3
    if pressed[pygame.K_RIGHT]:
        anchor_x += 3

    color = (0, 128, 255)
    pygame.draw.rect(screen, color, pygame.Rect(anchor_x, anchor_y, 60, 60))
    pygame.display.flip()
    screen.fill((0, 0, 0))
    clock.tick(60)
