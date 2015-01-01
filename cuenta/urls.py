# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('.views',
                       url(r'^perfil/(?P<usuario>.+)/$',VistaPerfilPublico.as_view(), name='perfil'),
                       url(r'^error/usuario_inexistente/$',UsuarioInexistente.as_view(), name='error'),
)
