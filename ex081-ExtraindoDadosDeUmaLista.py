valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
