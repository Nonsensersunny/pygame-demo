import pygame

class Ship():

	def __init__(self, screen):
		# Initialize the ship
		self.screen = screen
		# Loading ship and the rect
		self.image = pygame.image.load('images/hero.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Locate the ship to the center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		self.screen.blit(self.image, self.rect)


	def update(self, setting):
		width, height = setting.get_screen_size()
		if self.moving_right:
			if self.rect.centerx > width:
				self.rect.centerx = width
			else:
				self.rect.centerx += setting.ship_speed_factor
		if self.moving_left:
			if self.rect.centerx < 0:
				self.rect.centerx = 0
			else:
				self.rect.centerx -= setting.ship_speed_factor
		if self.moving_up:
			if self.rect.centery < 0:
				self.rect.centery = 0
			else:
				self.rect.centery -= setting.ship_speed_factor
		if self.moving_down:
			if self.rect.centery > height:
				self.rect.centery = height
			else:
				self.rect.centery += setting.ship_speed_factor

	def center_ship(self):
		self.rect.centerx, self.rect.bottom = self.screen_rect.centerx, self.screen_rect.bottom
