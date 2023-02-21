import pygame
from pygame.sprite import Sprite

class Points_hb(Sprite):
    """Class for hitbox in between pipes"""

    def __init__(self, y):
        """Initialize hitbox and its starting position"""
        super().__init__()
        self.hb = pygame.Surface((2, 210))
        self.rect = self.hb.get_rect()

        self.rect.y = y
        self.rect.x = 569

    def update(self):
        self.rect.x -= 6
        