from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('.views',
                url(r'^$',VistaRegistro.as_view(), name='registro'),
)
