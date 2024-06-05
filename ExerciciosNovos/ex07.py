'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = float(input("Digite o valor do ângulo: "))
anguloR = math.radians(angulo)
seno = math.sin(anguloR)
cosseno = math.cos(anguloR)
tangente = math.tan(anguloR)
print("")
print(f" O ângulo é: {angulo:.2f}\n O seno é: {seno:.3f}\n O cosseno é: {cosseno:.3f}\n A tangente é: {tangente:.3f}")
print("")