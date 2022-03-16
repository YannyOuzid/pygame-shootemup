import pygame
from variable import Variable


class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        keys = pygame.key.get_pressed()
        if Variable.weapon == "normal":
            self.rect.y += -10
        else:
            self.rect.y += -7
            if keys[pygame.K_RIGHT]:
                self.rect.x += 7
            if keys[pygame.K_LEFT]:
                self.rect.x += -7
        if self.rect.y < 35 or self.rect.x > 775 or self.rect.x < 0:
            self.kill()
