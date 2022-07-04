from random import randint
n = int(randint(15, 25))

while n >= 1:
    print('Кількість сірників:', n)
    print('')
    print('Хід гравця 1')
    a = int(input('Виберіть кількість сірникив (від 1 до 3):'))
    n = n - a
    if n <= 0:
        break
    print('Кількість сірників:', n)
    print('')
    print('Хід гравця 2')
    b = int(input('Виберіть кількість сірникив (від 1 до 3):'))
    n = n - b

print('')
print('Гравець який ходив останнім - програв!')
