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

    # interval_b = 0
    # bullets = []
    # for i in range(5):
    #     bullets.append(Bullet(hero, settings))
    # count_b = len(bullets)
    # index_b = 0

    enemies = pygame.sprite.Group()
    for i in range(settings.enemy_limit):
        enemy = Enemy(settings)
        enemies.add(enemy)
        # enemy.blitme(screen)
    # Loading hero
    hero = Hero(screen, settings)
    # Creating hero bullet list
    hero_bullets = pygame.sprite.Group()
    # Game over flag, True if game is over
    game_over = False

    # def check_hit(enemy, bullet):
    #     if enemy.x < bullet.x < enemy.x + enemy.image.get_width() and enemy.y < bullet.y < enemy.y + enemy.image.get_height():
    #         enemy.restart()
    #         bullet.active = False
    #         return True 
    #     return False


    # def check_crash(hero, enemy):
    #     if hero.x + hero.image.get_width()*0.7 > enemy.x and hero.x + hero.image.get_width()*0.3 < enemy.x + enemy.image.get_width() and hero.y + hero.image.get_height()*0.7 > enemy.y and hero.y + hero.image.get_height()*0.3 < enemy.y + enemy.image.get_height():
    #         return True 
    #     return False


    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         exit()
        #     if game_over:
        #         hero.restart()
        #         for enemy in enemies:
        #             enemy.restart()
        #         for bullet in bullets:
        #             bullet.active = False
        #         score = 0
        #         game_over = False
        
        # screen.blit(background, (0, 0))

        # interval_b -= 1
        # if interval_b < 0:
        #     bullets[index_b].restart()
        #     interval_b = 100
        #     index_b = (index_b+1) % count_b

        # for bullet in bullets:
        #     if bullet.active:
        #         bullet.move()
        #         bullet.blitme(screen)
        #         for enemy in enemies:
        #             if check_hit(enemy, bullet):
        #                 scoreboard.add_curent_score()

        # for enemy in enemies:
        #     if check_crash(hero, enemy):
        #         game_over = True
        #         scoreboard.reset()
        #     enemy.blitme(screen)
        #     enemy.move()

        # hero.blitme()
        # hero.move_by_keyboard()

        # scoreboard.blitme(screen)

        gf.check_events(screen, hero, hero_bullets, settings)
        gf.update_enemies(screen, enemies, hero, scoreboard)
        gf.update_bullets(screen, hero_bullets, enemies, scoreboard, settings)
        gf.update_screen(screen, hero_bullets, enemies, background, hero, scoreboard, settings)

        # pygame.display.update()

if __name__ == "__main__":
    run()
