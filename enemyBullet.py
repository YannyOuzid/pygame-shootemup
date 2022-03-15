import pygame
from variable import Variable

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.y += 7
        if self.rect.y < 50:
            self.kill()
