# 7-1. Rental Car:
# Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.
car_choice = input("What kind of car do you want ?:\n")
print(f"Let me see if I can find you a {car_choice.title()}")

# 7-2. Restaurant Seating:
# Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message
# saying they’ll have to wait for a table. Otherwise, report that their
# table is ready.
people_at_table = int(input("How many people are in your dinner group ?\n"))
if people_at_table > 8:
	print("You'll have to wait for a table.")
else:
	print("Your table is ready")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not
multiple_of_10 = int(input("Enter a multiple of 10:\n"))
if (multiple_of_10 % 10) == 0:
	print(f"{multiple_of_10} is a multiple of 10")
else:
	print(f"{multiple_of_10} is not a multiple of 10")
