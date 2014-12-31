# -*- coding: UTF-8 -*-
from django.views.generic import CreateView, View, TemplateView
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import random, string

from .models import RegistroUsuario
<<<<<<< HEAD
from .forms import FormaRegistro 
from cuenta.models import Perfil ## Agrego esto
=======
from .forms import FormaRegistro
from cuenta.models import Perfil #Agregado para la creacion de un perfil una vez que se activa la cuenta 
>>>>>>> branch-juan

class VistaRegistro(CreateView):
    model = RegistroUsuario
    form_class = FormaRegistro
    template_name = 'registro/registro.html'
    success_url = '/registro/registro_exito/'
    
    def form_valid(self, form):
    	#Cambiamos el valor por omision para que sea forzosa su activacion
    	form.instance.is_active = False
    	#generamos una clave de activacion horrible como suelen ser
    	form.instance.activation_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(20))
    	#obtenemos el campo de la base de datos para los datos de envio
    	usuario = form.cleaned_data.get('correo')
    	#Redactamos el contenido, aquí modifiquen el URL propio :3
    	contenido_html = 'Por favor visite http://127.0.0.1:8000/registro/activar/%s/ para activar su cuenta' %(form.instance.activation_key)
    	msg = EmailMultiAlternatives('Código de Activación',contenido_html,'cgah.95@gmail.com',[usuario])
    	#anexamos el contenido
    	msg.attach_alternative(contenido_html,'text/html')
    	#se envia el correo
    	msg.send()
    	return super(VistaRegistro, self).form_valid(form)

#Vista de activacion, con sus respectivos redireccionamientos
class VistaUsuarioActivacion(CreateView):

	def dispatch(self, *args, **kwargs):
	        self.codigo = self.kwargs['CODIGO']
	        return super(VistaUsuarioActivacion, self).dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
	    try:
	        self.usuario = RegistroUsuario.objects.get(activation_key=self.codigo)
	        if self.usuario.is_active == False:
	            self.usuario.is_active = True
	            self.usuario.save()
<<<<<<< HEAD
                #Si es exitoso creamos tambien el perfil
=======
                #Aquí agrego la creacion de un perfil
>>>>>>> branch-juan
                self.perfil = Perfil()
                self.perfil.usuario = self.usuario
                self.perfil.save()
	            return HttpResponseRedirect("/registro/activacion_exitosa/")
	        else:
	            return HttpResponseRedirect("/registro/ya_activo/")
	    except RegistroUsuario.DoesNotExist:
	        return HttpResponseRedirect('/registro/error_activacion') 

#Vistas resultantes de acuerdo al intento de activacion
class VistaActivacionExitosa(TemplateView):
	template_name = 'registro/usuario_activo.html'
class VistaYaActivo(TemplateView):
	template_name = 'registro/usuario_ya_activo.html'
class VistaError(TemplateView):
	template_name = 'registro/error_activacion.html'
class VistaExito(TemplateView):
	template_name = 'registro/registro_exito.html'
