def área(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terrano {largura}x{comprimento} é de {a}m²')

print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)