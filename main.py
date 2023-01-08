from movement import *
import pygame

def runtime():
    try:
        pygame.init()
        win = pygame.display.set_mode((settings.screen_width, settings.screen_height))
        pygame.display.set_caption("game")

        initial = True

        while True:
            pygame.time.delay(3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            settings.keys = pygame.key.get_pressed()

            controls()

            if initial:
                Thread(target=strings1).start()
                Thread(target=strings2).start()
                initial = False

            win.fill(settings.background)
            if p1.string:
                pygame.draw.circle(win, settings.outline, p1.coordinate, settings.radius+4)
            if p2.string:
                pygame.draw.circle(win, settings.outline, p2.coordinate, settings.radius+4)
            if p1.string and p2.string:
                pygame.draw.line(win, settings.outline, p1.coordinate, p2.coordinate)

            pygame.draw.circle(win, p1.colour, p1.coordinate, settings.radius)
            pygame.draw.circle(win, p2.colour, p2.coordinate, settings.radius)
            pygame.display.update()
    except:
        print("Game Quit")

Thread(target=runtime).start()