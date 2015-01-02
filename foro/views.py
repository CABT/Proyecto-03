from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from . import models
from . import forms

class VistaForo(generic.ListView):
    model = models.Categoria
    template_name = "foro/foro.html"

class VistaCategoria(generic.ListView):
    template_name = "foro/categoria.html"
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

class HacerHilo(generic.CreateView):
    model = models.Hilo
    form_class = forms.HiloForma
    success_url = "/foro/"
    template_name = 'foro/crea-hilo.html'

    def dispatch(self, *args, **kwargs):
        self.categoria = models.Categoria.objects.get(slug=self.kwargs['slug'])
        return super(HacerHilo, self).dispatch(*args, **kwargs)

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        form.instance.categoria = self.categoria
        return super(HacerHilo,self).form_valid(form)

class HacerComentario(generic.CreateView):
    model = models.Comentario
    form_class = forms.ComentarioForma
    success_url = "/foro/"
    template_name = 'foro/crea-comentario.html'

    def dispatch(self, *args, **kwargs):
        self.hilo = models.Hilo.objects.get(id=self.kwargs['id'])
        return super(HacerComentario, self).dispatch(*args, **kwargs)

    def form_valid(self,form):
        form.instance.usuario = self.request.user
        form.instance.hilo = self.hilo
        return super(HacerComentario,self).form_valid(form)
    
            

