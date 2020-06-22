#joho jump'run

print("loaded main code with code 1")

import pygame
import os
from player import *
from leveldata import *
from level_builder import *
window_width = 1000
window_height = 800

pygame.init()
jumpsound = pygame.mixer.Sound(os.path.join("media", "sounds", "jump.wav"))
fanfare = pygame.mixer.Sound(os.path.join("media","sounds","ending.wav"))
music = pygame.mixer.music.load(os.path.join("media", "sounds", "pumpit.mp3"))
win = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("joho Jump'n'run")
icon = pygame.image.load("media/icon.png")
background = pygame.image.load("media/background.png")
winbackground = pygame.image.load("media/ending.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
run = False
menu = True
ending = False


#redraw function
def redrawGameWindow():
    font = pygame.font.SysFont('comicsans', 60)
    
    win.blit(background, (0,0))
    #draw_grid(win)
    for single_block in blocks:
        single_block.draw(win)
    for single_end_block in endblocks:
        single_end_block.draw(win)
    for single_structure_block in structureblocks:
        single_structure_block.draw(win)
    for single_win_block in winblocks:
        single_win_block.draw(win)
    try:
        text = font.render(f"Time left: {seconds_left[levelid]}", 1, (0,0,0))
        win.blit(text, (30,30))
    except:
        pass
    player.draw(win)

    pygame.display.update()

#main function
if __name__ == "__main__":
    levelid = 0
    time_counter = 0
    reloadlevel = False
    player = playerclass(0, 0)
    loadlevel(level[levelid], player)
    original_time = seconds_left[levelid]
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    print(playercords)
    
    print(f"<< {len(blocks)} blocks were generated successfully >>")

# MENU
    while menu:
        clock.tick(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False
                ending = False
        
        menukeys = pygame.key.get_pressed()
        if menukeys[pygame.K_RETURN]:
            run = True
            menu = False
        
        win.fill((100,100,100))
        logo = pygame.image.load(os.path.join("media", "logo.png"))
        win.blit(logo, (window_width/2-logo.get_width()//2, 100))
        font = pygame.font.SysFont('comicsans', 50)
        text = font.render("Press ENTER to begin!", 1, (0,0,0))
        font2 = pygame.font.SysFont('comicsans', 35)
        text2 = font2.render("by Void Light", 1, (255,255,255))
        win.blit(text, (window_width/2-text.get_width()//2, 600))
        win.blit(text2, (window_width/2-text2.get_width()//2, 700))
        pygame.display.update()

# MAIN LOOP
    while run:

        clock.tick(60)

        if not levelid >= len(level):
            if reloadlevel:
                loadlevel(level[levelid], player)
                original_time = seconds_left[levelid]
                reloadlevel = False
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
                    jumpsound.play()
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

        if player.iscolliding(endblocks):
            print("NEXT")
            pygame.time.wait(300)
            reloadlevel = True
            levelid += 1
        
        if player.iscolliding(winblocks):
            run = False
            ending = True
            pygame.mixer.music.stop()
            pygame.time.wait(500)
            fanfare.play()

        time_counter += 1
        if time_counter >= 60:
            if levelid < len(seconds_left):
                seconds_left[levelid] -= 1
            time_counter = 0
        print(time_counter)
        if levelid < len(seconds_left):
            if seconds_left[levelid] <= 0:
                seconds_left[levelid] = original_time
                loadlevel(level[levelid], player)

        redrawGameWindow()
    
    while ending:
        done = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = False
        
        win.blit(winbackground, (0,0))
        pygame.display.update()


pygame.quit()
