import pygame
from settings import Settings
import game_functions as gf
from rocket import Rocket

def run_game():
	pygame.init()

	settings = Settings(bg_color=(0, 0, 255))

	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height)
	)

	# Make a rocket
	rocket = Rocket(screen)

	pygame.display.set_caption("Game Exercise")

	while True:
		gf.check_events()
		gf.update_screen(screen, settings, rocket)

run_game()
