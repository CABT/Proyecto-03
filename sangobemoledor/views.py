from django.http import HttpResponse
from django.views.generic import CreateView, View, TemplateView


#def index(request):
#    return HttpResponse("HOLALSyALSAS")

class Inicio(TemplateView):
	template_name = 'inicio.html' 

