"""Verificação de número positivo: Escreva um programa que leia um número e verifique se ele
é positivo ou negativo. Se for positivo, exiba a mensagem "O número é positivo". Caso
contrário, exiba "O número é negativo"""

num01 = int(input("Digite um número:\n"))

if num01 > 0:
    print("O número é positivo!")
elif num01 == 0:
    print("0 Não vale.")
else:
    print("O número é negativo!")