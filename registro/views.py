# -*- coding: UTF-8 -*-
from django.views.generic import CreateView, View, TemplateView
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
import random, string

from .models import RegistroUsuario
from .forms import FormaRegistro 

class VistaErrorActivacion(TemplateView):
    template_name = 'registro/error_activacion.html'
   
class VistaErrorUsuarioActivo(TemplateView):
    template_name = 'registro/usuario_ya_activo.html'

class VistaUsuarioActivo(TemplateView):
    template_name = 'registro/usuario_activo.html'

class VistaRegistro(CreateView):
    model = RegistroUsuario
    form_class = FormaRegistro
    template_name = 'registro/registro.html'
    
    def form_valid(self, form):
        form.instance.is_active = False
        form.instance.activation_key = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for n in range(20))
        usuario = form.cleaned_data.get('correo')
        html_content = 'Por favor visite http://sangobemoledor.com/activar/%s/ para activar su cuenta'%(form.instance.activation_key)
        msg = EmailMultiAlternatives('Código de Activación',html_content,'registration@midiminio.com',[usuario])
        msg.attach_alternative(html_content,'text/html')
        msg.send()
        return super(VistaRegistro, self).form_valid(form)

class VistaActivaUsuario(View):
   
    def dispatch(self, *args, **kwargs):
        self.codigo = self.kwargs['codigo']
        return super(VistaUsuarioActivo, self).dispatch(*args, **kwargs)
       
    def get(self, request, *args, **kwargs):
        try:
            self.usuario = RegistroUsuario.objects.get(
                activation_key=self.codigo)
            if self.usuario.is_active == False:
                self.usuario.is_active = True
                self.usuario.save()
                return HttpResponseRedirect("/registro/activo_exito/")
            else:
                return HttpResponseRedirect("/registro/activo/")
        except RegistroUsuario.NotExist:
            return HttpResponseRedirect('/registro/error_activacion')
