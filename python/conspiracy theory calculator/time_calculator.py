import math

'''
Esta e uma brincadeira que fiz porque estava entediado, este código mostra os mesmos cálculos do inicial
mas com a diferença que você não precisa especificar o número de anos, eu criei uma automação para que
o código fale a melhor probabilidade no melhor período de tempo, que pode ser alterada pela variável "probabilidade".
'''

n = float(input("numero de conspiradores: "))
L = 0.0
probabilidade = 95

def calculo(n):
    t = 3.0  # o tempo não preciza ser menor que 2.5
    phi = 1-math.pow((1 - 0.01),n*t)
    L = 1-math.pow(2.7182818, -t* phi)
    
    if L < probabilidade/100:
        while L < probabilidade/100:
            t += 0.1
            phi = 1-math.pow((1 - 0.01),n*t)
            L = 1-math.pow(2.7182818, -t* phi)

        if L >= probabilidade/100 and probabilidade/100 < 1.0:
            print(f"vai demorar: {round(t, 1)} ano(s) para: {round(L*100, 2)}%")

        else:
            print(f"vai demorar: {round(t, 1)} ano(s) para: {round(L*100, 2)-0.1}%")


calculo(n)