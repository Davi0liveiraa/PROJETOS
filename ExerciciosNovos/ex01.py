'''
     Crie um programa que leia quanto dinheiro em reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''
real = float(input("Quanto reais você tem na carteira? "))
dolar = real * 5.17
print(f"Você tem R${real:.2F} reais na carteira, e pode comprar US${dolar:.2f} dólares.")