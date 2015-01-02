# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from .views import *
from .views import VistaEdicion
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('.views',
				url(r'^perfil/(?P<usuario>.+)/$',VistaPerfilPublico.as_view(), name='perfil'),
				url(r'^editar/(?P<pk>.+)/$',VistaEdicion.as_view(), name='editar'),
                url(r'^error/usuario_inexistente/$',UsuarioInexistente.as_view(), name='error'),
)
