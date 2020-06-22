#playerclass
print("loaded player module with code 1")
import pygame
walk_left = [pygame.image.load("media/player/left1.png"), pygame.image.load("media/player/left2.png"), pygame.image.load("media/player/left3.png")]
walk_right = [pygame.image.load("media/player/right1.png"), pygame.image.load("media/player/right2.png"), pygame.image.load("media/player/right3.png")]

class playerclass(object):
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.width = 32
        self.height = 64
        self.left = False
        self.right = True
        self.standing = False
        self.sprite_animation_count = 0
        self.is_jump = False
        self.can_jump_again = True
        self.jump_count = 10
        self.movement_velocity = 6
        self.can_walk = True
        self.touches_ground = True
    
    def draw(self, win):
        #pygame.draw.rect(win, (255,204,0), (self.x, self.y, self.width, self.height))

        if self.sprite_animation_count + 1 >= 22:
            self.sprite_animation_count = 0
        if not self.standing:
            if self.left:
                win.blit(walk_left[self.sprite_animation_count // 7], (self.x, self.y))
                self.sprite_animation_count += 1
            elif self.right:
                win.blit(walk_right[self.sprite_animation_count // 7], (self.x, self.y))
                self.sprite_animation_count += 1
        else:
            if self.right:
                win.blit(walk_right[0], (self.x, self.y))
            else:
                win.blit(walk_left[0], (self.x, self.y))
    
    def fall(self, blocks):
        self.y += 5
        self.can_jump_again = False
        while self.iscolliding(blocks):
            self.touches_ground = True
            self.y -= 1
            if not self.can_jump_again:
                self.can_jump_again = True
    
    def iscolliding(self, blocks):
        for block in blocks:
            if self.x + self.width > block.x and self.x < block.x + block.width:
                if self.y  + self.height > block.y and self.y < block.y + block.height:
                    return True
    
    def player_is_on_endblock(self, blocks):
        for block in blocks:
            if self.x + self.width > block.x and self.x < block.x + block.width:
                if self.y  + self.height > block.y and self.y < block.y + block.height:
                    return True