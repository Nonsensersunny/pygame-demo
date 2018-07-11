import pygame
from pygame.sprite import Sprite

class Life(Sprite):

    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.centerx = self.rect.left
        self.rect.centery = self.rect.bottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)
