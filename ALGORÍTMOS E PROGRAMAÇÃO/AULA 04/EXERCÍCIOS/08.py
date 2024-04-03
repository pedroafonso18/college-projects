"""Cálculo de imposto: Escreva um programa que leia o salário de um funcionário e calcule o
valor do imposto a ser pago, considerando as seguintes faixas salariais: até R$ 1.000,00,
isento de imposto; de R$ 1.000,00 a R$ 2.000,00, 10% de imposto; acima de R$ 2.000,00,
20% de imposto."""

salario = float(input("Digite seu salário:\n"))

if salario < 1000:
    print("Você é isento de pagar imposto.")
elif salario >= 1000 and salario <= 2000:
    salario = salario / 100
    salario = salario * 10
    print(f"Você deve pagar o imposto de {salario} R$")
elif salario > 2000:
    salario = salario / 100
    salario = salario * 20
    print(f"Você deve pagar o imposto de {salario} R$")