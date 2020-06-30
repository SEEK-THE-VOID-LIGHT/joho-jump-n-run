#everything for the levelbuild

print("loaded level core module with code 1")

import pygame
from player import *
from block_types import *
playercords = []
blocks = []
endblocks = []
structureblocks = []
winblocks = []

def draw_grid(win):
    for i in range(20):
        for j in range(16):
            pygame.draw.rect(win, (0,0,0), (i*50, j*50, 50, 50), 1)

def loadlevel(level, player):
    playercords.clear()
    blocks.clear()
    endblocks.clear()
    structureblocks.clear()
    winblocks.clear()

    block_x = 0
    block_y = 0
    for row in level:
        for char in row:
            if char == "o":
                blocks.append(standardblock(block_x, block_y, 50, 50, (0,255,0)))
            if char == "O":
                blocks.append(standardblock_filled(block_x, block_y, 50, 50, (0,255,0)))
            if char == "q":
                blocks.append(standartblock_wood(block_x,block_y))
            if char == "Q":
                structureblocks.append(standartblock_wood_filled(block_x,block_y))
            if char == "S":
                playercords.append(block_x)
                playercords.append(block_y-50)
            if char == "E":
                endblocks.append(endblock(block_x,block_y))
            if char == "x":
                structureblocks.append(structureblock(block_x, block_y))
            if char == "W":
                winblocks.append(winblock(block_x, block_y))
            block_x += 50
        block_x = 0
        block_y += 50
    player.x = playercords[0]
    player.y = playercords[1]