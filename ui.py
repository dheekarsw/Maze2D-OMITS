import pygame
from settings import*

class UI:
	def __init__(self,surface):

		# setup 
		self.display_surface = surface 

		# health 
		# self.health_bar = pygame.image.load('../graphics/ui/health_bar.png').convert_alpha()
		# self.health_bar_topleft = (54,39)
		# self.bar_max_width = 152
		# self.bar_height = 4

		# coins 
		self.coin = pygame.image.load('../Awok/graphics/coin.png').convert_alpha()
		self.coin2 = pygame.image.load('../Awok/graphics/coin2.png').convert_alpha()
		self.coin_rect = self.coin.get_rect(topleft = (50,150))
		self.coin_rect2 = self.coin.get_rect(topleft = (50,100))
		self.font = pygame.font.Font('../Awok/graphics/font.ttf',30)

	# def show_health(self,current,full):
	# 	self.display_surface.blit(self.health_bar,(20,10))
	# 	current_health_ratio = current / full
	# 	current_bar_width = self.bar_max_width * current_health_ratio
	# 	health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
	# 	pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)

	def show_coins(self,amount):
		self.display_surface.blit(self.coin,self.coin_rect)
		coin_amount_surf = self.font.render(str(amount),False,'#f3ecdd')
		coin_amount_rect = coin_amount_surf.get_rect(midleft = (self.coin_rect.right + 4,self.coin_rect.centery))
		self.display_surface.blit(coin_amount_surf,coin_amount_rect)

	def show_coins2(self,amount):
		self.display_surface.blit(self.coin2,self.coin_rect2)
		coin_amount_surf2 = self.font.render(str(amount),False,'#f3ecdd')
		coin_amount_rect2 = coin_amount_surf2.get_rect(midleft = (self.coin_rect2.right + 4,self.coin_rect2.centery))
		self.display_surface.blit(coin_amount_surf2,coin_amount_rect2)

	def username(self, name):
		self.user_text = name
		username = self.font.render(name, True, (255, 255, 255))
		self.display_surface.blit(username, ((SCREEN_WIDTH/2)-300, (SCREEN_HEIGHT/2)+300))