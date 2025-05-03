from datetime import date
dicionario = {'nome': str(input('Nome: ')),
              'idade': int(input('Ano de nascimento: ' )),
              'CTPS': int(input('Carteira de trabalho (0 não tem): '))}
idade = date.today().year - dicionario['idade']
dicionario['idade'] = idade
if dicionario['CTPS'] != 0:
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['idade'] + ((dicionario['contratação'] + 35) - date.today().year)
    if dicionario['aposentadoria'] >= 0:
        print(f'A {dicionario['nome']} irá se aposentar com {dicionario['aposentadoria']}')
else:
    print('Carteira de trabalho vazia')
print('-=' * 30)
for k, v in dicionario.items():
    print(f'  - {k} tem o valor {v}')


