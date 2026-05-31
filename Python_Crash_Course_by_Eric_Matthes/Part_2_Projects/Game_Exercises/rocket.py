import pygame

class Rocket:
	def __init__(self, screen):
		"""Initialize the rocket and set its starting position."""

		self.screen      = screen
		self.screen_rect = self.screen.get_rect()
		self.image  	 = pygame.image.load('images/rocket.bmp')
		self.rect   	 = self.image.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

	def blitme(self):
		"""Draw the rocket at its current location."""

		self.screen.blit(self.image, self.rect)
