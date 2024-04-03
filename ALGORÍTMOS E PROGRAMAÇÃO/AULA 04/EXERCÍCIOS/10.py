""" Verificação de vogal: Escreva um programa que leia uma letra e verifique se ela é uma vogal
ou não. Se for uma vogal, exiba a mensagem "A letra é uma vogal". Caso contrário, exiba "A
letra é uma consoante"."""

def isVowel(ch):
    str = "aeiouAEIOU"
    return (str.find(ch) != -1)

letra = str(input("Diga uma letra!\n"))
letra = isVowel(letra)

if letra == True:
    print("É uma vogal!")
else:
    print("É uma consoante!")