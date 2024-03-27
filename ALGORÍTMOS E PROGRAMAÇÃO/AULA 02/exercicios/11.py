preço = float(input("DIGA UM NÚMERO PARA O PREÇO: "))
porcentagem = float(input("DIGA A PORCENTAGEM DO DESCONTO: "))

conta = preço / 100
conta = conta * porcentagem
preço = preço - conta


print(f"O PREÇO COM DESCONTO É:  ",preço)