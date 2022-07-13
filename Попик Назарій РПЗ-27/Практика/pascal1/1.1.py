import math

x = float(input('Bведіть х:'))
y = float(input('Bведіть y:'))
z = float(input('Bведіть z:'))

print(x,y,z)

a = (math.sqrt(math.fabs(x - 1)) - math.sqrt(math.fabs(y)))/(1+2*(x**2)+math.cos(x))
b = (x**2)*(math.atan(z) + y)

print('a=', a, 'b=', b)
