while True:
    num = int(input('Quar ver a tabuada de qual valor? '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
