preço = float(input('Preço do produto: R$'))
desconto = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}!'.format(preço, desconto))