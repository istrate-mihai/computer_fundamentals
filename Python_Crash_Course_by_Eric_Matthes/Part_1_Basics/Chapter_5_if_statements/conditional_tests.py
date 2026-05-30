# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your
# code should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	 Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# •	 Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.
# car = 'subaru'
# print("Is car == 'subaru' ? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi' ? I predict False.")
# print(car == 'audi')

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an
# if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed
# for the appropriate color alien.
alien_color = 'red'
if alien_color == 'green':
	print('You just earned 5 points')
elif alien_color == 'yellow':
	print('You just earned 10 points')
elif alien_color == 'red':
	print('You just earned 15 points')

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# •	 If the person is less than 2 years old, print a message that the person is
# a baby.
# •	 If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# •	 If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# •	 If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# •	 If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# •	 If the person is age 65 or older, print a message that the person is an
# elder.
age = 75
if age < 2:
	print("The person is a baby")
elif age >= 2 and age < 4:
	print("The person is a toddler")
elif age >= 4 and age < 13:
	print("The person is a kid")
elif age >= 13 and age < 20:
	print("The person is a teenager")
elif age >= 20 and age < 65:
	print("The person is a adult")
else:
	print("The person is an elder")

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a
# series of independent if statements that check for certain fruits in your list.
# •	 Make a list of your three favorite fruits and call it favorite_fruits.
# •	 Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a
# statement, such as You really like bananas!
favorite_fruits = ['apple', 'banana']

if 'apple' in favorite_fruits:
	print('You really like apples!')

if 'banana' in favorite_fruits:
	print('You really like bananas!')

if 'strawberries' in favorite_fruits:
	print('You really like strawberries!')

if 'kiwi' in favorite_fruits:
	print('You really like kiwis!')

# 5-8. Hello Admin:
# Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# •	 If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# •	 Otherwise, print a generic greeting, such as Hello Eric, thank you for
# logging in again

user_list = ['admin', 'eric', 'tom', 'jill', 'peter']
if len(user_list) != 0:
	for user in user_list:
		if user == 'admin':
			print('Hello admin, would you like to see a status report ?')
		else:
			print('Hello ' + user.title() + ', thank you for logging in again.')
else:
	print('We need to find some users!')

# 5-10. Checking Usernames:
# Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# •	 Make a list of five or more usernames called current_users.
# •	 Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# •	 Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# •	 Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.
current_users = ['dan', 'marius', 'carla', 'johanna']
new_users 	  = ['jerry', 'darius', 'DAN']

if new_users:
	for new_user in new_users:
		if new_user.lower() in current_users:
			print('Enter a new username')
		else:
			print('Username is available')

# 5-11. Ordinal Numbers:
# Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	 Store the numbers 1 through 9 in a list.
# •	 Loop through the list.
# •	 Use an if-elif-else chain inside the loop to print the proper ordinal
# ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.
number_list = list(range(1, 10))
for number in number_list:
	str_number = str(number)
	if number == 1:
		print(str_number + 'st')
	elif number == 2:
		print(str_number + 'nd')
	elif number == 3:
		print(str_number + 'rd')
	else:
		print(str_number + 'th')
