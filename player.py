#playerclass
import pygame
walk_left = [pygame.image.load("media/player/left1_m.png"), pygame.image.load("media/player/left2_m.png"), pygame.image.load("media/player/left3_m.png")]
walk_right = [pygame.image.load("media/player/right1_m.png"), pygame.image.load("media/player/right2_m.png"), pygame.image.load("media/player/right3_m.png")]

class playerclass(object):
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.width = 50
        self.height = 100
        self.is_jump = False
        self.can_jump_again = True
        self.jump_count = 10
        self.movement_velocity = 6
        self.can_walk = True
        self.touches_ground = True
    
    def draw(self, win):
        pygame.draw.rect(win, (255,204,0), (self.x, self.y, self.width, self.height))
    
    def fall(self, blocks):
        self.y += 5
        self.can_jump_again = False
        while self.iscolliding(blocks):
            self.touches_ground = True
            self.y -= 5
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