triangles_number = int(input('Кількість трикутників: '))
triangle_sides = []
triangle_square = []

i = 0

while i < triangles_number:
    triangle_side = int(input(f'Сторона трикутника {i + 1}: '))
    triangle_sides.append(triangle_side)
    i += 1

i = 0
while i < len(triangle_sides):
    p = (3*triangle_sides[i])/2
    s = (p * (p - triangle_sides[i]) * (p - triangle_sides[i]) * (p - triangle_sides[i])) ** 0.5
    triangle_square.append(s)
    print(f'Сторона трикутника {i + 1}:', triangle_sides[i])
    print(f'Напівпериметр трикутника {i + 1}:', p)
    print(f'Площа трикутника: {i + 1}', s)
    i += 1

print(sum(triangle_square), 'Сума площі трикутників')
