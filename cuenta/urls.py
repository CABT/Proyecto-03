# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('.views',
                url(r'^(?P<usuario>.+)/$',VistaPerfilPublico.as_view(), name='perfil'),
)