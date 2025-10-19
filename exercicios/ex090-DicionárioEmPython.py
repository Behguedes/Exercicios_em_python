dicionario = {}
dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input(f'Média de {dicionario["Nome"]}: '))
print('-=' * 20)
if dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'
elif 5 <= dicionario['Média'] < 7:
    dicionario['Situação'] = 'Recuperação'
else:
    dicionario['Situação'] = 'Reprovado'
for n, m in dicionario.items():
    print(f'{n} é igual a {m}')