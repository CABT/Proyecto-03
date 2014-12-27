from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
<<<<<<< HEAD
from imagekit.models import ProcessedImageField 
from imagekit.processors import ResizeToFill
=======
from django.contrib.auth.models import User
#comentario bobo
from django.db import models	
>>>>>>> 5b303d0594085341b1149d62ddded4cfdbc03078

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
 
