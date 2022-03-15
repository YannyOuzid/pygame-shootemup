import pygame


class Variable():
    score = 0
    lives = 3
    LIGHTBLUE = (0, 176, 240)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (243, 14, 14)
    size = (600, 850)
    screen = pygame.display.set_mode(size)
    weapon = "normal"

    def createScreen(self):
        self.screen.fill(Variable.LIGHTBLUE)
        pygame.draw.line(self.screen, Variable.WHITE, [0, 38], [800, 38], 2)
        font = pygame.font.Font(None, 34)
        text = font.render("Score: " + str(self.score), 1, Variable.WHITE)
        self.screen.blit(text, (20, 10))
        text = font.render("Lives: " + str(self.lives), 1, Variable.WHITE)
        self.screen.blit(text, (500, 10))
        text = font.render("Weapon: " + str(self.weapon), 1, Variable.WHITE)
        self.screen.blit(text, (0, 820))

    def gameOver(self):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, Variable.WHITE)
        self.screen.blit(text, (250, 300))
        pygame.display.flip()
        pygame.time.wait(3000)



