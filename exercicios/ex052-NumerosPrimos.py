num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0: # verifica se é numero primmo
        print('\033[32m', end=' ') # coloca cor
        tot += 1
    else:
        print('\033[31m', end=' ') # coloca cor
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')