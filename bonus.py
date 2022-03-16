import pygame
import random
from variable import Variable

class Bonus(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self):
        self.rect.y += 5
        if self.rect.y < 50:
            self.kill()

    def create(self):
        case = random.randint(1, 3)
        if case == 1:
            Variable.lives += 1
        if case == 2:
            if Variable.powerLevel < 3:
                Variable.powerLevel += 1
            else:
                Variable.lives += 1
        if case == 3:
            if Variable.speedLevel < 3:
                Variable.speedLevel += 1
            else:
                Variable.lives += 1