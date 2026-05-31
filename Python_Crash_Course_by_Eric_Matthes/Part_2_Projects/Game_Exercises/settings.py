class Settings:
	"""A class to store all settings for the game."""

	def __init__(
			self,
			screen_width=1200,
			screen_height=700,
			bg_color=(0, 0, 0)
		):
		"""Initialize the game's settings."""

		self.screen_width  = screen_width
		self.screen_height = screen_height
		self.bg_color 	   = bg_color
