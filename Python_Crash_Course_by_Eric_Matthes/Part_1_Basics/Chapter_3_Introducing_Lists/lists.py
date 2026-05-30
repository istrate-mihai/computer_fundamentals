letters = ['a', 'b', 'c']
print(letters[0])
print(letters[1])
print(letters[2])

guest_list = ['alex', 'dana', 'mihai']
guest_list.insert(0, 'ionut')
guest_list.insert(len(guest_list) // 2, 'elena')
guest_list.append('radu')
print(guest_list)
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()
print(guest_list)

del guest_list[1]
del guest_list[0]
print(guest_list)

cities = ['london', 'chicago', 'bucharest', 'hong kong', 'tokyo']
print(cities)
print(sorted(cities))
print(cities)
print(sorted(cities, reverse=True))
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
