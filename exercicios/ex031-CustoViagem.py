distancia = float(input('Qual a distância da sua viagem? '))
print('Você esta prestes a começar uma viagem de {}Km.'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}!'.format(preço))



"""if distancia <= 200:
    print('E o preço da sua viagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}!'.format(distancia * 0.45))"""