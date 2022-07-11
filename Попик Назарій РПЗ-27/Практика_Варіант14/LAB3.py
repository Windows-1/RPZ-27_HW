from random import randint

amount = 8
numbers = []

for i in range(amount):
    numbers.append(randint(-50, 50))

print(numbers)
print(' ')
print(numbers[0], numbers[1], numbers[2])
print(numbers[3], numbers[4])
print(numbers[5], numbers[6], numbers[7])
