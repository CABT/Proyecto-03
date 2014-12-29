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
        return super(VistaRegistro, self).form_valid(form)
