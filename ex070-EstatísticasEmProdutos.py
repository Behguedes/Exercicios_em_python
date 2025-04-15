total = totmil = menorPreço = 0
nomeBarato = ''
while True:
    print('-' * 40)
    print('{:^40}'.format('LOJA SUPER BARATÃO') )
    print('-' * 40)
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço >= 1000:
        totmil += 1
    if total == preço or preço < menorPreço:
        menorPreço = preço
        nomeBarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi RS{total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {nomeBarato} que custa R${menorPreço:.2f}.')
