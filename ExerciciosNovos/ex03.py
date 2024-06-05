'''
    Aluguel de carros:

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

    Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
'''
km = float(input("Digite quantos Kilômetros percorridos: "))
dias = float(input("Digite quantos dias de aluguel: "))
preço = (60 * dias) + (0.15 * km)
print("")
print(f"O carro percorreu: {km:.0f}kilômentros.")
print(f"Por um período de {dias:.0f}dias.")
print(f"O preço calculado é: R${preço:.2f}.")
print("")