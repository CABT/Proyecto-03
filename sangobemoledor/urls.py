from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sangobemoledor.views.index', name='inicio'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registro/', include('registro.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
