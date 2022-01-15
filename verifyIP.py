# DIO/ Curso: Segurança da Informação com Python
# Professor: Bruno de Campos
# Data: 15 de janeiro de 2022
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)
dados = json.load((resposta))

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['region']

print('\nDetalhes do IP externo:\n')
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}'.format(org, regiao, pais, cid, ip))

print('\n Trabalho concluído!\n ;-)')
