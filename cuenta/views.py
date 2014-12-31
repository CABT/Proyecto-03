# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, View, TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Perfil
from registro.models import RegistroUsuario
# Create your views here.

#Para esta clase utilizare la url /cuenta/usuario
class VistaPerfilPublico(CreateView):
	#Aqui obtenemos el usuario, mediante el url
	def dispatch(self, *args, **kwargs):
		try:
			self.usuario = RegistroUsuario.objects.get(username=self.kwargs['usuario'])
		except:
			return HttpResponseRedirect("/cuenta/error")
                return super(VistaPerfilPublico, self).dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		try:
			self.persona = Perfil.objects.get(usuario=self.usuario)
			if self.persona.usuario.is_active == True:
				return HttpResponseRedirect("/")
			else:
				return HttpResponseRedirect("/cuenta/cuenta_desactivada") #agregar a los urls




#Aqui repetiré basicamente lo de la clase anterior, pero se agregará el metodo de edicion bajo un url /cuenta/codsuarioactivacion
'''
def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        '''

