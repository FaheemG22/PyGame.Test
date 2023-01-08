class settings:
    screen_width = 1920
    screen_height = 1080

    outline = (255, 255, 255)
    background =(0, 0, 0)

    radius = 40
    vel = 8

    keys = "a"
    initial = True

class p1:
    x = 0 + settings.radius
    y = 0 + settings.radius
    coordinate = [x, y]

    colour = (255, 0, 0)
    string = False
class p2:
    x = settings.screen_width - settings.radius
    y = settings.screen_height - settings.radius
    coordinate = [x, y]

    colour = (0, 0, 255)
    string = False
