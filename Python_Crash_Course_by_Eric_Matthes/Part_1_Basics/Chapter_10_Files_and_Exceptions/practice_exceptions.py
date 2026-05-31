# 10-6. Addition:
# One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text
# instead of a number.
def add_numbers():
	try:
		num_1 = int(input('Enter first number:\n'))
		num_2 = int(input('Enter second number:\n'))

		result = num_1 + num_2
	except ValueError:
		print('Please enter two numbers')
	else:
		print(result)

add_numbers()

# 10-8. Cats and Dogs:
# Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs
# in the second file. Write
# a program that tries to read these files and print the
# contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing.
# Move one of the files to a different location on your system,
# and make sure the code in the except block
# executes properly

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

def read_file(filename):
	try:
		with open(filename, encoding='utf-8') as file_object:
			lines = file_object.readlines()
	except FileNotFoundError:
		# print(f"File {filename} does not exist")
		# Fail silently
		pass
	else:
		for line in lines:
			print(line.rstrip())

files = ['cats.txt', 'dogs.txt']
for file in files:
	read_file(file)

# 10-10. Common Words:
# Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.
def count_word(filename, word):
	try:
		with open(filename, encoding='utf-8') as file_object:
			lines = file_object.readlines()
	except FileNotFoundError:
		pass
	else:
		word_count = 0
		for line in lines:
			word_count += line.lower().count(word)
		
		print(f"The word '{word}' appears {word_count} in {filename}")

files = ['captain_kettle_on_the_war_path.txt']
for file in files:
	count_word(file, 'the')
