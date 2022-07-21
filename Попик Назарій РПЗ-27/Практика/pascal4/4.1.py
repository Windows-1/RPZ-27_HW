#Створення програми для обчислення значення функції.
 
import math

x = float(input('Введіть x(від 5 до 25): '))

if x >= 5 and x < 10:
    y = 1 - math.sin(x)
    print(y)
elif x >= 10 and x < 15:
    y = 1/2 * (1 + math.cos(x))
    print(y)
elif x >= 15 and x < 20:
    y = 1/3 * math.tan(x)
    print(y)
elif x >= 20 and x < 25:
    y = (1/math.tan(x))**3
    print(y)
else:
    print('Перевірте чи ви ввели правельне число та спробуйте ще раз.')