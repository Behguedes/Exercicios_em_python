from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = computador + jogador
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0  else 'DEU ÍMPAR')
    if pi == 'p'.upper():
        if soma % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif pi == 'i'.upper():
        if soma % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')
