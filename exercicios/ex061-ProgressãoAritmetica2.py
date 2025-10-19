print('=' * 40)
print('{:^40}'.format('Gerador de PA'))
print('=' * 40)
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
