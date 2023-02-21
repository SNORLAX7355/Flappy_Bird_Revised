import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    """Class to represent bonus coins"""

    def __init__(self, y):
        """Initialize the coin and set position"""
        super().__init__()

        #load coin images and get rect
        self.image = pygame.image.load('images\coin.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 546
        self.rect.y = y

    def update(self):
        """Move coin left across the screen"""
        self.rect.x -= 6