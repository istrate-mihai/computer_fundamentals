pizza_list = ['Margherita', 'Pepperoni', 'Quattro Stagioni']
for pizza in pizza_list:
    print("I really love " + pizza + " pizza!")

print("I really love pizza")

animal_list = ["dog", "cat", "hamster"]
for animal in animal_list:
    print("A " + animal + " would make a great pet")

print("Any of these animals would make a great pet!")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
for number in range(1, 21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop
# it by pressing ctrl-C or by closing the output window.)
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)
    if number == 10000:
        break

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
for i in range(1, 21, 2):
    print(i)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
three_multiple_list = list(range(3, 31, 3))
for number in three_multiple_list:
    print(number)

# # 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes
# (that is, the cube of each integer from 1 through 10), and use a for loop to
# print out the value of each cube.
cube_list = list()
for i in range(1, 11):
    cube_list.append(i ** 3)

for cube in cube_list:
    print(cube)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# •	 Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
# •	 Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
print("The first three items in the list are: ")
print(cubes[:3])
print("Three items from the middle of the list are: ")
middle_index = len(cubes) // 2
print(cubes[(middle_index - 1):(middle_index + 2)])
print("The last three items in the list are: ")
print(cubes[-3:])

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
friend_pizza = pizza_list[:]

pizza_list.append("Diavola")
friend_pizza.append("Quattro Formagi")

print("My favorite pizzas are: ")
for pizza in pizza_list:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizza:
    print(pizza)
