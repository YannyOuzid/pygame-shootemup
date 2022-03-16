import pygame


class Variable():
    score = 0
    lives = 3
    LIGHTBLUE = (0, 176, 240)
    BLUE = (5, 0, 240)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (243, 14, 14)
    PURPLE = (178, 0, 240)
    size = (1000, 850)
    screen = pygame.display.set_mode(size)
    screenColor = LIGHTBLUE
    weapon = "normal"
    power = 1
    speed = 1
    player_size = 25
    player_height = 25
    shootCooldown = 1500
    enemyspawn = 2500
    bonusColor = (243, 14, 14)
    powerLevel = 1
    speedLevel = 1
    bomb = 5
    multiplicator = 1
    enemyKilled = 0

    def createScreen(self):
        self.screen.fill(self.screenColor)
        pygame.draw.line(self.screen, Variable.WHITE, [0, 38], [800, 38], 2)
        pygame.draw.line(self.screen, Variable.WHITE, [800, 0], [800, 850], 2)
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(self.score), 1, Variable.WHITE)
        self.screen.blit(text, (20, 10))
        text = font.render("Lives: " + str(self.lives), 1, Variable.WHITE)
        self.screen.blit(text, (500, 10))
        text = font.render("Weapon: " + str(self.weapon), 1, Variable.WHITE)
        self.screen.blit(text, (810, 150))
        text = font.render("Power: " + str(self.powerLevel), 1, Variable.WHITE)
        self.screen.blit(text, (810, 180))
        text = font.render("Speed: " + str(self.speedLevel), 1, Variable.WHITE)
        self.screen.blit(text, (810, 210))
        text = font.render("Bomb: " + str(self.bomb), 1, Variable.WHITE)
        self.screen.blit(text, (810, 240))
        text = font.render("Multiplicator: " + str(self.multiplicator), 1, Variable.WHITE)
        self.screen.blit(text, (250, 10))

    def gameOver(self):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, Variable.WHITE)
        self.screen.blit(text, (250, 300))
        pygame.display.flip()
        pygame.time.wait(3000)

    def stageGenerator(self):
        if self.score > 500:
            self.enemyspawn = 1500
            self.screenColor = self.BLUE
        if self.score > 1000:
            self.enemyspawn = 1000
            self.screenColor = self.PURPLE
        if self.score > 1500:
            self.enemyspawn = 500

    def multiplicatorIncrement(self):
        if self.enemyKilled == 5:
            self.enemyKilled = 0
            self.multiplicator += 0.5



