#everything for the levelbuild
print("loaded level core module with code 1")

import pygame
from player import *
from block_types import *
playercords = []
blocks = []
endblocks = []

def draw_grid(win):
    for i in range(20):
        for j in range(16):
            pygame.draw.rect(win, (0,0,0), (i*50, j*50, 50, 50), 1)

def drawui(win):
    #setup
    font = pygame.font.SysFont('comicsans', 60)

def loadlevel(level):
    global playercords
    block_x = 0
    block_y = 0
    for row in level:
        for char in row:
            if char == "o":
                blocks.append(standardblock(block_x, block_y, 50, 50, (0,255,0)))
            if char == "S":
                playercords.append(block_x)
                playercords.append(block_y-50)
            if char == "E":
                endblocks.append(endblock(block_x,block_y))
            block_x += 50
        block_x = 0
        block_y += 50