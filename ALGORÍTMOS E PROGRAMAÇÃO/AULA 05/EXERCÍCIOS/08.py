"""Maria é uma estudante de física que está desenvolvendo um programa para converter uma
temperatura de Celsius para Fahrenheit. Ela sabe que muitas vezes precisa realizar essa conversão
em seus estudos, mas a fórmula matemática pode ser confusa. Por isso, ela está desenvolvendo um
programa em Python que simplifica esse processo. Escreva um algoritmo que ajude Maria a
converter uma temperatura de Celsius para Fahrenheit."""

temperatura = int(input("Diga qual tipo de conversão deseja fazer:\nCelsius para Fahrenheit :(1)\nFahrenheit para Celsius :(2)\n"))

if temperatura == 1:
    celsius = float(input("Diga o valor dos graus em Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"O valor destes graus em fahrenheit é de {fahrenheit:.2f} graus.")
elif temperatura == 2:
    fahrenheit = float(input("Diga o valor dos graus em Fahrenheit:\n"))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"O valor destes graus em celsius é de {celsius:.2f} graus.")
else:
    print("Favor escolher uma opção válida.")