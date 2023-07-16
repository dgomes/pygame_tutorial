import os
import pygame
import random
import math


class UA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_s = pygame.image.load(os.path.join("images", "logo_ua.png"))
        self.rect = self.image_s.get_rect()
        self.rect.centerx, self.rect.centery = 300, 100

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


class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_s = pygame.image.load(os.path.join("images", "cannon.png"))
        self.rect = self.image_s.get_rect()
        self.rect.x, self.rect.y = 0, 448

    def draw(self, surface):
        surface.blit(self.image_s, (self.rect.x, self.rect.y))


class Cannonball(pygame.sprite.Sprite):
    def __init__(self, x=50, y=448, angle=45, speed=40):
        pygame.sprite.Sprite.__init__(self)
        self.image_s = pygame.image.load(os.path.join("images", "cannonball.png"))
        self.rect = self.image_s.get_rect()
        self.rect.centerx, self.rect.centery = x, y
        self.initial_x, self.initial_y = x, y
        self.speed = speed
        self.gravity = -1
        self.angle = angle
        print(f"Angle: {self.angle} \t Speed: {self.speed} \t Gravity: {self.gravity}")

    def position(self, t):
        self.rect.centerx = (
            self.initial_x + self.speed * math.cos(math.radians(self.angle)) * t
        )
        self.rect.centery = (
            self.initial_y
            - self.speed * math.sin(math.radians(self.angle)) * t
            - 0.5 * self.gravity * (t**2)
        )

    def draw(self, surface):
        surface.blit(self.image_s, (self.rect.x, self.rect.y))

    def checkCollision(self, obj):
        col = pygame.sprite.collide_rect(self, obj)
        if col:
            print("Collide")


pygame.init()
screen = pygame.display.set_mode((640, 480))

ua = UA()
cannon = Cannon()
clock = pygame.time.Clock()


running = True
cannonball = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            running = False

    if (
        not cannonball
        or cannonball.rect.x > screen.get_width()
        or cannonball.rect.y > screen.get_height()
    ):
        # Respawn
        cannonball = Cannonball(
            angle=random.randrange(0, 90), speed=random.randrange(10, 50)
        )
        t = 0

    ua.handle_keys()
    cannonball.position(t)
    cannonball.checkCollision(ua)

    screen.fill((255, 255, 255))
    ua.draw(screen)
    cannon.draw(screen)
    cannonball.draw(screen)
    pygame.display.update()

    clock.tick(100)
    t += 0.1
