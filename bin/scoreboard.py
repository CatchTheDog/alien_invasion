import pygame
from pygame.sprite import Group

from ship import Ship


class Scoreboard():
	"""显示得分信息的类"""
	
	def __init__(self, ai_settings, screen, stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont("consolas", 48)
		
		# 准备初始得分图像
		self.prep_score()
		
		# 准备包含最高得分和当前得分的图像
		self.prep_highest_score()
		
		# 游戏等级显示
		self.prep_level()
		
		# 显示剩余飞船数
		self.prep_ships()
	
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		
		# 将得分你放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.screen_rect.top = 20
	
	def show_score(self):
		"""在屏幕上显示得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.highest_score_image, self.highest_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
	
	def prep_highest_score(self):
		"""将最高得分转换为渲染的图像"""
		highest_score = int(round(self.stats.highest_score, -1))
		highest_score_str = "{:,}".format(highest_score)
		self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)
		
		# 将最高得分置于屏幕顶部中央
		self.highest_score_rect = self.highest_score_image.get_rect()
		self.highest_score_rect.centerx = self.screen_rect.centerx
		self.highest_score_rect.top = self.score_rect.top
	
	def prep_level(self):
		"""将等级转换为渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		
		# 将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
	
	def prep_ships(self):
		"""显示剩余多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
