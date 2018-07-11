import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.image = pygame.image.load('images/enemy.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = self.rect.left
		self.rect.centery = self.rect.bottom
		
		self.moving_right = True
		self.moving_left = False
	
	# Customize the movement of the ship
	def update(self, setting):
		screen_width, screen_height = setting.screen_size
		if self.moving_right:
			if self.rect.centerx > screen_width:
				self.moving_left = True
				self.moving_right = False
				self.rect.centery += setting.fleet_drop_speed
			else:
				self.rect.centerx += setting.alien_speed_factor
		if self.moving_left:
			if self.rect.centerx < 0:
				self.moving_right = True
				self.moving_left = False
				self.rect.centery += setting.fleet_drop_speed
			else:
				self.rect.centerx -= setting.alien_speed_factor


	def blitme(self):
		self.screen.blit(self.image, self.rect)