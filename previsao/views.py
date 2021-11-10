from django.shortcuts import render
from django.views.generic import View
from .index import Prev

class Index(View):
	template_name = 'index.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		cidade_user = request.POST['cidade'].title()
		uf = request.POST['estado'].upper()
		localidade = f'{cidade_user}, {uf}'
		api = Prev(localidade)
		#Acessa os dados da API
		api.dados()
		#Recebe os dodos individuais
		data = str()
		cidade = str()
		resultado = {}
		if (type(api.resultado) == type('')):
			resultado = api.resultado
		else:
			data = api.resultado['date']
			cidade = api.resultado['city_name']
			resultado = api.resultado['forecast']

		contexto = {
			'data': data,
			'cidade': cidade,
			'dados': resultado
		}
		
		return render(request, self.template_name, contexto)

class Teste(View):
	template_name = 'teste.html'

	def get(self, request):
		contexto = {
			'dados': request.META.get('REMOTE_ADDR')
		}
		return render(request, self.template_name, contexto)
