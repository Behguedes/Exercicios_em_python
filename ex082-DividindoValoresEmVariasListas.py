num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}!')
print(f'A lista de pares é {pares}!')
print(f'A lista de ímpares é {impares}!')
