import pygame
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, settings, pos):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings 

        self.image = pygame.image.load(
            "../pygame/images/bullet-3.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos

        self.active = True

    def update(self):
        pass 

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))



class BulletHero(Bullet):
    def __init__(self, settings, pos):
        super().__init__(settings, pos)
        self.settings = settings
        self.image = pygame.image.load("../pygame/images/bullet-3.gif").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos

        self.active = True

    def update(self):
        self.rect.centery -= self.settings.hero_bullet_speed_factor
        if self.rect.centery <= 2:
            self.active = False

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))


class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, settings, pos):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        img_url = ["../pygame/images/bullet-1.gif",
                   "../pygame/images/bullet1.png", "../pygame/images/bullet-2.gif", "../pygame/images/bullet2.png"]
        current_img = random.choice(img_url)
        self.image = pygame.image.load(current_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos
        self.active = True

    def update(self):
        self.rect.centery += self.settings.enemy_bullet_speed_factor*10
        if self.rect.centery > self.settings.screen_size[1]:
            self.active = False

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))
