pratododia = 35
descontoalmoço = 10

horario = float(input("Diga o Horário"))

if horario >= 12 and horario < 13:
    print(f'O preço do prato do dia será {pratododia - descontoalmoço}')
else:
    print(f'O preço do prato do dia será {pratododia}')