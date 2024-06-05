'''
    As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento.

'''
salario = float(input("Digite seu salário: "))
if salario <= 280:
    porcentagem = ((20 * salario) / 100)
    salarioAjustado = salario + porcentagem
    print(f"O salário era: {salario:.2f}\n Aumento foi de 20%!\n Valor total de {porcentagem}\n O novo salário é: R${salarioAjustado:.2f}")
elif salario <= 700:
    porcentagem2 = ((15 * salario) / 100)
    salarioAjustado = salario + porcentagem2
    print(f"O salário era: {salario:.2f}\n Aumento foi de 20%!\n Valor total de {porcentagem2}\n O novo salário é: R${salarioAjustado:.2f}")
elif salario <= 1500:
    porcentagem3 = ((10 * salario) / 100)
    salarioAjustado = salario + porcentagem3
    print(f"O salário era: {salario:.2f}\n Aumento foi de 20%!\n Valor total de {porcentagem3}\n O novo salário é: R${salarioAjustado:.2f}")
elif salario >= 1501:
     porcentagem4 = ((5 * salario) / 100)
     salarioAjustado = salario + porcentagem4
     print(f"O salário era: {salario:.2f}\n Aumento foi de 20%!\n Valor total de {porcentagem4}\n O novo salário é: R${salarioAjustado:.2f}")
else: 
    print("Resposta inválida.")

