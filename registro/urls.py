from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('.views',
                url(r'^$',VistaRegistro.as_view(), name='registro'),
                url(r'^activar/(?P<codigo>.+)/$', 
                    VistaActivaUsuario.as_view(), name='activar_usuario'),
                url(r'^activo/$',VistaErrorUsuarioActivo.as_view(), 
                    name='activo'),
                url(r'^activo_exito/$',VistaUsuarioActivo.as_view(), 
                    name='exito_activacion'),
                url(r'^error_activacion/$',VistaErrorActivacion.as_view(), 
                    name='error_activacion'),
)
