'''
    Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
'''
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura em metros: "))
area = largura * altura
litro = area / 2
print("")
print(f"A largura é: {largura}m.") 
print(f"A altura é: {altura}m.")
print(f"A área é: {area}m²")
print(f"A quantidade de litros de tinta necessária é: {litro}l.")