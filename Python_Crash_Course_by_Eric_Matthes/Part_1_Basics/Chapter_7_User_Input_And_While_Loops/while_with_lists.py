# 7-8. Deli:
# Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders 	= [
	'Pastrami',
	'Club Sandwich',
	'BLT',
	'Pastrami',
	'Reuben',
	'Pastrami',
	'Philly Cheesesteak',
	'Pastrami',
	'Cubano',
	'Pastrami',
]
finished_sandwiches = []
pastrami 			= 'pastrami'

# 7-9. No Pastrami:
# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

print("\nWe've ran out of pastrami")

while pastrami in sandwich_orders:
	sandwich_orders.remove(pastrami)

while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print(f"I made you a {sandwich} sandwich")
	finished_sandwiches.append(sandwich)

print("-------- Finished Sandwiches --------")
for sandwich in finished_sandwiches:
	print(f"• {sandwich}\n")
