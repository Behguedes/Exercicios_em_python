# Calculando Fatorial com a biblioteca
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

# Calculando com while
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n # c recebe o valor digitado
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
print('{}.'.format(f))