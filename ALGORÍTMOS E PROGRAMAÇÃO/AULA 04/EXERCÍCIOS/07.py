"""Verificação de senha: Escreva um programa que peça ao usuário uma senha e verifique se
ela é válida ou não. Considere uma senha válida aquela que possui pelo menos 8
caracteres, contendo pelo menos uma letra maiúscula e um número. Se a senha for válida,
exiba a mensagem "Senha válida". Caso contrário, exiba "Senha inválida"."""

senha = input("Digite sua senha:\n")

numchar = len(senha)

upper = any(ele.isupper() for ele in senha)

number = any(chr.isdigit() for chr in senha)

if numchar >= 8 and upper == True and number == True:
    print("Sua senha é válida!")
else:
    print("Sua senha é inválida!")