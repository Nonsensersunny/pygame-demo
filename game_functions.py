import pygame
from enemy import Enemy
from bullet import Bullet
import sys 


def check_hit(enemy, bullet, screen):
    if enemy.rect.centerx < bullet.rect.centerx < enemy.rect.centery + enemy.image.get_width() and enemy.rect.centery < bullet.rect.centery < enemy.rect.centery + enemy.image.get_height():
        # enemy.explode(screen)
        enemy.restart()
        bullet.active = False
        return True
    return False


def check_crash(hero, enemy):
    if hero.rect.centerx + hero.image.get_width()*0.7 > enemy.rect.centerx and hero.rect.centerx + hero.image.get_width()*0.3 < enemy.rect.centerx + enemy.image.get_width() and hero.rect.centery + hero.image.get_height()*0.7 > enemy.rect.centery and hero.rect.centery + hero.image.get_height()*0.3 < enemy.rect.centery + enemy.image.get_height():
        return True
    return False


def set_background(screen, image):
    screen.blit(image, (0, 0))


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
    # print(len(bullets))


def check_bullet_enemy_hit(enemies, bullets, scoreboard, settings):
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for i in collisions.values():
            scoreboard.add_curent_score(len(i))
            print("Hit!")
    if len(enemies) == 0:
        enemies.add(Enemy(settings))


def check_hero_crash(hero, enemies):
    if pygame.sprite.spritecollideany(hero, enemies):
        return True 
    return False


def check_events(screen, hero, bullets, settings):
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[27] == 1 or event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(screen, hero, bullets, settings)
        elif event.type == pygame.KEYUP:
            check_key_up_events(hero)


# def create_enemies(screen, enemies, settings, num):
#     for i in range(num):
#         enemy = Enemy(settings)
#         enemies.add(enemy)


def update_bullets(screen, bullets, enemies, scoreboard, settings):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.centery <= 0:
            bullets.remove(bullet)
    check_bullet_enemy_hit(enemies, bullets, scoreboard, settings)


def update_enemies(screen, enemies, hero, scoreboard):
    enemies.update()
    for enemy in enemies:
        enemy.update()
    if pygame.sprite.spritecollideany(hero, enemies):
        # print("Hero hit enemy!")
        scoreboard.reset()
        hero.restart()


def update_screen(screen, bullets, enemies, image, hero, scoreboard, settings):
    set_background(screen, image)
    scoreboard.blitme(screen)
    
    for bullet in bullets:
        bullet.blitme(screen)

    hero.blitme()
    hero.move_by_keyboard()
    enemies.draw(screen)
    for enemy in enemies:
        enemy.blitme(screen)
    
    pygame.display.flip()
