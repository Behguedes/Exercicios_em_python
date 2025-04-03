frase = str(input('Digite uma frase: ')).strip().upper()
inverte = frase[::-1] # inverte a frase
print('o inverso de {} é {}'.format(frase, inverte))
if frase == inverte:
    print('Temos um palíndromo')
else:
    print('A frase digitada NÃO é um palíndromo!')