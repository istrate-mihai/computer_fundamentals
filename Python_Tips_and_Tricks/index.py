from datetime import datetime

time_now = datetime.now().strftime("%H:%M:%S")
# print(f'The time now is {time_now}')

from collections import Counter

list_1 		= ['John','Kelly', 'Peter', 'Moses', 'Peter']
count_peter = Counter(list_1).get('Peter')

# print(
#     f'Peter appears in the list '
#     f'{count_peter} times.'
# )

x = [12, 45, 67, 89, 34, 67, 13]

# print(min(x))
# print(enumerate(x, start = 0))

# for i in enumerate(x, start = 0):
#     print(i)

# print(max(enumerate(x, start = 0), key = lambda y : y[1]))

a = [10989767, 9876780, 9908763]
# b = ['{:,}'.format(num) for num in a]
# b = [f'{num:,}' for num in a]
# print(b)

# import heapq
# results = [12, 34, 67, 98, 90, 68, 55, 54, 64, 35]
# print(heapq.nlargest(5, results))
# print(heapq.nsmallest(5, results))

a = 'fecklessness'
# print(Counter(a).most_common(1))

from operator import itemgetter
names = [('Ben','Jones'), ('Peter','Parker'), ('Kelly','Isa')]

# Sort by first name
print(sorted(names, key=itemgetter(0)))
