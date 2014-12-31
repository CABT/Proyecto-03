from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import Inicio
from sangobemoledor import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Inicio.as_view(), name='inicio'),
                       url(r'^registro/', include('registro.urls')),
                       url(r'^cuenta/', include('cuenta.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    url(r'^cerrar-sesion/', views.cerrar_sesion, name='cerrar-sesion'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
