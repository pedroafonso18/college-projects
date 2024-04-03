"""Cálculo de desconto: Escreva um programa que leia o valor de um produto e calcule o valor
com desconto de 10%. Se o valor do produto for maior que R$ 50,00, aplique um desconto
adicional de 5%. Exiba o valor final com desconto."""

valor = float(input("Diga o valor do produto:\n"))

if valor >= 50:
    valor = (valor / 100)
    valor = valor * 85
    print(f'O preço ficou em {valor}')
else:
    valor = (valor / 100)
    valor = valor * 90
    print(f'O preço ficou em {valor}')