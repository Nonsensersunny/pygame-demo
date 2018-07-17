import pygame


class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, settings, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.image = pygame.image.load(
            "../pygame/images/bullet-2.gif").convert_alpha()

        self.enemy = enemy
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = enemy.rect.centerx, enemy.rect.centery

    def update(self):
        self.rect.centery += self.settings.enemy_bullet_speed_factor

    def blitme(self, screen):
        screen.blit(self.image, (self.rect.centerx, self.rect.centery))

