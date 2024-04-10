"""Você está desenvolvendo um programa que verifica se um número é par ou ímpar. Para isso, você
precisa solicitar o número e verificar se ele é divisível por 2. Se o número for divisível por 2, o
programa deve informar que o número é par, caso contrário, o programa deve informar que o número
é ímpar.
"""

def par (int):
    if int % 2 == 0:
        return True
    return False

num = int(input("Diga um número e eu direi se ele é par ou ímpar.\n"))

ispar = par(num)

if ispar:
    print("É par.")
else:
    print("É ímpar;")