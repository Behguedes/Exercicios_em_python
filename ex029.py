veloz = int(input('Digite a volocidade: '))
if veloz > 80:
    print('MULTADO!')
    print('A multa vai custar R$7,00 por cada Km acima do limite, valor {}!'.format(veloz*7))
