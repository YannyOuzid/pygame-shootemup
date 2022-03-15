import pygame
import random

class Bonus(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.y += -7
        if self.rect.y < 50:
            self.kill()

    def create(self, x, y):
        case = random.randint(1, 4)
        self.rect.x = x
        self.rect.y = y

        if case == 1:
            print('live')
        if case == 2:
            print('power')
        if case == 3:
            print('speed')
        if case == 4:
            print('nothing')





