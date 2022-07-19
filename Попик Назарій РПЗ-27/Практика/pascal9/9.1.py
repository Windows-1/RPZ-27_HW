#14. Составить программу, выводящую на экран "Телефонный справочник" (Ф. И. О., адрес, номер телефона).

amount = int(input('Введіть кількість пунктів у довіднику:'))

name = []
address = []
pnumber = []

for i in range(amount):
    name.append(input('Введіть ПІБ:'))
    address.append(input('Введіть адресу:'))
    pnumber.append(input('Введіть номер телефону:'))

print('')
for i in range(amount):
    print(name[i], address[i], pnumber[i])
    i +=1