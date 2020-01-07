import json

class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = 0

        #High Score should never be reset
        with open(self.settings.filename) as f:
            self.high_score = json.load(f)

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1