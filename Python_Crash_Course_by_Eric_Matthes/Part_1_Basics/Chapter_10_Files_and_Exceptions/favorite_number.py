import json

# 10-11. Favorite Number:
# Write a program that prompts for the user’s favorite
# number. Use json.dump() to store this number in a file. Write a separate
# program that reads in this value and prints the message, “I know your favorite
# number! It’s _____.”

# 10-12. Favorite Number Remembered:
# Combine the two programs from
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

def store_favorite_number(filename):
	favorite_number = None

	while not isinstance(favorite_number, (int, float)):
		try:
			favorite_number = int(input('Enter your favorite number:\n'))
		except ValueError:
			print('Please enter a number')
		else:
			with open(filename, 'a') as file_object:
				json.dump(favorite_number, file_object)

	return favorite_number

def get_favorite_number(filename):

	try:
		with open(filename) as file_object:
			favorite_number = json.load(file_object)
	except FileNotFoundError:
		return None
	else:
		return favorite_number

def print_favorite_number(number):
	print(f"I know what your favorite number is! It's {number}.")

def remember_favorite_number(filename):
	favorite_number = get_favorite_number(filename)

	if favorite_number:
		print_favorite_number(favorite_number)
	else:
		favorite_number = store_favorite_number(filename)
		print(
			f"We'll remember your favorite number as {favorite_number}, " +
			"when you come back"
		)

filename = './favorite_number.json'
remember_favorite_number(filename)
