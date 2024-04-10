"""Pedro é um estudante de matemática que está desenvolvendo um programa para calcular o volume
de uma esfera. Ele sabe que o cálculo pode ser um pouco complicado, mas também é muito
importante em diversas áreas da matemática e da física. Pedro está animado em desenvolver esse
programa em Python para ajudar outros estudantes a entenderem melhor a fórmula. Escreva um
algoritmo que ajude Pedro a calcular o volume de uma esfera."""

from math import pi

raio = float(input("Digite o valor do raio da esfera:\n"))

volume = (4/3) * pi * raio ** 3

print(f"O volume da esfera é de {volume:.2f}")