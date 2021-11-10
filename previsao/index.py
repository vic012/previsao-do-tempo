import requests

class Prev:

	def __init__(self):
		#Link da API
		self._api = 'https://api.hgbrasil.com/weather?'
		#Chave de acesso a API
		self._key = '1eff744c'
		#Recebe o resultado
		self._resultado = {}
		
	def dados(self):
		#Acessando o IP do usuário
		ip = requests.get('https://api.ipify.org/')
		#Acessa os dados em Json da API
		dados = requests.get(f'{self._api}fields=only_results,city_name,forecast,date,weekday,max,min,description&key={self._key}&user_ip={ip}')
		#Se a API for acessada com sucesso
		if (dados.status_code == 200):
			self._resultado = dados.json()
		#Se a API não for acessada corretamente
		else:
			self._resultado = 'Erro no processamento das informações'

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