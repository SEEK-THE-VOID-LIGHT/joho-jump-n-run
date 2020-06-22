import pygame
dirtblock = pygame.image.load("media/dirtblock.png")
endblockimage =  pygame.image.load("media/icon.png")

class standardblock(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, win):
        win.blit(dirtblock, (self.x, self.y))

class endblock(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (0,255,0)
    def draw(self, win):
        win.blit(endblockimage, (self.x, self.y))