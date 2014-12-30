from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('.views',
                url(r'^$',VistaRegistro.as_view(), name='registro'),
                #Esta será la url que reciba el usuario a registrar por correo y mandará a llamar el método que verificará la validez
                url(r'^activar/(?P<codigo_activacion>.+)/$',VistaUsuarioActivacion.as_view(),name='activar_usuario'),
                #Se mandará a esta en caso de exito
                url(r'^activacion_exitosa/$',VistaActivacionExitosa.as_view(),name='exito'),
                #si el usuario ya existe, se redireccionara a esta url, con el template correspondiente
                url(r'^ya_activo/$',VistaYaActivo.as_view(),name='ya_activo'),
                #Si no existe el usuario, mandaremos este template de error
                url(r'^error_activacion/$',VistaError.as_view(),name='error'),
)
