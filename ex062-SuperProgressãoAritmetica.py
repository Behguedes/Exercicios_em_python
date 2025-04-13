print('=' * 40)
print('{:^40}'.format('Gerador de PA'))
print('=' * 40)
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais  != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?' ))
print('Progressão finalizada com {} termos mostrados.'.format(total))
