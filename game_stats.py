class GameStats:
    """Track scores and other stats"""
    
    def __init__(self):
        """Initialize stats"""
        self.score = 0
        with open("high_score.txt") as f:
            hs = int(f.readline())
        self.high_score = hs
        self.game_active = False