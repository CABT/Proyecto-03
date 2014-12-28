# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFill
from django.utils.encoding import smart_unicode
 
# Create your models here.

class RegistroUsuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    clave_activacion = models.CharField(max_length=30)
    avatar = ProcessedImageField(upload_to='media',
                                 processors=[ResizeToFill(50,50)],
                                 format='JPEG',
                                 options={'quality: 75'},
                                 default='media/img_usuario_default.png'
                                 )
    pais = CountryField(verbose_name='País')
    correo = models.EmailField(verbose_name='Dirección de correo', unique=True,
                              max_length=255)
    fecha = models.DateTimeField(verbose_name='Fecha de registro', auto_now_add=True,
                                 auto_now=False)
    
    def __str__(self):
        return smart_unicode(self.nombre)

    def __unicode__(self):
        return smart_unicode(self.nombre)
 
