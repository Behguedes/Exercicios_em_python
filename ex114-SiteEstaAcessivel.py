from urllib import request, error

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site pudim não está acessível no momento!\033[m')
else:
    print('\033[31mConsegui acessar o site Pudim com sucesso!\033[m')
