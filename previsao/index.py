import requests

class Prev:

	def __init__(self, localidade):
		#Pega a localidade da pessoa
		self._localidade = localidade
		#Link da API
		self._api = 'https://api.hgbrasil.com/weather?'
		#Chave de acesso a API
		self._key = 'f21d6ed6'
		#Recebe o resultado
		self._resultado = {}
		
	def dados(self):
		#Acessa os dados em Json da API
		dados = requests.get(f'{self._api}fields=only_results,city_name,forecast,date,weekday,max,min,description&key={self._key}&city_name={self._localidade}')
		#Se a API for acessada com sucesso
		if (dados.status_code == 200):
			self._resultado = dados.json()
		#Se a API não for acessada corretamente
		else:
			self._resultado = 'Erro no processamento das informações ou o limite de consultas à API por nome de cidade foi atingido'

	@property
	def resultado(self):
		return self._resultado

""" Teste do módulo
teste = Prev()
teste.dados()
for item in teste.resultado['forecast']:
	print(item)
#print(teste.resultado['forecast'])
"""