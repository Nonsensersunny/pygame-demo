

class GameStats():

	def __init__(self, setting):
		self.setting = setting
		self.game_active = False
		self.reset_stats()

	def reset_stats(self):
		self.ships_left = self.setting.ship_limit
		self.score = 0
		self.level = 1
