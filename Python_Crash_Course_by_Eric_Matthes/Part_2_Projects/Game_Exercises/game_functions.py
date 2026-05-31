import sys
import pygame

def check_events():
	"""Respond to keypresses and mouse events."""

	for event in pygame.event.get():
		if event == pygame.QUIT:
			sys.exit()

def update_screen(screen, settings, rocket):
	"""Update images on the screen and flip to the new screen."""

	screen.fill(settings.bg_color)
	rocket.blitme()

	pygame.display.flip()
