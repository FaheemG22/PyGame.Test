from movement import *
import pygame
from threading import Thread

class game:
    def __init__(self):
        try:
            pygame.init()
            self.win = pygame.display.set_mode((settings.screen_width, settings.screen_height))
            pygame.display.set_caption("game")

            while True:
                pygame.time.delay(3)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                settings.keys = pygame.key.get_pressed()
                controls()

                if settings.initial:
                    Thread(target=strings1).start()
                    Thread(target=strings2).start()
                    settings.initial = False
                self.display()

        except:
            print("Game Quit")

    def display(self):
        if p1.string:
            pygame.draw.circle(self.win, settings.outline, p1.coordinate, settings.radius + 4)
        if p2.string:
            pygame.draw.circle(self.win, settings.outline, p2.coordinate, settings.radius + 4)
        if p1.string and p2.string:
            pygame.draw.line(self.win, settings.outline, p1.coordinate, p2.coordinate)

        pygame.draw.circle(self.win, p1.colour, p1.coordinate, settings.radius)
        pygame.draw.circle(self.win, p2.colour, p2.coordinate, settings.radius)
        pygame.display.update()
        self.win.fill(settings.background)
game()
