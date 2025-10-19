veloz = float(input('Qual é a velocidade atual do carro? '))
if veloz > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa no valor de R${:.2f}!'.format((veloz-80)*7))
print('Tenha um bom dia! Dirija com segurança!')