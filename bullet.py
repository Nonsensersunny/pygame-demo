import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, setting, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('images/bullet.png')
		self.rect = self.image.get_rect()

		# self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
		self.rect.centerx, self.rect.centery = ship.rect.centerx, ship.rect.top
		# self.color = setting.bullet_color
		self.speed_factor = setting.bullet_speed_factor

	def update(self):
		self.rect.centery -= self.speed_factor

	def draw_bullet(self):
		# pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.image, self.rect)







