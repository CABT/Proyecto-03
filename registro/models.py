from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFill

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
    pais = CountryField()
    
    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
 
