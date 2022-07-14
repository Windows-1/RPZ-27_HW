#14. Даны две матрицы А и В. Написать программу, меняющую местами максимальные элементы этих матриц. 
# Нахождение максимального элемента матрицы оформить в виде процедуры.
from random import randint

def matrix_max(matrix) :
    amax = matrix[0][0]
    n = len(matrix)
    for i in range(n) :
        if max(matrix[i]) > amax :
            amax = max(matrix[i])
    return amax
    
def matrix_print(a, b) :
    for i in a :
        print(*i)
    print()
    for i in b :
        print(*i)
    print()
 
print('Кількість рядків у першій матриці: ')
aa = int(input())
print('Кількість елементів в рядку: ')
ab = int(input())
print('Кількість рядків у другій матриці: ')
ba = int(input())
print('Кількість елементів в рядку: ')
bb = int(input())
 
a = [[randint(1,50) for i in range(ab)] for j in range(aa)]
b = [[randint(1,50) for i in range(bb)] for j in range(ba)]
 
matrix_print(a,b)
 
amax = matrix_max(a)
bmax = matrix_max(b)
 
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = bmax if a[i][j] == amax else a[i][j]
for i in range(len(b)) :
    for j in range(len(b[i])) :
        b[i][j] = amax if b[i][j] == bmax else b[i][j]
    
matrix_print(a,b)