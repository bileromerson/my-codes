import random

cara = 50
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)
lista = []

if num1 <= cara:
    lista.append('Cara')
else:
    lista.append('coroa')

if num2 <= cara:
    lista.append('Cara')
else:
    lista.append('Coroa')

if num3 <= cara:
    lista.append('cara')
else:
    lista.append('coroa')

print(lista)

if lista.count('Cara') == 2:
    print('Você ganhou')
elif lista.count('Cara') == 3:
    print('Você ganhou')

else:
    print('Você perdeu')