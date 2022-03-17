import pygame
from variable import Variable

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.width = 25
        self.height = 25
        self.image = pygame.Surface([25, 25])
        self.color = Variable.WHITE
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect()
        self.shoot_cooldown = 0
        self.speed = 5

    def controller(self, speed):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.moveLeft(speed)
        if keys[pygame.K_RIGHT]:
            self.moveRight(speed)
        if keys[pygame.K_UP]:
            self.moveUp(speed)
        if keys[pygame.K_DOWN]:
            self.moveDown(speed)

        if keys[pygame.K_LSHIFT]:
            Variable.weapon = "normal"
        else:
            Variable.weapon = "risk"

    def moveLeft(self, speed):
        self.rect.x -= speed
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, speed):
        self.rect.x += speed
        if self.rect.x > 775:
            self.rect.x = 775

    def moveUp(self, speed):
        self.rect.y -= speed
        if self.rect.y < 40:
            self.rect.y = 40

    def moveDown(self, speed):
        self.rect.y += speed
        if self.rect.y > 825:
            self.rect.y = 825

    def shootBullet(self, bullet):
        bullet.rect.x = self.rect.x + 10
        bullet.rect.y = self.rect.y
        bullet.update()

    def shootBomb(self, bomb):
        bomb.rect.x = self.rect.x - 250
        bomb.rect.y = self.rect.y
        Variable.bomb -= 1

    def update(self, enemy, bullet_enemy, bonus_group):
        if Variable.weapon == "risk":
            self.riskReward(bullet_enemy)
        if pygame.sprite.spritecollide(self, enemy, True) or pygame.sprite.spritecollide(self, bullet_enemy, True):
            Variable.lives = Variable.lives - 1
            Variable.enemyKilled = 0
            Variable.enemyspawn = 2500
            Variable.multiplier = 1
            Variable.stage = 0
            Variable.screenColorDefault = Variable.screenColor[0]
            for enemy in enemy:
                enemy.kill()
            for bullet in bullet_enemy:
                bullet.kill()
            if Variable.powerLevel > 1:
                Variable.powerLevel -= 1
            if Variable.speedLevel > 1:
                Variable.speedLevel -= 1
        if pygame.sprite.spritecollide(self, bonus_group, True):
            for bonus in bonus_group:
                bonus.create()

    def changeWeapon(self):
        if Variable.weapon == "normal":
            Variable.weapon = "risk"
            self.image = pygame.Surface([10, 10])
            pygame.draw.rect(self.image, self.color, [0, 0, 10, 10])
            self.speed = 3
        else:
            Variable.weapon = "normal"
            self.image = pygame.Surface([25, 25])
            pygame.draw.rect(self.image, self.color, [0, 0, 25, 25])
            self.speed = 5

    def riskReward(self, bullets):
        for bullet in bullets:
            dist = pygame.math.Vector2(self.rect.x, self.rect.y).distance_to((bullet.rect.x, bullet.rect.y))
            if dist < 50:
                Variable.score += 10



