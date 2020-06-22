#joho jump'run
#pop test
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
    draw_grid(win)
    for single_block in blocks:
        single_block.draw(win)
    for single_end_block in endblocks:
        single_end_block.draw(win)
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
                player.x += player.movement_velocity
                if player.iscolliding(blocks):
                    player.x -= player.movement_velocity
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= player.movement_velocity
                if player.iscolliding(blocks):
                    player.x += player.movement_velocity

        if not player.is_jump:
            if player.can_jump_again:
                if keys[pygame.K_SPACE]:
                    player.is_jump = True
                    player.can_jump_again = False
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

        redrawGameWindow()
        if player.player_is_on_endblock(endblocks):
            print("WIN")
            run = False
pygame.quit()

        # bad examples of shitty code
        # if not player.is_jump:
        #     if player.touches_ground:
        #         if not player.would_collide(blocks):
        #             if keys[pygame.K_SPACE]:
        #                 original_y = player.y
        #                 player.is_jump = True
        #                 player.touches_ground = False
        #                 can_check = False
        # else:
        #     if can_check:
        #         if player.on_ground(original_y):
        #                         player.is_jump = False 
        #                         player.jump_count = 10
        #                         pass
        #     if player.is_jump:
        #         if player.jump_count >= -10:
        #             neg = 1
        #             if player.jump_count < 0:
        #                 neg = -1
        #             jumpminus = (player.jump_count ** 2) * 0.5 * neg
        #             if not player.iscolliding(blocks):
        #                 player.y -= jumpminus
        #             else:
        #                 if jumpminus > 0:
        #                     player.y += jumpminus
        #                 else:
        #                     player.y -= jumpminus
        #                     can_check = True
        #             player.jump_count -= 1
        #         else:
        #             player.is_jump = False
        #             player.jump_count = 10

        # if not player.is_jump:
        #      player.fall(blocks)
