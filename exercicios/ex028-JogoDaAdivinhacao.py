from random import randint
from time import sleep
computador = randint(1, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Computer say: Pensei em um número entre 0 e 5, guess what!')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
