'''
    Crie um programa que leia o nome completo de uma pessoa:
        O nome com todas as letras maiúsculas
        O nome com todas minúsculas
        Quantas letras ao todo sem considerar espaços
        Quantas letras tem o primeiro nome:
'''
nome = str(input("Digite seu nome completo: "))
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
lse = len(nome.strip())
lpn = len(nome.split()[0])
print("")
print(f" Nome em maiúsculo: {nome_maiusculo}\n Nome minúsculo: {nome_minusculo}\n Quantidade de letras sem espaço: {lse}\n Quantidade de letras do primeiro nome: {lpn}")
print("")