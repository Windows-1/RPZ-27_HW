# 5.1 варіант 13. Дана степінь натурального числа A. Знайти її показник.
import sys

try:
    a = int(input('Введіть початкове число:'))
    b = int(input('Введіть результат:'))
    n = a
    count = 0
    
    if b==1:
        print()
    elif b<a:
        sys.exit(0)
    elif a>=2 and b>=2:
        count+=1
        while n!=b:
            n = n * a
            if n>b:
                sys.exit(0)
            count+=1
    else:
        sys.exit(0)
    print('\n''Показник степіня', count)
except:
    print('\n''Перевірте правельність написання числа та результату')
