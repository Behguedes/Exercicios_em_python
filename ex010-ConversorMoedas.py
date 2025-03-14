real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Você tem R${:.2f} na carteira, e pode comprar US${:.2f} dólares!'.format(real, dolar))