# 3.2 варіант 14. Відомо, що з чотирьох чисел a1, a2, a3, a4 одне відрізняється від
# інших трьома рівними між собою, присвоїти номер цього числа змінній n.

numbers = [7, 7, 7, 3]
n = 0


if numbers[1]==numbers[2] and numbers[2]==numbers[3]:
    n = 1
elif numbers[0]==numbers[2] and numbers[2]==numbers[3]:
    n = 2
elif numbers[0]==numbers[1] and numbers[1]==numbers[3]:
    n = 3
else: 
    n = 4
print('Номер числа:', n)