import pygame
from mongo import Mongo

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
    screenColor = [LIGHTBLUE, BLUE, PURPLE]
    screenColorDefault = LIGHTBLUE
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
    multiplier = 1
    enemyKilled = 0
    stage = 0
    highscore = Mongo.getHighscore(Mongo)
    topHighscore = Mongo.getTop(Mongo)

    def createScreen(self):
        self.screen.fill(self.screenColorDefault)
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
        text = font.render("Multiplier: x" + str(self.multiplier), 1, Variable.WHITE)
        self.screen.blit(text, (250, 10))
        text = font.render("Highscore: " + str(self.highscore), 1, Variable.WHITE)
        self.screen.blit(text, (810, 10))

    def gameOver(self):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, Variable.WHITE)
        Mongo.post(Mongo, self.score)
        self.screen.blit(text, (250, 300))
        pygame.display.flip()
        pygame.time.wait(3000)

    def stageIncrement(self):
        if self.enemyKilled == 5:
            self.stage += 1
            self.enemyKilled = 0
            self.multiplier += 0.25
            self.enemyspawn = self.enemyspawn/self.multiplier
            if self.stage < 3:
                self.screenColorDefault = self.screenColor[self.stage]

    def pauseScreen(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Pause / Highscore", 1, Variable.WHITE)
        i = 1
        for scores in self.topHighscore:
            fontscore = pygame.font.Font(None, 50)
            score = scores['score']
            textscore = fontscore.render(str(i) + ". " + str(score), 1, Variable.WHITE)
            self.screen.blit(textscore, (425, (200 + (i * 50))))
            i += 1
        screen = pygame.Surface((500,750))
        screen.set_alpha(128)
        screen.fill((255, 255, 255))
        self.screen.blit(screen, (225, 75))
        self.screen.blit(text, (250, 100))
        pygame.display.flip()

    def updateHighscore(self):
        if self.score > self.highscore:
            self.highscore = self.score



