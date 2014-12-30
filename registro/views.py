# -*- coding: UTF-8 -*-
from django.views.generic import CreateView, View, TemplateView
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
import random, string

from .models import RegistroUsuario
from .forms import FormaRegistro 

class VistaRegistro(CreateView):
    model = RegistroUsuario
    form_class = FormaRegistro
    template_name = 'registro/registro.html'
    
    def form_valid(self, form):
    	#Cambiamos el valor por omision para que sea forzosa su activacion
    	form.instance.is_active = False
    	#generamos una clave de activacion horrible como suelen ser
    	form.instance.activation_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in range(20))
    	#obtenemos el campo de la base de datos para los datos de envio
    	usuario = form.cleaned_data.get('correo')
    	#Redactamos el contenido
    	contenido_html = 'Por favor visite http://127.0.0.1:8000/activar/%s/ para activar su cuenta' %(form.instance.activation_key)
    	msg = EmailMultiAlternatives('Código de Activación',contenido_html,'cgah.95@gmail.com',[usuario])
    	#anexamos el contenido
    	msg.attach_alternative(contenido_html,'text/html')
    	#se envia el correo
    	msg.send()
    	return super(VistaRegistro, self).form_valid(form)
