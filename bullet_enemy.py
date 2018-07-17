import pygame
import random


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

    def update(self):
        self.rect.centery += self.settings.enemy_bullet_speed_factor*5

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))

