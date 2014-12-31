from django.shortcuts import render
from django.views.generic import CreateView, View, TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Perfil
# Create your views here.

#Para esta clase utilizare la url /cuenta/usuario
class VistaPerfilPublico(CreateView):
	#Aqui obtenemos el usuario, mediante el url
	def dispatch(self, *args, **kwargs):
	    self.usuario = self.kwargs['usuario']
	    return super(VistaPerfil, self).dispatch(*args, **kwargs)
	def get(self, request, *args, **kwargs):
		try:


#Aqui repetiré basicamente lo de la clase anterior, pero se agregará el metodo de edicion bajo un url /cuenta/usuario/codigousuarioactivacion
	    return super(VistaPerfilPublico, self).dispatch(*args, **kwargs)
	def get(self, request, *args, **kwargs):
		try:
			self.persona = Perfil.objects.get(usuario=self.usuario)
			if self.persona.is_active == False
				return HttpResponseRedirect("cuenta/cuenta_desactivada") # agregar a los urls
		except Perfil.DoesNotExist:
			return HttpResponseRedirect("cuenta/error") #agregar a los urls





#Aqui repetiré basicamente lo de la clase anterior, pero se agregará el metodo de edicion bajo un url /cuenta/codsuarioactivacion


