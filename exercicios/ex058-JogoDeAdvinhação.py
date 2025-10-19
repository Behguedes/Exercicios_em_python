from random import randint
computador = randint (0, 10)
print('Sou seu computador... Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
cont = 1
palpite = int(input('Qual é o seu palpite? '))
while palpite != computador:
        if palpite > computador:
            print('Menos...', end=' ')
        elif palpite < computador:
           print('Mais...', end=' ')
        cont += 1
        palpite = int(input('Tente outra vez: '))
print('Jogador venceu com {} tentativas. Parabéns!'.format(cont))