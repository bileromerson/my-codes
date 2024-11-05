import random

numero_secreto = random.randint(1, 10)
tentativas = 0
acertou = False

while tentativas < 5:
    palpite = int(input("-"))

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