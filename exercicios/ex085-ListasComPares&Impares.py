principal = []
pares = []
impares = []
for dado in range(1, 8):
    principal.append(int(input(f'Digite o {dado}ª valor: ')))
for p in principal:
    if p % 2 == 0:
        pares.append(p)
        pares.sort()
    elif p % 2 == 1:
        impares.append(p)
        impares.sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: [{pares}]')
print(f'Os valores ímpares digitados foram: [{impares}]')
