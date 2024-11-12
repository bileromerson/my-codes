import math

'''
este e um codico simples para você brincar com as probabilidades,
estes calculos foram desenvolvidos por Grimes com o objetivo de
prever quando uma conspiração iria ser revelada. De acordo com Grimes
ele comparou 3 conspirações reais como a base de dados dele.
Come este codico você pode prever quando irão derubar uma conspiracão
de acordo com o numero de envolvidos.
saiba mais em:
https://youtu.be/4g8KhkInwyk?list=LL
'''
# Resultado deve ser maior que 0.95

def probabilidade_exposicao(t, n):
    # n número total de pessoas que têm conhecimento da conspiração
    # Fórmula de Grimes para a probabilidade de exposição

    phi = 1-math.pow((1 - 0.01),(n * t))

    L = 1-math.pow(2.7182818, -t* phi)
    print(f"Probabilidade de exposição após {t} anos: {L}")

tempo_anos = float(input("digite o tempo em anos: "))       # anos para considerar
numero_conspiradores = int(input("número de conspiradores: "))  # quem supostamente não pode revelar o segredo
probabilidade = probabilidade_exposicao(tempo_anos, numero_conspiradores)

