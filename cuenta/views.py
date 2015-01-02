# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, View, TemplateView, DetailView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Perfil
from .forms import FormaEdicionPerfil
from registro.models import RegistroUsuario
from registro.forms import FormaRegistro
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

#class VistaPerfilPersonal(TemplateView)


class VistaEdicion(UpdateView):
	context_object_name = 'usuario'
	model = RegistroUsuario
	form_class = FormaEdicionPerfil
	template_name = 'perfil/edicion_perfil.html'
	success_url = '/'

	#get object
	def form_valid(self, form):
		#print(form.cleaned_data['correo'])
		return super(VistaEdicion, self).form_valid(form)


	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		try:
			self.object = RegistroUsuario.objects.get(pk=self.kwargs['pk'])
		except RegistroUsuario.DoesNotExist:
			return HttpResponseRedirect("/cuenta/error/usuario_inexistente") #Editar la redireccion
		return super(VistaEdicion, self).dispatch(*args, **kwargs)


	



#Templates de error
class UsuarioInexistente(TemplateView):
	template_name = 'perfil/usuario_inexistente.html'

