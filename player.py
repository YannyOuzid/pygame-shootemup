import pygame
from variable import Variable
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.shoot_cooldown = 0

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 575:
            self.rect.x = 575

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 40:
            self.rect.y = 40

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 825:
            self.rect.y = 825

    def shootBullet(self, bullet):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 50
            bullet.rect.x = self.rect.x + 10
            bullet.rect.y = self.rect.y
            bullet.update()

    def cooldown(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def update(self, enemy, bullet_enemy):
        if pygame.sprite.spritecollide(self, enemy, True) or pygame.sprite.spritecollide(self, bullet_enemy, True):
            Variable.lives = Variable.lives - 1

    def changeWeapon(self):
        if Variable.weapon == "normal":
            Variable.weapon = "side"
        else:
            Variable.weapon = "normal"

