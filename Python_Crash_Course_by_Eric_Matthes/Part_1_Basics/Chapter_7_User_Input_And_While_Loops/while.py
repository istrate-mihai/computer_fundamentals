# 7-4. Pizza Toppings:
# Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
# while True:
# 	topping = input("Enter a pizza topping or 'quit' to stop:\n")

# 	if topping == 'quit':
# 		break
# 	print(f"I'll add {topping} to the pizza\n")

# 7-5. Movie Tickets:
# A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12,
# the ticket is $15. Write a loop in which you ask users their age, and then
# tell them the cost of their movie ticket.
# active = True
# while active:
# 	age = input("What age are you ?\n")

# 	if age == 'quit':
# 		active = False
# 		continue
	
# 	age = int(age)
# 	ticket_charge = 0
# 	if age >= 3 and age <= 12:
# 		ticket_charge = 10
# 	elif age > 12:
# 		ticket_charge = 15

# 	print(f"Your movie ticket costs: ${ticket_charge}")
