from restaurant import Restaurant
from ice_cream_stand import IceCreamStand

restaurant = Restaurant('The Rustic Bistro', 'Modern American')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)

flavors = [
	'Stracciatella',
	'Pistachio',
	'Dark Chocolate',
	'Blood Orange Sorbet',
	'Salted Caramel'
]
iceCreamStand = IceCreamStand('Gelato Paradiso', 'Italian Dessert', flavors)
iceCreamStand.display_flavors()
