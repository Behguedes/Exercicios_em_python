print('{:=^40}'.format(' LOJAS BEHGUEDES '))
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = compras - (compras * 10 / 100)
elif opção == 2:
    total = compras - (compras * 5 / 100)
elif opção == 3:
    total = compras
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcelas))
elif opção == 4:
    total = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    juros = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, juros))
else:
    total = compras
    print('{}OPÇÃO INVÁLIDA de pagamento. Tente novamente!{}'.format('\033[31m', '\033[m'))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compras, total))


