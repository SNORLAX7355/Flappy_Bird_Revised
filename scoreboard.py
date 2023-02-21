import pygame.font

class Scoreboard:
    """class to record scores"""

    def __init__(self, fb_game):
        """Initialize scorekeeping attributes"""
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = fb_game.stats

        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """Prep necessary elements for displaying the score, render images"""
        score_str = f"Score: {self.stats.score}"
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        #coordinates for score
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = f"High Score {self.stats.high_score}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)

        #coordinates for high score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.centerx + 20
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """display score in the game"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)