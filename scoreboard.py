import pygame.font

class ScoreBoard():

    def __init__(self, screen, setting, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.setting = setting
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()


    def prep_score(self):
        score_str = 'Score:' + str(int(self.stats.score))
        self.score_img = self.font.render(score_str, True, self.text_color, self.setting.bg_color)
        self.score_img_rect = self.score_img.get_rect()
        self.score_img_rect.right = self.screen_rect.right - 20
        self.score_img_rect.top = 20


    def prep_high_score(self):
        high_score_str = 'Highest:' + str(self.setting.get_high_score())
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.setting.bg_color)
        self.high_score_img_rect = self.high_score_img.get_rect()
        self.high_score_img_rect.right = self.screen_rect.right - 20
        self.high_score_img_rect.top = 50


    def prep_level(self):
        level_str = 'Level:' + str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_color, self.setting.bg_color)
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.centerx =self.screen_rect.centerx
        self.level_img_rect.top = 20


    def draw_score(self):
        self.screen.blit(self.score_img, self.score_img_rect)


    def draw_high_score(self):
        self.screen.blit(self.high_score_img, self.high_score_img_rect)


    def draw_level(self):
        self.screen.blit(self.level_img, self.level_img_rect)