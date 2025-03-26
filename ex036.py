casa = float(input('Valor da casa? R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * 30 / 100
prestação = casa / (anos * 12)

print ('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}!'.format(casa, anos, prestação))

if prestação <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

