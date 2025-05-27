def calcular_rendimento_cdi(cdi_real, percentual_cdi, aporte_inicial, aporte_mensal, meses):
    # Conversão do CDI anual para mensal
    cdi_efetivo_anual = (cdi_real * percentual_cdi) / 100
    cdi_mensal = (1 + cdi_efetivo_anual / 100) ** (1 / 12) - 1

    saldo = aporte_inicial
    total_investido = aporte_inicial

    for mes in range(1, meses + 1):
        rendimento = saldo * cdi_mensal
        saldo += rendimento + aporte_mensal
        total_investido += aporte_mensal

    # Alíquota de IR regressiva
    if meses <= 6:
        imposto = 0.225
    elif meses <= 12:
        imposto = 0.20
    elif meses <= 24:
        imposto = 0.175
    else:
        imposto = 0.15

    lucro_bruto = saldo - total_investido
    imposto_pago = lucro_bruto * imposto
    lucro_liquido = lucro_bruto - imposto_pago
    return {
        "Total investido": round(total_investido, 2),
        "Valor final": round(saldo, 2),
        "Lucro bruto": round(lucro_bruto, 2),
        "Imposto aproximado": round(imposto_pago, 2),
        "Lucro líquido": round(lucro_liquido, 2)
    }

# Entradas do usuário

print('para escolhas com padrao, digite 0 \n caso contrario, digite o valor desejado')

cdi_real = float(input("Informe o CDI atual (padrao: 14.65%): "))

if cdi_real == 0:
    print("o cdi foi ajustado para padrao (14.65)")
    cdi_real = 14.65

percentual_cdi = float(input("Qual o % do CDI que o investimento rende (padrao: 100%)? "))
if percentual_cdi == 0:
    print("o percentual foi ajustado para padrao (100%)")
    percentual_cdi = 100
inicial = float(input("Quanto vai colocar inicialmente? R$ "))
mensal = float(input("Quanto vai entrar todo mês? R$ "))
prazo = int(input("Por quantos meses você quer simular? "))


resultado = calcular_rendimento_cdi(cdi_real, percentual_cdi, inicial, mensal, prazo)

print("\n Resultado da simulação:")
for chave, valor in resultado.items(): 
    print(f"{chave}: R$ {valor}")