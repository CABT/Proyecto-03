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

    def get_queryset(self):
        try:
            slug=  self.kwargs['slug']
            object_list = self.model.objects.filter(publica = True, categoria__slug = slug)
        except:
            raise Http404
        return object_list

class VistaHilo(generic.ListView):
    template_name = "foro/hilo.html"
    paginate_by = 15
    model = models.Comentario

    def get_queryset(self):
        try:
            idd =  self.kwargs['id']
            object_list = self.model.objects.filter(publica = True, id = idd)
        except:
            raise Http404
        return object_list
    

