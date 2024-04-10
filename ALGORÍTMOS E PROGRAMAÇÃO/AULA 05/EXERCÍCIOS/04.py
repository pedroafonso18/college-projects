""" Você está desenvolvendo um programa para calcular a altura máxima e o tempo de queda de um
objeto em um lançamento vertical. O usuário deve informar a altura inicial do objeto. Assuma que a
aceleração da gravidade é igual a 9,81 m/s². Escreva um algoritmo que calcule e imprima a altura
máxima e o tempo de queda do objeto."""
from math import sqrt

alturainicial = float(input("Diga a altura inicial do objeto:\n"))

gravidade = 9.81

tempo = sqrt(2 * alturainicial / gravidade)

alturamaxima = alturainicial + (0.5 * gravidade * tempo ** 2)

print(f"A altura máxima é de {alturamaxima} metros.\n")
print(f"O tempo de queda é de {tempo:.2f} segundos.")