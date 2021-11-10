from django.shortcuts import render
from django.views.generic import View
from .index import Prev

class Index(View):
	template_name = 'index.html'

	def get(self, request):
		#acessa a API
		api = Prev()
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
		print(contexto)
		return render(request, self.template_name, contexto)
