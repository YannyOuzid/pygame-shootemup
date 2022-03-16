import pygame
import random
from variable import Variable
from bonus import Bonus


class Enemy(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.shoot_cooldown = 0
        self.spawn_cooldown = 0
        self.speed = random.randint(1, 7)

    def update(self, bullet, bonus_group):
        self.rect.y += self.speed
        if self.rect.x > 600:
            self.rect.x -= self.rect.x
        if self.rect.y > 825:
            self.kill()
        if pygame.sprite.spritecollide(self, bullet, True):
            luck = random.randint(1, 3)
            if luck == 3:
                for bonus in bonus_group:
                    self.createBonus(bonus, self.rect.x, self.rect.y)
            self.kill()
            Variable.score = Variable.score + 100

    def shootBulletEnemy(self, bullet):
        bullet.rect.x = self.rect.x + 10
        bullet.rect.y = self.rect.y
        bullet.update()

    def spawn(self):
        self.rect.x = random.randint(25, 575)
        self.rect.y = 50

    def spawnCoolDown(self):
        if self.spawn_cooldown > 0:
            self.spawn_cooldown -= 1

    def createBonus(self, bonus, x, y):
        bonus.rect.x = x
        bonus.rect.y = y
