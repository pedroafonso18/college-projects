"""Você está desenvolvendo um programa para calcular a distância percorrida por um objeto em um
movimento uniformemente acelerado. O usuário deve informar a velocidade inicial, a aceleração e o
tempo de deslocamento. Escreva um algoritmo que calcule e imprima a distância percorrida pelo
objeto."""

vel_inicial = float(input("Diga a velocidade inicial:\n"))
aceleracao = float(input("Diga a aceleração:\n"))
tempo = float(input("Diga o tempo de deslocamento:\n"))

distancia = vel_inicial * tempo + 0.5 * aceleracao * tempo ** 2

print(f"A distância percorrida pelo objeto é de {distancia:.2f} metros.")