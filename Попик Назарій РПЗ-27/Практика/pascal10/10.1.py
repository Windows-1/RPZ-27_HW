#10.1 варіант 14. Дан текст-строка, состоящая из строчных латинских букв, цифр и знаков. 
# Получить новый текст, состоящий только из цифр.


string = input('Введіть текст:')
numbers = []

for i in string:
    if i.isdigit():
        numbers.append(i)
print(numbers)