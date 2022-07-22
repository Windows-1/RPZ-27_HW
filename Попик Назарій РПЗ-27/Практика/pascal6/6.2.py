#Даны две матрицы А(nxn) и B(nxn). Написать программу получения коммутатора АВ этих матриц.

from random import randint

def matrix_print(a):
    for i in a:
        print(*i)
    print()

aa = int(input('Кількість рядків у першій матриці: ' ))
a1 = int(input('Кількість елементів в рядку: '))
b1 = int(input('Кількість рядків у другій матриці: '))
bb = int(input('Кількість елементів в рядку: '))
 
a = [[randint(1,10) for i in range(a1)] for j in range(aa)]
b = [[randint(1,10) for i in range(bb)] for j in range(b1)]

matrix_print(a)
matrix_print(b)

length = len(a) 
ab = [[0 for i in range(length)] for i in range(length)]
for i in range(length):
    for j in range(length):
        for k in range(length):
            ab[i][j] += a[i][k] * b[k][j]

length = len(b) 
ba = [[0 for i in range(length)] for i in range(length)]
for i in range(length):
    for j in range(length):
        for k in range(length):
            ba[i][j] += b[i][k] * a[k][j]

length = len(ab) 
for i in range(length):
    for j in range(length):
        ab[i][j]-=ba[i][j]

matrix_print(ab)