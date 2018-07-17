import pygame 


class ScoreBoard:
    def __init__(self, settings):
        self.settings = settings
        self.current_score = 0
        self.font = pygame.font.Font(None, 20)
    
    def add_curent_score(self, num):
        self.current_score += self.settings.enemy_point*num
        if self.current_score % 1000 == 0:
            self.settings.speed_up()

    def reset(self):
        self.current_score = 0
        self.settings.update_high_score(self.highest_score)
    
    def blitme(self, screen):
        self.highest_score = max(self.current_score, self.settings.get_high_score())
        # self.settings.update_high_score(highest_score)
        current_score_text = self.font.render(
            "Score: %d" % self.current_score, 1, (0, 0, 0))
        high_score_text = self.font.render(
            "Highest: %d" % self.highest_score, 1, (0, 0, 0))
        screen.blit(current_score_text, (0, 0))
        screen.blit(high_score_text, (0, 20))
