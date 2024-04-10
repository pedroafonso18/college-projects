"""Você está desenvolvendo um programa para classificar triângulos de acordo com as medidas de
seus lados. O usuário deve informar as medidas dos três lados do triângulo. Escreva um algoritmo
que determine e imprima se o triângulo é equilátero, isósceles ou escaleno."""

lado1 = float(input("Diga a medida do lado 1 do triângulo:\n"))
lado2 = float(input("Diga a medida do lado 2 do triângulo:\n"))
lado3 = float(input("Diga a medida do lado 3 do triângulo:\n"))

if lado1 == lado2 == lado3:
    print("\nSeu triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("\nSeu triângulo é isósceles")
else:
    print("\nSeu triângulo é escaleno.")