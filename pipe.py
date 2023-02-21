import pygame
from pygame.sprite import Sprite

class Pipe(Sprite):
    """class for initializing pipes"""

    def __init__(self, fb_game, y):
        """Initialize pipe and its starting position"""
        super().__init__()
        self.screen = fb_game.screen

        #draw rects
        self.top = pygame.Surface((60, 700))
        self.top.fill((4, 173, 0))
        self.rect_t = self.top.get_rect()
        self.rect_t.y = y - 700

        self.bottom = pygame.Surface((60, 700))
        self.bottom.fill((4, 173, 0))
        self.rect_b = self.bottom.get_rect()
        self.rect_b.y = y + 210

        self.x = 540
        self.rect_t.x = self.x
        self.rect_b.x = self.x

    def update(self):
        """update pipe movement"""
        self.x -= 6

        #move the rects position
        self.rect_t.x = self.x
        self.rect_b.x = self.x

    def draw(self):
        """draw pipes onto the screen"""
        self.screen.blit(self.top, (self.x, self.rect_t.y))
        self.screen.blit(self.bottom, (self.x, self.rect_b.y))