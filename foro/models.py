# -*- coding: UTF-8 -*-
from django.db import models
from  registro.models import RegistroUsuario
        
class Categoria(models.Model):

    titulo = models.CharField(max_length=60, unique =True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.titulo
        
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("categoria", kwargs={"slug": self.slug,})
        
    class Meta:
        verbose_name_plural = "Categorías"
        
class Hilo(models.Model):

    titulo = models.CharField(max_length=60)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(RegistroUsuario)
    contenido = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    publica = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.titulo
        
    def __unicode__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("hilo", kwargs={"cat": self.categoria__slug, "id": self.id, "slug": self.slug,})

    class Meta:
        verbose_name_plural = "Hilos"
        ordering = ["-fecha"]
    
class Comentario(models.Model):
    
    usuario = models.ForeignKey(RegistroUsuario)
    hilo = models.ForeignKey(Hilo)
    contenido = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    publica = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
        
    def __unicode__(self):
        return str(self.id)

    def get_categoria(self):
        return self.hilo.categoria

    get_categoria.short_description = 'Categoría'

    class Meta:
        verbose_name_plural = "Comentarios"
        ordering = ["-fecha"]

        
class DenunciaComentario(models.Model):
    comentario = models.ForeignKey(Comentario)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comentario
        
    def __unicode__(self):
        return self.comentario

    class Meta:
        verbose_name = "Comentario denunciado"
        verbose_name_plural = "Comentarios denunciados"
        ordering = ["-fecha"]
        
class DenunciaHilo(models.Model):
    hilo = models.ForeignKey(Hilo)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.hilo
        
    def __unicode__(self):
        return self.hilo

    class Meta:
        verbose_name = "Hilo denunciado"
        verbose_name_plural = "Hilos denunciados"
        ordering = ["-fecha"]
