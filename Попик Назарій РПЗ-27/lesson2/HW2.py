from random import randint
amount = int(input('Введіть кількість чисел:'))
numbers = []

for i in range(amount):
    numbers.append(randint(-100, 100))
print(numbers)

i = 0
summinus = 0
sumplus = 0
while i < len(numbers):
    if numbers[i] < 0:
        summinus = summinus + numbers[i]
    else:
        sumplus = sumplus + numbers[i]
    i = i + 1

print(abs(summinus), 'Модуль суми від`ємних')
print(abs(sumplus), 'Модуль суми невід`ємних')
if abs(sumplus) > abs(summinus):
    print(' Модуль суми невід`ємних більший')
elif abs(sumplus) < abs(summinus):
    print('Модуль суми від`ємних більший')
else:
    print('Модулі сум чисел однакові')
