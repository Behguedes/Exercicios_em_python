cont = ('zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <=20:
        break
    if num < -1 or num > 20:
        print('Tente novamente.', end=' ')
        num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {cont[num]}')
while True:
        res = str(input('Quer continuar? [s/n] ')).upper().strip()[0]
        if res == 'S':
            num = int(input('Digite um número entre 0 e 20: '))
            print(f'Você digitou o número {cont[num]}')
        if res == 'N':
            break
print(f'Você digitou o número {cont[num]}')


