"""Cálculo de média: Escreva um programa que leia três notas e calcule a média do aluno. Se a
média for maior ou igual a 7, exiba a mensagem "Aprovado". Caso contrário, exiba
"Reprovado"."""

nota01 = float(input("Diga a Nota do primeiro aluno:\n"))
nota02 = float(input("\nDiga a Nota do segundo aluno:\n"))
nota03 = float(input("\nDiga a nota do terceiro aluno:\n"))

media = (nota01 + nota02 + nota03) / 3

if media >= 7:
    print(f"\nAprovado com nota {media}")
else:
    print(f"\nReprovado com nota {media}")
