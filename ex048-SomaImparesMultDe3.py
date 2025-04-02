soma = 0
cont = 0
for c in range (1, 501, 2): # conta os numeros impares
    if c % 3 == 0:
        cont += 1 # conta mais 1
        soma += c # soma os valores
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))