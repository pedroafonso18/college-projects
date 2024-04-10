"""Você está desenvolvendo um programa para calcular a corrente elétrica em um circuito elétrico. O
usuário deve informar a resistência elétrica e a tensão elétrica do circuito. Escreva um algoritmo que
calcule e imprima a corrente elétrica do circuito, de acordo com a lei de Ohm"""

resistencia = float(input("Diga a resistência do circuito:\n"))

tensao = float(input("Diga a tensão elétrica do circuito:\n"))

corrente = tensao / resistencia
print(f" A corrente é de {corrente}")