import os
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

done = False
anchor_x, anchor_y = 30, 30
uaveiro = pygame.image.load(os.path.join("images", "logo_ua.png"))
pygame.mixer.music.load(os.path.join("sounds", "loop.mp3"))
pygame.mixer.music.play(-1)
effect = pygame.mixer.Sound(os.path.join("sounds", "zap.wav"))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
           event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: anchor_y -= 3
    if pressed[pygame.K_DOWN]: anchor_y += 3
    if pressed[pygame.K_LEFT]: anchor_x -= 3
    if pressed[pygame.K_RIGHT]: anchor_x += 3    

    if anchor_y < 0:
        anchor_y = 0
        effect.play()
    if anchor_x < 0:
        anchor_x = 0
        effect.play()
    if anchor_y > 300-uaveiro.get_height():
        anchor_y = 300-uaveiro.get_height()
        effect.play()
    if anchor_x > 400-uaveiro.get_width():
        anchor_x = 400-uaveiro.get_width() 
        effect.play()

    screen.blit(uaveiro, (anchor_x, anchor_y))
    pygame.display.flip()
    screen.fill((255,255,255))
    clock.tick(60)
