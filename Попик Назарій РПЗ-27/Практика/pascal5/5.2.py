# 5.2 варіант 14. Дано таблицю цілих чисел a1, a2, ..., an та число с. Розширити цю таблицю до таблиці a1<= a2<= ...<= an+1, включивши в неї число с.

from random import randint

amount = int(input('Введіть кількість чисел у таблиці:'))
numbers = []
c = int(input('Введіть число С:'))

numbers.append(c)

for i in range(amount):
    numbers.append(randint(-100, 100))
print('Невідсортований список:', numbers)

numbers = sorted(numbers)
print('Відсортований список:', numbers)