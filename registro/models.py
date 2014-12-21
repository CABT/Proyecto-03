from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
#comentario bobo
from django.db import models	

# Create your models here.

class Usuario(models.Model):

    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=50)
    pais = CountryField()
    imagen = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.nombre

#Tal vez a ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí#ustedes no
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
#ustedes no les importa pero a juan sí
