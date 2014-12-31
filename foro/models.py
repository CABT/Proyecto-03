from django.db import models

class Categoria(models.Model):

    titulo = models.CharField(max_length=60)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.titulo
        
    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Categorías"
        
class Hilo(models.Model):

    categoria = models.ForeignKey(Categoria)
    titulo = models.CharField(max_length=60)
    contenido = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    publica = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
        
    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Hilos"
    
class Comentario(models.Model):

    hilo = models.ForeignKey(Hilo)
    contenido = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = "Comentarios"
        
class DenunciaComentario(models.Model):
    comentario = models.ForeignKey(Comentario)

    def __str__(self):
        return self.comentario
        
    def __unicode__(self):
        return self.comentario

    class Meta:
        verbose_name = "Comentario denunciado"
        verbose_name_plural = "Comentarios denunciados"
        
        
class DenunciaHilo(models.Model):
    hilo = models.ForeignKey(Hilo)

    def __str__(self):
        return self.hilo
        
    def __unicode__(self):
        return self.hilo

    class Meta:
        verbose_name = "Hilo denunciado"
        verbose_name_plural = "Hilos denunciados"
