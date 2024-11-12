import math

'''
Esta e uma brincadeira que fiz porque estava entediado, este código mostra os mesmos cálculos do inicial
mas com a diferença que você não precisa especificar o número de anos, eu criei uma automação para que
o código fale a melhor probabilidade no melhor período de tempo, que pode ser alterada pela variável "probabilidade",
lembre-se que as probabilidades devem ser divididas por 100 para que o código funcione corretamente
'''

n = float(input("numero de conspiradores: "))
L = 0.0
probabilidade = 0.95

def calculo(n):
    t = 0.5

    phi = 1-math.pow((1 - 0.01),n*t)
    L = 1-math.pow(2.7182818, -t* phi)

    if L < probabilidade:

        while L < probabilidade:
            
            phi = 1-math.pow((1 - 0.01),n*t)
            L = 1-math.pow(2.7182818, -t* phi)
            t += 0.05

            if L >= probabilidade:

                print(f"vai demorar: {round(t, 2)} ano(s) para: {round(L*100, 2)}%")


calculo(n)