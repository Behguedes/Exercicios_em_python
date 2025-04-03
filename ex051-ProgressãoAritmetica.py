print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (10 - 1) * razão
for pa in range(termo, decimo + razão, razão):
    print('{}'.format(pa), end=' -> ')
print('ACABOU')