import pygame
from enemy import Enemy
from bullet import Bullet
from bullet_enemy import BulletEnemy
import sys 
import random

BG_START = 0

def check_hit(body, bullet):
    if body.x < bullet.rect.centerx < body.x + body.image.get_width() and body.y < bullet.rect.centery < body.y + body.image.get_height():
        body.restart()
        bullet.active = False
        return True
    return False


def check_enemy_hero_crash(hero, enemy):
    if hero.rect.centerx - hero.image.get_width()/2 < enemy.x < hero.rect.centerx + hero.image.get_width()/2 and hero.rect.centery - hero.image.get_height()/2 < enemy.y < hero.rect.centery + hero.image.get_height()/2:
        return True 
    return False


def set_background_up(screen, image, settings):
    global BG_START
    screen.blit(image, (0, BG_START - image.get_height()))


def set_background_down(screen, image, settings):
    global BG_START
    screen.blit(image, (0, BG_START))
    BG_START += settings.ship_speed_factor*2
    if BG_START >= image.get_height():
        BG_START = 0


def background_scroll(screen, image, settings):
    set_background_down(screen, image, settings)
    set_background_up(screen, image, settings)


def check_key_down_events(screen, hero, bullets, settings):
    keys = pygame.key.get_pressed()
    if keys[275] == 1:
        hero.moving_right = True
    if keys[276] == 1:
        hero.moving_left = True
    if keys[273] == 1:
        hero.moving_up = True
    if keys[274] == 1:
        hero.moving_down = True
    if keys[32] == 1:
        hero_open_fire(screen, hero, bullets, settings)
    if keys[112] == 1:
        print("Start game")


def check_key_up_events(hero):
    keys = pygame.key.get_pressed()
    if keys[275] == 0:
        hero.moving_right = False
    if keys[276] == 0:
        hero.moving_left = False
    if keys[273] == 0:
        hero.moving_up = False
    if keys[274] == 0:
        hero.moving_down = False


def hero_open_fire_auto(screen, hero, bullets, settings):
    if len(bullets) < settings.hero_bullets_limit:
        bullets.append(Bullet(hero, settings))


def hero_open_fire(screen, hero, bullets, settings):
    if len(bullets) < settings.hero_bullets_limit:
        bullets.add(Bullet(hero, settings))


def enemy_open_fire(screen, enemy, bullets, settings):
    if len(bullets) < settings.enemy_bullets_limit:
        bullets.add(BulletEnemy(settings, enemy))


def check_events(screen, hero, bullets, settings):
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[27] == 1 or event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(screen, hero, bullets, settings)
        elif event.type == pygame.KEYUP:
            check_key_up_events(hero)


def create_enemies(enemies, settings):
    for i in range(settings.enemy_limit):
        enemy = Enemy(settings)
        enemies.add(enemy)


def restart_game(hero, hero_bullets, enemy_bullets, enemies, scoreboard, settings):
    scoreboard.reset()
    hero.restart()
    hero_bullets.empty()
    enemy_bullets.empty()
    enemies.empty()
    create_enemies(enemies, settings)


def update_hero_bullets(screen, bullets, enemies, scoreboard, settings):
    for bullet in bullets:
        bullet.update()
        if bullet.rect.centery <= 0:
            bullets.remove(bullet)
        for enemy in enemies:
            if check_hit(enemy, bullet):
                scoreboard.add_curent_score(1)


def update_enemy_bullets(hero_bullets, enemy_bullets, hero, settings, enemies, scoreboard):
    for bullet in enemy_bullets:
        bullet.update()
        if bullet.rect.centery >= settings.screen_size[1]:
            enemy_bullets.remove(bullet)
            if check_hit(hero, bullet):
                restart_game(hero, hero_bullets, enemy_bullets, enemies, scoreboard, settings)


def update_enemies(screen, enemies, hero, hero_bullets, enemy_bullets, scoreboard, settings):
    for enemy in enemies:
        enemy.update()
        if random.random() > 0.9:
            # enemy.fire(enemy_bullets)
            enemy_open_fire(screen, enemy, enemy_bullets, settings)
        if check_enemy_hero_crash(hero, enemy):
            restart_game(hero, hero_bullets, enemy_bullets, enemies, scoreboard, settings)


def update_screen(screen, hero_bullets, enemy_bullets, enemies, image, hero, scoreboard, settings):
    # Render background
    background_scroll(screen, image, settings)
    set_background_down(screen, image, settings)
    # Render hero
    hero.blitme()
    # Control system
    hero.move_by_keyboard()
    # Render enemies
    for enemy in enemies:
        enemy.blitme(screen)
    # Render socre board
    scoreboard.blitme(screen)
    # Render bullets
    for bullet in hero_bullets:
        bullet.blitme(screen)
    for bullet in enemy_bullets:
        bullet.blitme(screen)
    # Refresh interface
    pygame.display.flip()
