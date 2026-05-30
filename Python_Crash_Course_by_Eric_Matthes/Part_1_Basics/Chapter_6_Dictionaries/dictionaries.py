# 6-1. Person:
# Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
person = {
	'first_name': 'John',
	'last_name': 'Doe',
	'age': 30,
	'location': 'New York',
}

# for info_key in person:
# 	print(person[info_key])

# 6-2. Favorite Numbers:
# Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
favorite_numbers = {
	'dan': 10,
	'marius': 5,
	'carla': 4,
	'johanna': 7,
}

# for number_key in favorite_numbers:
# 	print(
# 		number_key.title() +
# 		'\'s favorite number is: ' +
# 		str(favorite_numbers[number_key])
# 	)

# 6-5. Rivers:
# Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# •	 Use a loop to print the name of each river included in the dictionary.
# •	 Use a loop to print the name of each country included in the dictionary.
# rivers = {
# 	'nile': 'egypt',
# 	'amazon': 'brazil',
# 	'yangtze': 'china'

# }

# for river, country in rivers.items():
# 	print('The ' + river.title() + ' runs through ' + country.title())

# for river in rivers.keys():
# 	print('River name: ' + river.title())

# for country in rivers.values():
# 	print('Country name: ' + country.title())

# 6-6. Polling:
# Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
favorite_languages = {
	'jen': 		'python',
	'sarah': 	'c',
	'edward': 	'ruby',
	'phil': 	'python',
 }

# people_to_poll = ['james', 'dan', 'caty', 'edward', 'phil']
# for person in people_to_poll:
# 	if person in favorite_languages:
# 		print('Thank you for taking the poll !')
# 	else:
# 		print('Please take the favorite language poll.')

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
person_1 = person
person_2 = {
    'first_name': 'Ana',
    'last_name': 'Popescu',
    'age': 27,
    'location': 'Cluj-Napoca',
}
person_3 = {
    'first_name': 'Mihai',
    'last_name': 'Ionescu',
    'age': 34,
    'location': 'Brașov',
}

people = [person_1, person_2, person_3]
# for person in people:
# 	print(person)
# 	full_name = person['first_name'] + ' ' + person['last_name']

# 	print(
# 		'\nPerson\'s name: ' 	+ full_name 			+
# 		'\nAge: ' 			 	+ str(person['age'])	+
# 		'\nLocation: ' 			+ person['location']
# 	)

# 6-8. Pets:
# Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet

# filename: pets.py

whiskers = {
    'animal': 'cat',
    'owner': 'John Doe',
}

rex = {
    'animal': 'dog',
    'owner': 'Ana Popescu',
}

bubbles = {
    'animal': 'fish',
    'owner': 'Mihai Ionescu',
}

pets = [whiskers, rex, bubbles]

# for pet in pets:
#     print(f"This pet is a {pet['animal']} owned by {pet['owner']}.")

# 6-9. Favorite Places:
# Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places
favorite_places = {
    'Mihai': ['Brașov', 'Sinaia', 'Cluj-Napoca'],
    'Ana': ['Paris', 'Barcelona'],
    'John': ['Tokyo', 'New York', 'Lisbon'],
}

for person, place_list in favorite_places.items():
	print(
		f"{person}'s favorite places are: "
	)

	for place in place_list:
		print(f"\n{place}")

cities = {
    'Brașov': {
        'country': 'Romania',
        'population': 253_000,
        'fact': 'Home to the Black Church, the largest Gothic church in Eastern Europe.',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13_960_000,
        'fact': 'The most populous metropolitan area in the world.',
    },
    'Lisbon': {
        'country': 'Portugal',
        'population': 545_000,
        'fact': 'One of the oldest cities in the world, predating Rome by centuries.',
    },
}

for city_name, city_info in cities.items():
	print(
		f'''{city_name.title()}, info list:
			• Country: {city_info['country']}
			• Population: {city_info['population']}
			• Fact: {city_info['fact']}
		'''
	)
