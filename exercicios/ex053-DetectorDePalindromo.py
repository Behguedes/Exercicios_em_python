frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # separa a frase
junto = ''.join(palavras) # junta a frase sem espaço
inverte = junto[::-1] # inverte a frase
print('O inverso de {} é {}'.format(junto, inverte))
if junto == inverte:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')