import math
print("digite 1 para ver o tempo que levara \ndigite 2 para faser calculos de probabilidade")
escolha = int(input("-"))


def escolha1(n, p):
    L = 0.0
    t = 3.0  # o tempo não preciza ser menor que 2.5
    phi = 1-math.pow((1 - 0.01),n*t)
    L = 1-math.pow(2.7182818, -t* phi)
    
    if L < p:
        while L < p:
            t += 0.1
            phi = 1-math.pow((1 - 0.01),n*t)
            L = 1-math.pow(2.7182818, -t* phi)

        if L >= p and p < 1.0:
            print(f"vai demorar: {round(t, 1)} ano(s) para: {round(L*100, 2)}%")

        else:
            print(f"vai demorar: {round(t, 1)} ano(s) para: {round(L*100, 2)-0.1}%")


def escolha2(t, n):
    phi = 1-math.pow((1 - 0.01),(n * t))
    L = 1-math.pow(2.7182818, -t* phi)
    if L >= 0.995:
        print(f"Probabilidade de exposição após {round(t, 2)} anos: {round(L*100, 2)-0.1}%")
    else:
        print(f"Probabilidade de exposição após {round(t, 2)} anos: {round(L*100, 2)}%")

if escolha == 1:
    conspiradores = float(input("numero de conspiradores: "))
    probabilidades = input("qual e a probabilidade, digite '-' para o padrão:")
    
    if probabilidades == '-':
        escolha1(conspiradores, 0.95)
    
    else:
        escolha1(conspiradores, float(probabilidades)/100)
    
elif escolha == 2:
    tempo_anos = float(input("digite o tempo em anos: "))
    numero_conspiradores = int(input("número de conspiradores: "))
    escolha2(tempo_anos, numero_conspiradores)

else:
    print("comando não reconhecido, tente novamente...")