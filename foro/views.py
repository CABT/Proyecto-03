from django.http import Http404
from django.shortcuts import render
from django.views import generic
from . import models

class VistaForo(generic.ListView):
    model = models.Categoria
    template_name = "foro/foro.html"

class VistaCategoria(generic.ListView):
    template_name = "foro/categoria.html"
    paginate_by = 15
    model = models.Hilo
    context_object_name = 'hilos'

    def get_queryset(self):
        try:
            self.sl =  self.kwargs['slug']
            object_list = self.model.objects.filter(publica = True, categoria__slug = self.sl)
        except:
            raise Http404
        return object_list

    def dispatch(self, *args, **kwargs):
        return super(VistaCategoria, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(VistaCategoria, self).get_context_data(**kwargs)
        context['slug'] = self.sl
        return context

    def get_categoria(self):
        return Hilo.objects.get(slug = self.sl).categoria.titulo

class VistaHilo(generic.ListView):
    template_name = "foro/hilo.html"
    paginate_by = 15
    model = models.Comentario
    context_object_name = 'comentarios'

    def get_queryset(self):
        try:
            id =  self.kwargs['id']
            object_list = self.model.objects.filter(publica = True, hilo__id = id)
        except:
            raise Http404
        return object_list

    def dispatch(self, *args, **kwargs):
        return super(VistaHilo, self).dispatch(*args, **kwargs)

    

