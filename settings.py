import configparser


class Settings:
    def __init__(self):
        self.screen_size = self.get_screen_size()
        self.hero_limit = 3
        self.enemy_limit = 5
        self.enemy_point = 10
        self.ship_speed_factor = 0.1
        self.enemy_speed_factor = 0.1
        self.hero_bullet_speed_factor = 0.1
        self.hero_bullets_limit = 10
        self.enemy_bullet_speed_factor = 0.1

    def get_screen_size(self):
        return list(map(int, (self.get_configs('screenSize', 'width'), self.get_configs('screenSize', 'height'))))

    def get_high_score(self):
        return int(self.get_configs('record', 'highest'))

    def get_life_limit(self):
        return int(self.get_configs('life', 'limit'))

    def get_configs(self, option, item):
        cf = configparser.ConfigParser()
        cf.read(r'game.ini', encoding='utf8')
        return cf.get(option, item)

    def update_high_score(self, new_record):
        cf = configparser.ConfigParser()
        cf.read('game.ini', encoding='utf8')
        cf.set('record', 'highest', str(int(new_record)))
        cf.write(open('game.ini', 'r+'))

    def speed_up(self):
        self.enemy_limit += 1
        self.enemy_point += 10
        self.ship_speed_factor += 0.1
        self.enemy_speed_factor += 0.2
        self.hero_bullet_speed_factor += 0.1
        self.enemy_bullet_speed_factor += 0.1
        self.enemy_bullets_limit += 3
