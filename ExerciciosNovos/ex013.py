'''
    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

'''

lista = []
contador = 0
for i in range(1, 9):
    contador += 1
    lista2 = str(input("Digite {}° produto: ".format(contador)))
    var = lista.append(lista2)
print(lista)