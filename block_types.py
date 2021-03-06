#block types

print("loaded block core module with code 1")

import pygame
dirtblock = pygame.image.load("media/dirtblock.png")
dirtblock_full = pygame.image.load("media/dirtblockfull.png")
endblockimage =  pygame.image.load("media/icon.png")
structureblockimage = pygame.image.load("media/structureblock.png")
winblockimage = pygame.image.load("media/winnercup.png")
woodblock = pygame.image.load("media/woodblock.png")
woodblock_full = pygame.image.load("media/woodblockfull.png")

class standardblock(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, win):
        win.blit(dirtblock, (self.x, self.y))

class standartblock_wood(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, win):
        win.blit(woodblock, (self.x, self.y))

class standardblock_filled(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, win):
        win.blit(dirtblock_full, (self.x, self.y))

class standartblock_wood_filled(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, win):
        win.blit(woodblock_full, (self.x, self.y))

class endblock(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, win):
        win.blit(endblockimage, (self.x, self.y))

class structureblock(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, win):
        win.blit(structureblockimage, (self.x, self.y))

class winblock(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    def draw(self, win):
        win.blit(winblockimage, (self.x, self.y))