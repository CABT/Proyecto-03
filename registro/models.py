from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

<<<<<<< HEAD
# Create your models here.

class Usuario(models.Model):

    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=50)
    pais = CountryField()
    imagen = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.nombre
=======
# Esto debe sobrevivir al pull
>>>>>>> 4051e82673f472ee9bc79cc865d17d2f1946be10
