'''
     Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
h = math.sqrt(co * co + ca * ca)
print(f"A Hipotenusa é: {h:.2f}")
print("")