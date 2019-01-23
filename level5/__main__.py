import os
import pygame
import random


class UA(pygame.sprite.Sprite):  
    def __init__(self):      
        pygame.sprite.Sprite.__init__(self)     
        self.image_s = pygame.image.load(os.path.join("images", "logo_ua.png"))
        self.rect = self.image_s.get_rect()

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 2 
        if key[pygame.K_DOWN]:
            self.rect.y += dist 
        elif key[pygame.K_UP]: 
            self.rect.y -= dist
        if key[pygame.K_RIGHT]: 
            self.rect.x += dist 
        elif key[pygame.K_LEFT]:
            self.rect.x -= dist 

    def draw(self, surface):
        surface.blit(self.image_s, (self.rect.x, self.rect.y))

class GGJ(pygame.sprite.Sprite): 
    def __init__(self, x=640, y=0,):
        pygame.sprite.Sprite.__init__(self)     
        self.image_s = pygame.image.load(os.path.join("images", "logo_ggj.png"))
        self.rect = self.image_s.get_rect()
        self.rect.centerx,self.rect.centery = x, y
        self.dist = 10 

    def roll(self):
        self.rect.centerx -= self.dist

    def draw(self, surface):
        surface.blit(self.image_s, (self.rect.x, self.rect.y))

    def checkCollision(self, obj):
        col = pygame.sprite.collide_rect(self, obj)
        if col:
            print("Collide")

pygame.init()
screen = pygame.display.set_mode((640, 200))

ua = UA() 
ggj = GGJ(0, 10)
clock = pygame.time.Clock()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False

        if ggj.rect.x < 0:
            # Respawn
            y = random.randint(10, 190)
            ggj = GGJ(640, y)

    ggj.checkCollision(ua)
    ua.handle_keys()     
    ggj.roll()

    screen.fill((255,255,255))
    ua.draw(screen)
    ggj.draw(screen)
    pygame.display.update() 

    clock.tick(40)
