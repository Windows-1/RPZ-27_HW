#1.	Даны m векторов x1=(x11, x21, x31), ..., xm=(x1m, x2m, x3m). Написать программу нахождения суммы этих векторов.

m = int(input('Введіть m: '))
a = [0, 0, 0]
b = [0, 0, 0]

for i in range(m):
    print(f'Введіть коорденати вектора {i+1}: ')
    for i in range(3):
        b[i] = int(input(f'Координата {i+1}: '))  
    for i in range(3):
        a[i] += b[i]

print(a)
