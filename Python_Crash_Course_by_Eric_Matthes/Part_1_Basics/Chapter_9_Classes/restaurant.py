# 9-1. Restaurant:
# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

# 9-4. Number Served:
# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class
# you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either
# version of the class will work; just pick the one you like better. Add an
# attribute called flavors that stores a list of ice cream flavors. Write a
# method that displays these flavors. Create an instance of IceCreamStand, and
# call this method.

# 9-10. Imported Restaurant:
# Using your latest Restaurant class, store it in a module. Make a separate
# file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant’s methods to show that the import statement is
# working properly
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type 	 = cuisine_type
		self.number_served 	 = 0

	def describe_restaurant(self):
		print(f"""
			Restaurant name: {self.restaurant_name}\n
			Cuisine type: {self.cuisine_type}
		""")
	
	def open_restaurant(self):
		print(f"{self.restaurant_name} is opened")

	def set_number_served(self, number_served):
		self.number_served = number_served
	
	def increment_number_served(self, number_served):
		self.number_served += number_served
