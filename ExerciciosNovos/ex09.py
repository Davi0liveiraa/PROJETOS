'''
    Faça um programa que leia uma frase qualquer e mostre:
    Quantas vezes aparece a letra "a"
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece a última vez
'''
frase = str(input("Digite uma frase: "))
a = frase.count("a")
fraseM = frase.upper()
primeiraVez = frase.find("a")
ultimaVez = frase.rfind("a")
print("")
print("", fraseM)
print(f" A letra 'a' aparece {a} vezes nesta frase.\n Aparece pela primeira vez na posição {primeiraVez},\n E pela última vez na posição: {ultimaVez}.")
print("")