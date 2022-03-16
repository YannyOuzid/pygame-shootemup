import pygame
from variable import Variable


class Bomb(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    def update(self, enemyBullet, enemies):
        self.rect.y += -7
        if self.rect.y < 30:
            self.kill()
        if pygame.sprite.spritecollide(self, enemyBullet, True):
            for bullet in enemyBullet:
                bullet.kill()
                Variable.score += 5
        if pygame.sprite.spritecollide(self, enemies, True):
            for enemy in enemies:
                enemy.kill()
                Variable.score += 100


