# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, View, TemplateView, DetailView
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Perfil
from registro.models import RegistroUsuario
# Create your views here.

#Para esta clase utilizare la url /cuenta/usuario
class VistaPerfilPublico(DetailView):
	#model = Perfil
	template_name = 'perfil/perfil.html'
	

	#Aqui obtenemos el usuario, mediante el url
	def dispatch(self, *args, **kwargs):
		try:
			self.usuario = RegistroUsuario.objects.get(username=self.kwargs['usuario'])
		except RegistroUsuario.DoesNotExist: 
			return HttpResponseRedirect("/cuenta/usuario_inexistente")
		#print('hey')
		return super(VistaPerfilPublico, self).dispatch(*args, **kwargs)	

	def get_object(self):
		print('ho')
		try:
			return Perfil.objects.get(usuario=self.usuario.pk)
		except Perfil.DoesNotExist:
			return None
		
'''

try:
			self.perfil =  Perfil.objects.get(usuario=self.usuario.pk)
		except Perfil.DoesNotExist:
			return HttpResponseRedirect('/cuenta/cuenta_desactivada')
	def get_context_data(self, **kwargs):
		persona = self.get_object()
		if persona == None:
			return HttpResponseRedirect("/cuenta/desactivada")
		context = super(VistaPerfilPublico, self).get_context_data(**kwargs)
		return context
		'''





#Aqui repetiré basicamente lo de la clase anterior, pero se agregará el metodo de edicion bajo un url /cuenta/codsuarioactivacion
'''
def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        try:
			self.persona = Perfil.objects.get(usuario=self.usuario)
			if self.persona.usuario.is_active == True:
				context = super(VistaPerfilPublico, self).get_context_data(**kwargs)
				return 	context
			else:
				return HttpResponseRedirect("/cuenta/cuenta_desactivada") #agregar a los urls
		except Perfil.DoesNotExist:
			return HttpResponseRedirect("/cuenta/inexistente") #Agregar a los ursl

        '''

