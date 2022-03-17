import pygame
from player import Player
from enemy import Enemy
from enemyBullet import EnemyBullet
from bullet import Bullet
from variable import Variable
from bonus import Bonus
from bomb import Bomb

pygame.init()

pygame.display.set_caption("Project")
pause = False

player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
bonus_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

player = Player()
player.rect.x = 250
player.rect.y = 750

pygame.display.flip()

player_group.add(player)

carryOn = True

clock = pygame.time.Clock()
startEnemy = pygame.time.get_ticks()
startShoot = pygame.time.get_ticks()

while carryOn:
    keys = pygame.key.get_pressed()
    bomb = Bomb(Variable.WHITE, 550, 5)
    Variable.stageIncrement(Variable)
    Variable.updateHighscore(Variable)
    player.controller(player.speed)
    player.changeWeapon()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Variable.bomb > 0:
                player.shootBomb(bomb)
            if event.key == pygame.K_p:
                while True:
                    event = pygame.event.wait()
                    Variable.pauseScreen(Variable)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        break

    if Variable.lives == 0:
        Variable.gameOver(Variable)
        carryOn = False

    enemy = Enemy(Variable.BLACK, 25, 25)
    bonus = Bonus(Variable.bonusColor, 14, 14)
    playerBullet = Bullet(Variable.WHITE, (5 ** Variable.powerLevel), 25)
    enemyBullet = EnemyBullet(Variable.BLACK, 5, 5)

    now = pygame.time.get_ticks()
    if now - startEnemy > Variable.enemyspawn:
        startEnemy = now
        enemy.spawn()
        enemy_group.add(enemy)
        enemy.shootBulletEnemy(enemyBullet)
        enemy_bullet_group.add(enemyBullet)

    if now - startShoot > (Variable.shootCooldown / Variable.speedLevel):
        startShoot = now
        player.shootBullet(playerBullet)
        player_bullet_group.add(playerBullet)

    bonus_group.add(bonus)
    bomb_group.add(bomb)

    player_group.update(enemy_group, enemy_bullet_group, bonus_group)
    enemy_group.update(player_bullet_group, bonus_group)
    player_bullet_group.update()
    enemy_bullet_group.update()
    bonus_group.update()
    bomb_group.update(enemy_bullet_group, enemy_group)

    Variable.createScreen(Variable)

    player_group.draw(Variable.screen)
    enemy_group.draw(Variable.screen)
    player_bullet_group.draw(Variable.screen)
    enemy_bullet_group.draw(Variable.screen)
    bonus_group.draw(Variable.screen)
    bomb_group.draw(Variable.screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
