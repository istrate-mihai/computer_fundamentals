# 10-3. Guest:
# Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt
name     = input("Enter your name:\n")
filename = 'guest.txt'

with open(filename, 'a') as file_object:
	file_object.write(name)

# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

while True:
	reason = input('Why do you like programming:\n')

	if not reason:
		break
	with open('programming_poll.txt', 'a') as file_object:
		file_object.write(reason + "\n")
