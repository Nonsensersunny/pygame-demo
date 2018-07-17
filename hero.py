import pygame
import random
from settings import Settings


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

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def restart(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.x = self.rect.centerx
        self.y = self.rect.centery
