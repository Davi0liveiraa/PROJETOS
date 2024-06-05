'''
    Escreva um programa para aprovar o empréstimo bancário
    para a compra de uma casa
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos
    anos ele vai pagar

    Calcule o valor da prestação mensal,
    sabendo que ela não pode exceder 30% do salário
    ou então o empréstimo será negado
'''

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = float(input("Em quantos anos você realizará o pagamento? "))
mensalidade = casa / (anos*12)
minimo = (salario * 30) / 100
if mensalidade > minimo:
    print("Empréstimo aprovado!")
elif mensalidade > minimo:
    print("Empréstimo recusado!")


