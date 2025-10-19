from time import sleep
from emoji import emojize
for cont in range(10, -1, -1):
    print(cont) # faz a contagem
    sleep(1) # da tempo de 1 segundo
print('-=' * 10)
print(emojize('{} :sparkler: FELIZ ANO NOVO!!! :fireworks: {}'.format('\033[35;107m', '\033[m')))
print('-=' * 10)