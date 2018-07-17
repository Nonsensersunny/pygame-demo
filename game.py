import pygame
from bullet import Bullet
from enemy import Enemy
from hero import Hero
from settings import Settings
from scoreboard import ScoreBoard
from sys import exit
import game_functions as gf


def run():
    # Initialize the game
    pygame.init()
    # Loading settings
    settings = Settings()
    # Loading score board
    scoreboard = ScoreBoard(settings)
    # Setting screen
    screen = pygame.display.set_mode(settings.get_screen_size(), 0, 32)
    # Setting caption
    pygame.display.set_caption("Fleet War")
    # Setting background
    background = pygame.image.load("../pygame/images/background.png").convert()
    # Creating enemies
    enemies = pygame.sprite.Group()
    for i in range(settings.enemy_limit):
        enemy = Enemy(settings)
        enemies.add(enemy)
    # Loading hero
    hero = Hero(screen, settings)
    # Creating hero bullet list
    hero_bullets = pygame.sprite.Group()
    # Creating enemy bullet list
    enemy_bullets = pygame.sprite.Group()
    # Game over flag, True if game is over
    game_over = False

    while True:
        gf.check_events(screen, hero, hero_bullets, settings)
        gf.update_enemies(screen, enemies, hero, hero_bullets, enemy_bullets, scoreboard, settings)
        gf.update_hero_bullets(screen, hero_bullets, enemies, scoreboard, settings)
        gf.update_enemy_bullets(hero_bullets, enemy_bullets, hero, settings, enemies, scoreboard)
        gf.update_screen(screen, hero_bullets, enemy_bullets, enemies, background, hero, scoreboard, settings)

if __name__ == "__main__":
    run()
