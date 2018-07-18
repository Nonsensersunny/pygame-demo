import pygame
import random
from settings import Settings
from bullet import BulletHero, BulletEnemy


class Hero:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.image = pygame.image.load(
            "../pygame/images/hero.gif").convert_alpha()
        self.rect = self.image.get_rect()

        self.restart()

        self.settings = settings
        self.screen_width, self.screen_height = settings.get_screen_size()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move_by_mouse(self):
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_X
        self.rect.bottom = mouse_Y + self.image.get_height()/2

    def move_by_keyboard(self):
        if self.moving_right:
            if self.rect.centerx > self.screen_width:
                self.rect.centerx = self.screen_width
            else:
                self.rect.centerx += self.settings.ship_speed_factor*10
        if self.moving_left:
            if self.rect.centerx < 0:
                self.rect.centerx = 0
            else:
                self.rect.centerx -= self.settings.ship_speed_factor
        if self.moving_up:
            if self.rect.centery < 0:
                self.rect.centery = 0
            else:
                self.rect.centery -= self.settings.ship_speed_factor
        if self.moving_down:
            if self.rect.centery > self.screen_height:
                self.rect.centery = self.screen_height
            else:
                self.rect.centery += self.settings.ship_speed_factor*10
    
    def fire(self, bullets):
        if len(bullets) < self.settings.hero_bullets_limit:
            bullets.add(BulletHero(self.settings, (self.rect.centerx-10, self.rect.top)))

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def restart(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = self.rect.centerx
        self.y = self.rect.centery



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

        self.active = True

    def get_pos(self):
        return (self.x-10, self.y)

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
            self.active = False

    def fire(self, bullets):
        bullet = BulletEnemy(self.settings, self.get_pos())
        bullets.add(bullet)

    def blitme(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def restart(self):
        self.x = random.randint(10, self.width_limit-10)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + self.settings.enemy_speed_factor
        self.move_left = random.choice([-1, 1])
