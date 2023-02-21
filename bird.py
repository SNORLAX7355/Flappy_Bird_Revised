import  pygame

class Bird:
    """"class for managing bird"""

    def __init__(self, fb_game):
        """Initialize bird and its starting position"""
        self.screen = fb_game.screen
        self.screen_rect = fb_game.screen.get_rect()

        #load image of bird
        self.image = pygame.image.load('images\Bird.bmp')
        self.rect = self.image.get_rect()

        #starting positionn
        self.rect.x = 100
        self.rect.y = 250

        self.y = float(self.rect.y)
        
        self.fall = True
        self.f = 1
        self.jump = False
        self.a = 0
        self.t1, self.t2 = 8, 8 
        
    def update(self):
        """Update bird position"""
        
        if self.fall:
            Y = (1/2) * (self.f**2)
            self.y += Y
            self.f += 0.5
        
        if self.jump and self.a % 2 == 0:
            Y = (1/2) * (self.t1**2)
            self.y -= Y
            self.t1 -= 1
            self.t2 = 8
            if self.t1 <= 0:
                self.jump = False
                self.fall = True
                self.f = 1
                self.t1 = 8
                self.a = 0
        
        if self.jump and self.a % 2 == 1:
            Y = (1/2) * (self.t2**2)
            self.y -= Y
            self.t2 -= 1
            self.t1  = 8
            if self.t2 <= 0:
                self.jump = False
                self.fall = True
                self.f = 1
                self.t2 = 8
                self.a = 0

        if self.rect.bottom > self.screen_rect.bottom:
            self.y = 764
            self.fall = False
        
        if self.rect.top < self.screen_rect.top:
            self.y = 1
            self.jump = False
            self.fall = True
            self.f = 1
        
        self.rect.y = self.y

    def reset_bird(self):
        """reset bird starting position"""
        self.rect.y = 250
        self.y = self.rect.y
        self.jump = False
        self.fall = True
        self.f = 1
        self.a = 0
        self.t1, self.t2, = 8, 8

    def blitme(self):
        """Draw bird onto screen at currrent location"""
        self.screen.blit(self.image, self.rect)