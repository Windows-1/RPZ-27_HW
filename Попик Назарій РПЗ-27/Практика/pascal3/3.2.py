# 3.2 варіант 14. Відомо, що з чотирьох чисел a1, a2, a3, a4 одне відрізняється від
# інших трьома рівними між собою, присвоїти номер цього числа змінній n.
import sys

numbers = []
n = 0

for i in range(4):
    numbers.append(input('Введінь число:'))

if numbers[1]==numbers[2]==numbers[3]:
    n = 1
elif numbers[0]==numbers[2]==numbers[3]:
    n = 2
elif numbers[0]==numbers[1]==numbers[3]:
    n = 3
else: 
    n = 4

count = 0
if n!=1:
    a = numbers[0]
else:
    a = numbers[1]
for i in numbers:
    if i == a:
        count+=1
if count!=3:
    print('Два чи більше чисел різні або всі числа однакові')
    sys.exit(0)

print('Номер числа:', n)
