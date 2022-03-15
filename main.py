import pygame
from player import Player
from enemy import Enemy
from enemyBullet import EnemyBullet
from bullet import Bullet
from variable import Variable
from bonus import Bonus

pygame.init()

pygame.display.set_caption("Project")

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
bonus_group = pygame.sprite.Group()

player = Player(Variable.WHITE, 25, 25)
player.rect.x = 250
player.rect.y = 750

pygame.display.flip()

player_group.add(player)

carryOn = True

clock = pygame.time.Clock()
start = pygame.time.get_ticks()

while carryOn:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.changeWeapon()

    if keys[pygame.K_LEFT]:
        player.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        player.moveRight(5)
    if keys[pygame.K_UP]:
        player.moveUp(5)
    if keys[pygame.K_DOWN]:
        player.moveDown(5)
    if keys[pygame.K_DOWN]:
        player.moveDown(5)

    if Variable.lives == 0:
        Variable.gameOver(Variable)
        carryOn = False

    enemy = Enemy(Variable.BLACK, 25, 25)

    now = pygame.time.get_ticks()
    if now - start > 2500:
        start = now
        enemy.spawn()
        enemy_group.add(enemy)

    bonus = Bonus(Variable.RED, 7, 7)
    playerBullet = Bullet(Variable.WHITE, 5, 5)
    enemyBullet = EnemyBullet(Variable.BLACK, 5, 5)

    enemy.shootBulletEnemy(enemyBullet)
    player.shootBullet(playerBullet)

    bonus_group.add(bonus)
    enemy_bullet_group.add(enemyBullet)
    player_bullet_group.add(playerBullet)

    enemy.cooldown()
    player.cooldown()

    player_group.update(enemy_group, enemy_bullet_group)
    enemy_group.update(player_bullet_group)
    player_bullet_group.update()
    enemy_bullet_group.update()
    bonus_group.update()


    Variable.createScreen(Variable)

    player_group.draw(Variable.screen)
    enemy_group.draw(Variable.screen)
    player_bullet_group.draw(Variable.screen)
    enemy_bullet_group.draw(Variable.screen)
    bonus_group.draw(Variable.screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
