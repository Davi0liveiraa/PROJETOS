'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''
metros = float(input("Digite o valor em metros: "))
cm = metros * 100
mm = metros * 1000
print("")
print(f" O valor é: {metros}m\n Convertida para cm: {cm}cm\n Convertida para ml: {mm}mm.")
print("")