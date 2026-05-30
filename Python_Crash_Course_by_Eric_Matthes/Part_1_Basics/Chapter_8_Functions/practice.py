from calculate_area import square_area as s_a, circle_area as c_a

# 8-1. Message: Write a function called display_message() that prints one
# sentence telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly
def display_message():
	"""Display message about learning functions"""
	print("I am learning about functions in Python")

# display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book(title):
	print(f"One of my favorite books is: {title}")

# favorite_book('Alice in Wonderland')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt and the message printed on
# it. Call the function once using positional arguments to make a shirt. Call
# the function a second time using keyword arguments.
def make_shirt(size='L', msg='I love Python'):
	print(f"A T-Shirt of size: {size} with message: {msg}")

make_shirt('S', 'Python is awesome')
make_shirt(msg='Python is awesome', size='S')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
make_shirt()
make_shirt(size='M')
make_shirt(size='XXL', msg='Python is great!')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not
# in the default country.
def describe_city(name, country='Germany'):
	print(f"{name} is in {country}")

# describe_city('Berlin')
# describe_city('Paris', 'France')
# describe_city('Bucharest', 'Romania')

# 8-7. Album:
# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the
# number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.
def make_album(artist_name, album_title, number_of_tracks = 0):
	album = {
		'artist_name': artist_name,
		'album_title': album_title,
	}

	if number_of_tracks:
		album['number_of_tracks'] = number_of_tracks
	
	return album

# make_album('Eminem', 'The Marshall Mathers LP')
# make_album('Pink Floyd', 'The Dark Side of the Moon')
# make_album('Kendrick Lamar', 'To Pimp a Butterfly')
# make_album('Eminem', 'The Marshall Mathers LP', number_of_tracks=20)

# while True:
# 	print('Press \'q\' to quit:\n')
# 	option = input('Enter continue or \'q\' to quit')
	
# 	if option == 'q':
# 		break

# 	artist_name 	 = input('Enter artist name:\n')
# 	album_title  	 = input('Enter album title:\n')
# 	number_of_tracks = input('Enter number of tracks on the album (optional):\n')
	
# 	if number_of_tracks:
# 		number_of_tracks = int(number_of_tracks)

# 	album = make_album(artist_name, album_title, number_of_tracks)
	
# 	print(album)

# 8-9. Magicians:
# Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list
magician_list = ['Houdini', 'Copperfield', 'Blaine', 'Angel', 'Burton']
def show_magicians(magicians):
	for magician in magicians:
		print(f"{magician}")

# show_magicians(magician_list)

# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by
# adding the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
def great_magicians(magicians):
	for index, magician in enumerate(magicians):
		magicians[index] = f"The Great {magicians[index]}"
		print(f"{magician}")

# great_magicians(magician_list[:])
# show_magicians(magician_list)
# great_magicians(magician_list)
# show_magicians(magician_list)

# 8-11. Unchanged Magicians:
# Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate
# list.
# Call show_magicians() with each list to show that you have one list of the
# original names and one list with the Great added to each magician’s name.

# 8-12. Sandwiches:
# Write a function that accepts a list of items a person wants
# on a sandwich. The function should have one parameter that collects as many
# items as the function call provides, and it should print a summary of the
# sandwich that is being ordered. Call the function three times, using a
# different number of arguments each time.
def make_sandwich(*ingredients):
	for ingredient in ingredients:
		print(ingredient)

# make_sandwich('turkey', 'cheese', 'lettuce')
# make_sandwich('ham', 'mustard')
# make_sandwich('tuna', 'mayo', 'pickles', 'onion', 'tomato')

def build_profile(first_name, last_name, **info_list):
	profile = dict()

	profile['first_name'] = first_name
	profile['last_name']  = last_name
	for k, v in info_list.items():
		profile[k] = v

	return profile

profile = build_profile(
	'mihai',
	'ionescu',
	city='brașov',
	profession='full-stack developer',
	hobby='hiking',
)
# print(profile)

# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments. Call the
# function with the required information and two other name-value pairs, such as
# a color or an optional feature. Your function should work for a call like
# this one:
def make_car(manufacturer, model_name, **features):
	car 				= dict()
	car['manufacturer'] = manufacturer
	car['model_name']   = model_name

	for k, v in features.items():
		car[k] = v

	return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

print(s_a(12))
print(c_a(2))
