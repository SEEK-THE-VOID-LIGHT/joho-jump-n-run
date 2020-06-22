#joho jump'run
print("loaded main code with code 1")

import pygame
from player import *
from leveldata import *
from level_builder import *
window_width = 1000
window_height = 800

pygame.init()
win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("joho Jump'n'run")
icon = pygame.image.load("media/icon.png")
background = pygame.image.load("media/background.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
run = True

#redraw function
def redrawGameWindow():
    win.blit(background, (0,0 ))
    #draw_grid(win)
    for single_block in blocks:
        single_block.draw(win)
    for single_end_block in endblocks:
        single_end_block.draw(win)
    for single_structure_block in structureblocks:
        single_structure_block.draw(win)
    player.draw(win)

    pygame.display.update()

#main loop
if __name__ == "__main__":
    loadlevel(level1)
    print(playercords)
    player = playerclass(playercords[0], playercords[1])
    print(f"<< {len(blocks)} blocks were generated successfully >>")

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if player.can_walk:
            if keys[pygame.K_RIGHT] and player.x < window_width - player.width:
                player.right = True
                player.left = False
                player.standing = False
                player.x += player.movement_velocity
                while player.iscolliding(blocks):
                    player.x -= 1
            elif keys[pygame.K_LEFT] and player.x > 0:
                player.right = False
                player.left = True
                player.standing = False
                player.x -= player.movement_velocity
                while player.iscolliding(blocks):
                    player.x += 1
            else:
                player.standing = True
                player.sprite_animation_count = 0

        if not player.is_jump:
            if player.can_jump_again:
                if keys[pygame.K_SPACE]:
                    player.is_jump = True
                    player.can_jump_again = False
                    player.left = False
                    player.right = False
                    player.sprite_animation_count = 0
        else:
            if player.jump_count > 0:
                player.y -= (player.jump_count ** 2) * 0.5 * 1
                if player.iscolliding(blocks):
                    player.y += (player.jump_count ** 2) * 0.5 * 1
                player.jump_count -= 1
            else:
                player.is_jump = False
                player.jump_count = 10

        if not player.is_jump:
            player.fall(blocks)

        if player.player_is_on_endblock(endblocks):
            print("WIN")
            run = False

        redrawGameWindow()
pygame.quit()
