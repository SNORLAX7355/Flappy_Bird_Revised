import pygame
import sys
import random
from time import sleep

from settings import Settings
from bird import Bird
from pipe import Pipe
from game_stats import GameStats
from points_hb import Points_hb
from coin import Coin
from scoreboard import Scoreboard
from start_button import Button

class FlappyBird:
    """Overall class to manage game"""

    def __init__(self):
        """Initialize game & create resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.stats = GameStats()

        self.screen = pygame.display.set_mode(self.settings.scrn_dimen)
        pygame.display.set_caption("Flappy Bird")
        self.sb = Scoreboard(self)

        self.bird = Bird(self)
        self.pipes = pygame.sprite.Group()
        self.timer = 60

        self.hbxs = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

    def run_game(self): 
        """Start main loop for game"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.bird.update()
                self._update_pipes()

                self.timer -= 1
                if self.timer <= 0:
                    self._create_pipe()
                    self.timer = 60

            self._update_screen()            

    def _check_events(self):
        """keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open("high_score.txt", "w") as f:
                    f.write(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    with open("high_score.txt", "w") as f:
                        f.write(str(self.stats.high_score))
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self.bird.a += 1
                    self.bird.jump = True
                    self.bird.fall = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def  _check_play_button(self, mouse_pos):
        """start and reset game if clicked"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.score = 0
            self.sb.prep_score()
            self.bird.reset_bird()
            self.pipes.empty()
            self.hbxs.empty()
            self.timer = 60
            pygame.mouse.set_visible(False)
            self.stats.game_active = True
            sleep(0.5)

    def _create_pipe(self):
        """create instances of pipes"""
        y = random.randint(30, 572)
        pipe = Pipe(self, y)
        hb = Points_hb(y)
        if random.randint(1, 5) == 1:
            coin = Coin(y)
            self.coins.add(coin)
        self.pipes.add(pipe)
        self.hbxs.add(hb)

    def _update_pipes(self):
        """update pipes and its position"""
        self.pipes.update()
        self.hbxs.update()
        self.coins.update()

        for hb in self.hbxs.copy():
            if pygame.sprite.collide_rect(self.bird, hb):
                self.stats.score += 1
                if pygame.sprite.spritecollideany(self.bird, self.coins):
                    self.stats.score += 2
                    self.coins.remove(pygame.sprite.spritecollideany(self.bird, self.coins))
                if self.stats.score > self.stats.high_score:
                    self.stats.high_score = self.stats.score

                self.sb.prep_score()
                self.sb.prep_high_score()
                self.hbxs.remove(hb)

        for pipe in self.pipes.copy():
            if self.bird.rect.colliderect(pipe.rect_t) or self.bird.rect.colliderect(pipe.rect_b):
                self._bird_hit()

            if pipe.x <= -60:
                self.pipes.remove(pipe)
                
    def _bird_hit(self):
        """Respond to bird collisions and reset game"""
        self._update_screen()
        self.stats.game_active = False
        pygame.mouse.set_visible(True) 
    
    def _update_screen(self):
        """updates images and flips to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.clock.tick(30)
        
        self.bird.blitme()
        self.coins.draw(self.screen)
        for pipe in self.pipes.sprites():
            pipe.draw()

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    #make game instance to run game
    fb = FlappyBird()
    fb.run_game()