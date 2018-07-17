import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, hero, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.image = pygame.image.load("../pygame/images/bullet-3.gif").convert_alpha()
        self.hero = hero

        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = hero.rect.centerx-10, hero.rect.top

    def update(self):
        self.rect.centery -= self.settings.hero_bullet_speed_factor

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))

    # def restart(self):
    #     hero_X, hero_Y = self.hero.rect.centerx, self.hero.rect.centery
    #     self.rect.centerx = hero_X - self.image.get_width()/2
    #     self.rect.centery = hero_Y - self.image.get_height()/2
    #     self.active = True
