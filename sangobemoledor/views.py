# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.views.generic import CreateView, View, TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

class Inicio(TemplateView):
	template_name = 'inicio.html' 

def inicio_sesion(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user:
                        if user.is_active:
                                login(request, user)
                                return HttpResponseRedirect('/')
                        else:
                                messages.warning(request, 'Tu cuenta aun no esta activada, por favor revisa tu correo')
                                return HttpResponseRedirect('/inicio-sesion/')
                else:
                        messages.error(request, 'Usuario o contraseña inválidos')
                        return HttpResponseRedirect('/inicio-sesion/')
        else:
                return render(request, 'inicio_sesion.html', {})
                
