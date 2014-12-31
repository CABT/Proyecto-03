# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFill
 
# Create your models here.

class RegistroUsuario(AbstractUser):
    avatar = ProcessedImageField(verbose_name='Foto de Perfil', upload_to='/static/registro/media',
                                 processors=[ResizeToFill(50,50)],
                                 format='JPEG',
                                 options={'quality: 75'},
                                 default='/static/registro/media/img_usuario_default.png'
                                 )
    pais = CountryField(verbose_name='País')
    correo = models.EmailField(verbose_name='Dirección de correo', unique=True,
                              max_length=255)
    descripcion = models.CharField(verbose_name='Descripción', max_length=255,
                                   null = True, blank = True)
    activation_key = models.CharField(default='12345',max_length=30)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username
 
