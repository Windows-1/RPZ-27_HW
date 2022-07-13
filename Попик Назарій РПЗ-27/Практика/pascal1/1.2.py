#14.	По довжинам двох сторін трикутника і кута між ними знайдіть довжину третьої сторони і площу трикутника.

import math

triangle_side_1 = float(input('Введіть першу сторону трикутника:'))
triangle_side_2 = float(input('Введіть другу сторону трикутника:'))
angle = float(input('Введіть кут:'))
angle = angle * math.pi / 180

triangle_side_3 = (triangle_side_1**2 + triangle_side_2**2 - 2 * triangle_side_1 * triangle_side_2 * math.cos(angle))**0.5
p = (triangle_side_1 + triangle_side_2 + triangle_side_3)/2
s = (p * (p - triangle_side_1) * (p - triangle_side_2) * (p - triangle_side_3)) ** 0.5

print('Третя сторона трикутника=', triangle_side_3, 'Площа трикутника=', s)