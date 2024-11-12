import math

n = float(input("numero de conspiradores: "))
L = 0.0

def calculo(n):
    t = 0.5

    phi = 1-math.pow((1 - 0.01),n*t)
    L = 1-math.pow(2.7182818, -t* phi)

    if L < 0.95:

        while L < 0.95:
            
            phi = 1-math.pow((1 - 0.01),n*t)
            L = 1-math.pow(2.7182818, -t* phi)
            t += 0.05

            if L >= 0.95:

                print(f"vai demorar: {round(t, 2)} ano(s) para: {round(L*100, 2)}%")


calculo(n)