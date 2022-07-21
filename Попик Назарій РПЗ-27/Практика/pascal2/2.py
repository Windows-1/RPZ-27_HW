#Напишіть Паскалем логічний вираз, який приймає значення істинне або хибне при виконанні умови:
#Трикутник з вершинами A(x1, y1), B(x2, y2), C(x3, y3) рівносторонній.

x1 = int(input('Введіть вершину А(х1):'))
y1 = int(input('Введіть вершину А(y1):'))
x2 = int(input('Введіть вершину В(х2):'))
y2 = int(input('Введіть вершину В(y2):'))
x3 = int(input('Введіть вершину С(х3):'))
y3 = int(input('Введіть вершину С(y3):'))

ab = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
ac = (x1-x3)*(x1-x3) + (y1-y3)*(y1-y3)
bc = (x2-x3)*(x2-x3) + (y2-y3)*(y2-y3)

if ab==ac==bc:
    print('Трикутник рівносторонній')
else:
    print('Трикутник не рівносторонній')