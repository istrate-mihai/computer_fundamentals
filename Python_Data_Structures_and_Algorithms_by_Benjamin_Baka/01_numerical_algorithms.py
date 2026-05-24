# --------------------------------------------------------------
n1 = int(input('Enter a number: '))
s = 0

# Sum of the digits of a number
while n1 != 0:
    c = n1 % 10
    s += c
    n1 //= 10

# --------------------------------------------------------------
print('The sum of the digits is:', s)

n2 = int(input('Enter a number: '))

# Count of the digits of a number
count = 0
while n2 != 0:
    count += 1
    n2 //=10

# --------------------------------------------------------------
print('The count of the digits is:', count)

n3 = int(input('Enter a number: '))

# Reverse of the digits of a number
reverse = 0
while n3 != 0:
    reverse = reverse * 10 + n3 % 10
    n3 //= 10

# --------------------------------------------------------------
print('The reverse of the digits is:', reverse)

# --------------------------------------------------------------
# Determine if a number is prime or not
# Edge cases:
# n < 2: not prime
# Mathematically no number can have a divisor greater than half of itself
n4 = int(input('Enter a number: '))
d = 2
is_prime = 1

while (d <= (n4 // 2)) and is_prime == 1:
    if n4 % d == 0:
        is_prime = 0
    else:
        d += 1

if is_prime == 1:
    print('The number is prime.')
else:
    print('The number is not prime.')

# --------------------------------------------------------------
# Determine the prime factors decomposition
n = int(input('Enter a number: '))
d = 2

while n > 1:
    p = 0

    while (n % d) == 0:
        p += 1
        n = n // d

    if p != 0:
        print('%d ^ %d' % (d, p))
    d += 1

# --------------------------------------------------------------
# Determine the greatest common divisor of two numbers
# Repeated subtractions method
a    = int(input('Enter number 1: '))
b    = int(input('Enter number 2: '))
num1 = a
num2 = b

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print('The greatest common divisor of %d and %d is %d' % (num1, num2, a))

# --------------------------------------------------------------
# Determine smallest common multiple
# x * y = cmmdc(x, y) * cmmmc(x, y)
n1 = int(input('Enter number 1: '))
n2 = int(input('Enter number 2: '))
x  = n1
y  = n2

while n1 != n2:
    if n1 > n2:
        n1 = n1 - n2
    else:
        n2 = n2 - n1

print('The smallest common multiple of %d and %d is %d' % (x, y, (x * y / n1)))
