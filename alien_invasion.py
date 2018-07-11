import sys
import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from life import Life

def run_game():
	# Initialize the game
	pygame.init()
	# Configure the game
	setting = Settings()
	screen = pygame.display.set_mode(setting.get_screen_size())
	pygame.display.set_caption('Alien Invasion')
	# Create button
	play_button = Button(setting, screen, 'Play')
	# Create a ship
	ship = Ship(screen)
	# Create game stats instance
	game_stats = GameStats(setting)
	# Create score board
	sb = ScoreBoard(screen, setting, game_stats)
	# Create bullets
	bullets = Group()
	# Create aliens
	aliens = Group()
	# Create life
	lifes = Group()
	while True:
		# 监听
		gf.check_events(setting, screen, ship, bullets, game_stats, play_button, aliens, lifes)
		if game_stats.game_active:
			gf.update_aliens(aliens, setting, ship, game_stats, bullets, screen, lifes)
			gf.update_bullets(bullets, aliens, screen, setting, game_stats, sb)
		gf.update_screen(setting, screen, ship, bullets, aliens, play_button, game_stats, sb, lifes)

	
run_game() 
