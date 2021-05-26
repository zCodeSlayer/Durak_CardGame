import pygame

class TCard(object):
    power = False

    def __init__(self, name, status, xpos, ypos, picture, x, y, w, h):
        self.name = name
        self.status = status
        self.x = xpos
        self.y = ypos
        self.picture = pygame.image.load(picture)
        self.picture = self.picture.subsurface(x, y, w, h)
    
    def render(self, window):
        window.blit(self.picture, (self.x, self.y))
    @classmethod 
    def powerup(cls):
        cls.power = True

class TCcherv(TCard):
    def __init__(self, status, xpos, ypos, picture, x, y, w, h):
        TCard.__init__(self, 'Черви', status, xpos, ypos, picture, x, y, w, h)


class TCbubi(TCard):
    def __init__(self, status, xpos, ypos, picture, x, y, w, h):
        TCard.__init__(self, 'Буби', status, xpos, ypos, picture, x, y, w, h)


class TCkresti(TCard):
    def __init__(self, status, xpos, ypos, picture, x, y, w, h):
        TCard.__init__(self, 'Крести', status, xpos, ypos, picture, x, y, w, h)


class TCpiki(TCard):
    def __init__(self, status, xpos, ypos, picture, x, y, w, h):
        TCard.__init__(self, 'Пики', status, xpos, ypos, picture, x, y, w, h)



