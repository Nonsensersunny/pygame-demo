import pygame
import random
from bullet_enemy import BulletEnemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.width_limit = settings.get_screen_size()[0]
        self.height_limit = settings.get_screen_size()[1]

        self.restart()
        img_url = ["../pygame/images/enemy0.png",
                   "../pygame/images/enemy1.png"]
        current_img = random.choice(img_url)
        self.image = pygame.image.load(
            current_img).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.centerx = self.rect.left
        self.rect.centery = self.rect.bottom

    def get_pos(self):
        return (self.x, self.y)

    def update(self):
        if self.y < self.height_limit:
            self.y += self.speed
            self.x += self.settings.enemy_speed_factor*self.move_left
            if self.x <= 0:
                self.x = 0
                self.move_left = 1
            if self.x >= self.width_limit - 30:
                self.x = self.width_limit - 30
                self.move_left = -1
        else:
            self.restart()

    def fire(self, bullets):
        if len(bullets) < self.settings.enemy_bullets_limit:
            bullet = BulletEnemy(self.settings, self.rect)
            bullets.add(bullet)

    def blitme(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def restart(self):
        self.x = random.randint(10, self.width_limit-10)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + self.settings.enemy_speed_factor
        self.move_left = random.choice([-1, 1])
