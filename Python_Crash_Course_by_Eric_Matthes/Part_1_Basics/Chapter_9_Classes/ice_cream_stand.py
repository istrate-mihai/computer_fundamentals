from restaurant import Restaurant

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def display_flavors(self):
		for flavor in self.flavors:
			print(flavor)
