import configparser

class Settings():

	def __init__(self):
		self.screen_size = self.get_screen_size()
		self.button_size = self.get_button_size()
		self.bg_color = self.get_bg_color()

		self.ship_limit = 3
		self.bullet_allowed = 5
		self.fleet_drop_speed = 20

		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def get_screen_size(self):
		return list(map(int, (self.get_configs('screenSize', 'width'), self.get_configs('screenSize', 'height'))))


	def get_bg_color(self):
		return list(map(int, (self.get_configs('bgColor', 'r'), self.get_configs('bgColor', 'g'), self.get_configs('bgColor', 'b'))))


	def get_button_size(self):
		return list(map(int, (self.get_configs('buttonStyle', 'width'), self.get_configs('buttonStyle', 'height'))))


	def get_high_score(self):
		return int(self.get_configs('gameRecord', 'highest'))


	def get_configs(self, option, item):
		cf = configparser.ConfigParser()
		cf.read(r'game.ini', encoding='utf8')
		return cf.get(option, item)


	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 3
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 5
		self.alien_point = 50


	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_point *= self.speedup_scale


	def update_high_score(self, new_record):
		cf = configparser.ConfigParser()
		cf.read('game.ini', encoding='utf8')
		cf.set('gameRecord', 'highest', str(int(new_record)))
		cf.write(open('game.ini', 'r+'))
