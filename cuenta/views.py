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
			return HttpResponseRedirect("/cuenta/error/usuario_inexistente")
		#print('hey')
		return super(VistaPerfilPublico, self).dispatch(*args, **kwargs)	

	def get_object(self):
		print('ho')
		try:
			return Perfil.objects.get(usuario=self.usuario.pk)
		except Perfil.DoesNotExist:
			return None



