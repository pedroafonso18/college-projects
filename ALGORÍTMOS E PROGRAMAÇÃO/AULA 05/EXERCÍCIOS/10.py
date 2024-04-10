""". Ana é uma professora de matemática que está desenvolvendo um programa para calcular a média
aritmética de uma lista de números. Ela sabe que, para calcular a média, é necessário somar todos
os números da lista e dividir pelo total de números. Ana quer desenvolver um programa em Python
que possa ser utilizado por seus alunos para facilitar esse processo. Escreva um algoritmo que ajude
Ana a calcular a média aritmética de uma lista de números."""

def calcular_media(lista_numeros):
    
    total_numeros = len(lista_numeros)
    soma = sum(lista_numeros)
    media = soma / total_numeros
    return media

numeros_str = input("Digite os números separados por espaços: ")

numeros = [float(x) for x in numeros_str.split()]

media = calcular_media(numeros)

print("A média aritmética dos números é:", media)
