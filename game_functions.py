import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from life import Life

def check_key_down_events(setting, screen, ship, bullets, stats, aliens, lifes):
	keys = pygame.key.get_pressed()
	if keys[275] == 1:
		ship.moving_right = True
	if keys[276] == 1:
		ship.moving_left = True
	if keys[273] == 1:
		ship.moving_up = True
	if keys[274] == 1:
		ship.moving_down = True
	if keys[32] == 1:
		fire_bullet(bullets, setting, screen, ship)
	if keys[112] == 1:
		start_game(stats, aliens, bullets, screen, setting, ship, lifes)


def check_key_up_events(ship):
	keys = pygame.key.get_pressed()
	if keys[275] == 0:
		ship.moving_right = False
	if keys[276] == 0:
		ship.moving_left = False
	if keys[273] == 0:
		ship.moving_up = False
	if keys[274] == 0:
		ship.moving_down = False


def check_events(setting, screen, ship, bullets, stats, play_button, aliens, lifes):
	# Respond to the events created by player
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		if keys[27] == 1 or event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_key_down_events(setting, screen, ship, bullets, stats, aliens, lifes)
		elif event.type == pygame.KEYUP:
			check_key_up_events(ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, setting, screen, lifes)


def start_game(stats, aliens, bullets, screen, setting, ship, lifes):
	setting.initialize_dynamic_settings()
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	stats.game_active = True
	aliens.empty()
	bullets.empty()
	create_fleet(screen, aliens, setting)
	create_life(screen, setting, lifes)
	ship.center_ship()


def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, setting, screen, lifes):
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(stats, aliens, bullets, screen, setting, ship, lifes)


def update_screen(setting, screen, ship, bullets, aliens, play_button, stats, sb, lifes):
	# Refresh the screen
	screen.fill(setting.get_bg_color())
	sb.draw_score()
	sb.draw_high_score()
	sb.draw_level()
	for bullet in bullets:
		bullet.draw_bullet()
	# update_life(lifes)
	ship.blitme()
	aliens.draw(screen)
	ship.update(setting)
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()


def update_bullets(bullets, aliens, screen, setting, stats, sb):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	check_alien_bullet_collisions(bullets, aliens, screen, setting, stats, sb)


# 检查撞击元素
def check_alien_bullet_collisions(bullets, aliens, screen, setting, stats, sb):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for i in collisions.values():
			stats.score += setting.alien_point*len(i)
			if stats.score > setting.get_high_score():
				setting.update_high_score(stats.score)
			sb.prep_high_score()
			sb.prep_score()
	if len(aliens) == 0:
		stats.level += 1
		sb.prep_level()
		bullets.empty()
		setting.increase_speed()
		create_fleet(screen, aliens, setting)


def fire_bullet(bullets, setting, screen, ship):
	if len(bullets) < setting.bullet_allowed:
		new_bullet = Bullet(setting, screen, ship)
		bullets.add(new_bullet)


def get_number_aliens_x(screen_width, alien_width):
	available_spacex = screen_width - 2*alien_width
	number_alienx = available_spacex/(alien_width*6/5)
	return int(number_alienx)


def get_number_aliens_y(screen_height, alien_height):
	available_spacey = screen_height - 3*alien_height
	number_alieny = available_spacey/(alien_height*6/5)
	alien_y = []
	for i in range(int(number_alieny)):
		alien_y.append(alien_height*(i*1.5 + 1))
	return alien_y


def create_alien(screen, aliens, number_x, number_y):
	for i in range(number_x):
		for j in number_y:
			alien = Alien(screen)
			alien.rect.centerx = alien.rect.width*(i*1.5 + 1)
			alien.rect.centery = j
			aliens.add(alien)


def create_life(screen, setting, lifes):
	for i in range(setting.ship_limit):
		life = Life(screen)
		life.rect.centerx = life.rect.width*(i + 1)
		life.rect.centery = 20
		lifes.add(life)


def update_life(lifes):
	for life in lifes:
		life.blitme()


def create_fleet(screen, aliens, setting):
	alien = Alien(screen)
	alien_width, alien_height = alien.rect.width, alien.rect.height
	screen_width, screen_height = setting.screen_size
	number_alienx = get_number_aliens_x(screen_width, alien_width)
	number_alieny = get_number_aliens_y(screen_height, alien_height)
	create_alien(screen, aliens, number_alienx, number_alieny)


def update_aliens(aliens, setting, ship, stats, bullets, screen, lifes):
	for alien in aliens:
		alien.update(setting)
	if pygame.sprite.spritecollideany(ship, aliens) or check_aliens_bottom(aliens, setting, stats, bullets, screen, ship):
		# print('Ship Hit!')
		ship_hit(stats, aliens, bullets, screen, setting, ship, lifes)


def ship_hit(stats, aliens, bullets, screen, setting, ship, lifes):
	if stats.ships_left > 1:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()
		# update_life(lifes)
		create_fleet(screen, aliens, setting)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)


def check_aliens_bottom(aliens, setting, stats, bullets, screen, ship):
	screen_width, screen_height = setting.screen_size
	for alien in aliens:
		if alien.rect.bottom >= screen_height:
			return True
	return False


def show_high_score(sb):
	sb.draw_high_score()
