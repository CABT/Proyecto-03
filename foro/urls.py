from django.conf.urls import patterns, url
from . import views
from . import models

urlpatterns = patterns(
    '',
    url(r'^$', views.VistaForo.as_view(), kwargs=(), name='foro'),
    url(r'^categoria/(?P<slug>\S+)$', views.VistaCategoria.as_view(), kwargs=dict(model=models.Categoria), name='categoria'),
    url(r'^hilo/(?P<cat>\S+)/(?P<id>\d+)$', views.VistaHilo.as_view(), kwargs=dict(model=models.Hilo),  name='hilo'),
    url(r'^crear/(?P<slug>\S+)$',views.HacerHilo.as_view(), name='crea-hilo'),
    url(r'^crear-post/(?P<cat>\S+)/(?P<id>\d+)$',views.HacerComentario.as_view(), name='crea-comentario'),
)
