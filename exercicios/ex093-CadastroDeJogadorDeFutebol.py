dicionario = dict()
dicionario['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicionario["nome"]} jogou? '))
gols = []
for v in range(partidas):
    gols.append(int(input(f'    Quantos gols na partida {v}? ')))
dicionario['gols'] = gols[:]
dicionario['total'] = sum(gols)
print('-=' * 30)
print(dicionario)
print('-=' * 30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dicionario['nome']} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dicionario['total']} gols.')
