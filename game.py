import pygame
from plane import Hero
from settings import Settings
from scoreboard import ScoreBoard
from sys import exit
import game_functions as gf

# Entry of the game
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
    enemies = pygame.sprite .Group()
    # Loading hero
    hero = Hero(screen, settings)
    # Creating hero bullet group
    hero_bullets = pygame.sprite.Group()
    # Creating enemy bullet group
    enemy_bullets = pygame.sprite.Group()
    # Game start
    while True: 
        # Check game events
        gf.check_events(hero, hero_bullets)
        # Updating enemies
        gf.update_enemies(screen, enemies, hero, hero_bullets, enemy_bullets, scoreboard, settings)
        # Updating hero bullets
        gf.update_hero_bullets(screen, hero_bullets, enemies, scoreboard, settings)
        # Updating enemy bullets
        gf.update_enemy_bullets(hero_bullets, enemy_bullets, hero, settings, enemies, scoreboard)
        # Refresh screen
        gf.update_screen(screen, hero_bullets, enemy_bullets, enemies, background, hero, scoreboard, settings)


if __name__ == "__main__":
    run()
