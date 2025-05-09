
def calcular_rendimento_cdi(cdi_anual, aporte_inicial, aporte_mensal, meses):
    # Conversão do CDI anual para mensal (aproximação composta)
    cdi_mensal = (1 + cdi_anual / 100) ** (1 / 12) - 1

    saldo = aporte_inicial
    total_investido = aporte_inicial

    rendimentos_por_mes = []

    for mes in range(1, meses + 1):
        rendimento = saldo * cdi_mensal
        saldo += rendimento + aporte_mensal
        total_investido += aporte_mensal
        rendimentos_por_mes.append(rendimento)

    # Imposto regressivo sobre o rendimento (simples baseado no tempo total)
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

# Exemplo de uso:
cdi = float(input("Informe o CDI anual (%): "))
inicial = float(input("Quanto vai colocar inicialmente? R$ "))
mensal = float(input("Quanto vai entrar todo mês? R$ "))
prazo = int(input("Por quantos meses você quer simular? "))

resultado = calcular_rendimento_cdi(cdi, inicial, mensal, prazo)

print("\nResultado da simulação:")
for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor}")
