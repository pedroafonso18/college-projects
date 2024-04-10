"""João é um médico que trabalha em uma clínica especializada em saúde preventiva. Ele está
desenvolvendo um programa para calcular o IMC (Índice de Massa Corporal) de seus pacientes. O
IMC é uma medida que relaciona o peso e a altura de uma pessoa e é utilizada para verificar se ela
está com o peso ideal. João sabe que, para calcular o IMC, ele precisa da altura e do peso do
paciente. Escreva um algoritmo em Python que ajude João a calcular o IMC de seus pacientes.
"""

peso = float(input("Diga o seu peso em kilos:\n"))
altura = float(input("Diga sua altura em metros:\n"))

imc = peso / (altura ** 2)

print(f"O resultado do seu imc é de {imc:.2f}")