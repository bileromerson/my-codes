import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

while tentativas < 4:
    palpite = int(input(f"digite um numero de 1 a 10 - "))

    if palpite == numero_secreto:    
        acertou = True
        print("coreto")

    elif palpite < numero_secreto:
        print(f"{palpite} < numero")

    else:
        print(f"{palpite} > numero")
    tentativas += 1
    
    if  acertou == True:
        tentativas = 6

else:
  print("suas tentativas acabaram")