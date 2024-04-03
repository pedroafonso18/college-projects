"""Verificação de idade para votação: Escreva um programa que peça a idade do usuário e
verifique se ele pode votar ou não. Se a idade for igual ou superior a 16 anos, exiba a
mensagem "Você pode votar". Caso contrário, exiba "Você ainda não pode votar"."""

idade = int(input("Diga sua idade:\n"))
if idade >= 16:
    print("Já pode votar.")
else:
    print("Não pode votar.")